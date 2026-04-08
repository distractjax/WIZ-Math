from math_server import model as m, runtime as r
from datetime import datetime
from dataclasses import replace
import socket
from json import dumps
from time import sleep
from threading import Thread
from os import path

class TestHandleCommand:
    initial_state = m.MathState()
    
    def test_generate_question(self):
        question_module = "Foundations"
        question_type = "multiply by fractions"
        test_state = replace(self.initial_state, 
            question_type = "multiply by fractions",
            question_module = "Foundations"
        )
        cmd = m.Cmd.GENERATE_QUESTION
        new_state, new_cmd = r.handle_command(test_state, cmd)
        assert new_state.state == m.AppStatus.GENERATED_QUESTION
        assert new_state.question != ""
        assert new_state.answer != ""
        assert new_cmd == m.Cmd.NONE

    def test_check_answer(self):
        test_state = replace(self.initial_state,
            answer = "2",
            user_answer = "2"
        )
        cmd = m.Cmd.CHECK_ANSWER
        new_state, new_cmd = r.handle_command(test_state, cmd)
        assert new_state.state == m.AppStatus.ANSWER_CHECKED
        assert new_state.is_answer_correct
        assert new_cmd == m.Cmd.WRITE

    def test_write(self):
        test_state = replace(self.initial_state,
            write_safe = True
        )
        cmd = m.Cmd.WRITE
        new_state, new_cmd = r.handle_command(test_state, cmd)
        assert new_state.state == m.AppStatus.IDLE
        assert new_cmd == m.Cmd.NONE

    def test_none(self):
        test_state = self.initial_state

        new_state, new_cmd = r.handle_command(test_state, m.Cmd.NONE)

        assert new_state == test_state
        assert new_cmd == m.Cmd.NONE

    def test_error(self):
        test_state = self.initial_state

        new_state, new_cmd = r.handle_command(test_state, m.Cmd.ERROR)

        assert new_state == test_state
        assert new_cmd == m.Cmd.ERROR

class TestMsgFactory:
    json_data = {
        'target': 'Backend',
        'message': 'QUIT',
        'payload': {
            'question_type': None,
            'question_module': None,
            'end_time': None,
            'user_answer': None,
        }
    }

    def test_quit(self):
        json_dump = self.json_data.copy()
        msg = r.msg_factory(json_dump)
        assert msg == m.Msg.QUIT

    def test_new_question(self):
        json_dump = self.json_data.copy()
        json_dump['message'] = 'NewQuestionRequested'
        json_dump['payload']['question_type'] = 'Test Question'
        json_dump['payload']['question_module'] = 'Test Module'

        msg = r.msg_factory(json_dump)
        assert msg == m.NewQuestionRequested(
            question_type = 'Test Question',
            question_module = 'Test Module'
        )

    def test_answer(self):
        right_now = datetime.strftime(datetime.now(),"%Y-%m-%dT%H:%M:%S.%f")
        json_dump = self.json_data.copy()
        json_dump['message'] = 'AnswerSubmitted'
        json_dump['payload']['end_time'] = right_now
        json_dump['payload']['user_answer'] = 'Test Answer'

        msg = r.msg_factory(json_dump)
        assert msg == m.AnswerSubmitted(
            user_answer = 'Test Answer',
            end_time = datetime.strptime(right_now, "%Y-%m-%dT%H:%M:%S.%f")
        )

    def test_error(self):
        json_dump = self.json_data.copy()
        json_dump['message'] = 'Test'
        msg = r.msg_factory(json_dump)
        assert msg == m.Msg.ERROR

class TestRuntime():
    test_path = path.expanduser('~/.local/share/gre-prep/test/')
    test_socket = path.join(test_path, 'math_server.sock')
    test_json = path.join(test_path, 'math_model.json')
    initial_state = m.MathState(
        json_path = test_json,
        socket_path = test_socket
    )

    def test_runtime(self):
        runtime = r.Runtime(self.initial_state)
        json_data = dumps({
            'target': 'Math',
            'message': 'NewQuestionRequested',
            'payload': {
                'question_type': 'multiply by fractions',
                'question_module': 'Foundations',
                'end_time': None,
                'user_answer': None,
            }
        })
        byte_data = json_data.encode()

        server_thread = Thread(target = runtime.run, daemon = True)
        server_thread.start()
        sleep(0.1)

        client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        client.connect(self.initial_state.socket_path)
        client.sendall(byte_data)

        response = client.recv(4096)
        print(f'Server replied: {response.decode()}')

        quit_msg = dumps({'message': 'QUIT'}).encode()
        client.sendall(quit_msg)
        client.close()
        server_thread.join(timeout=2)
