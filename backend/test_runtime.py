from backend import model as m, runtime as r
from datetime import datetime, date
from dataclasses import replace
import sqlite3
import pytest
from os import path
from json import dumps
from threading import Thread
from time import sleep
import socket

class TestHandleCommand:
    initial_state = m.GlobalState()
    test_path = path.expanduser('~/.local/share/gre-prep/test/')
    test_db = path.join(test_path, 'gre_prep.db')
    
    def test_save_to_db(self):
        test_sub_state = {
            'start_time': datetime.strftime(datetime.now(),"%Y-%m-%d %H:%M:%S.%f"),
            'end_time': datetime.strftime(datetime(2027, 11, 8),"%Y-%m-%d %H:%M:%S.%f"),
            'question_type': 'Test Type',
            'question_module': 'Test Module',
            'is_answer_correct': True,
        }

        start_time = datetime.strptime(test_sub_state['start_time'], "%Y-%m-%d %H:%M:%S.%f") 
        end_time = datetime.strptime(test_sub_state['end_time'], "%Y-%m-%d %H:%M:%S.%f") 
        exec_time = end_time - start_time

        test_state = replace(
            self.initial_state,
            app_path = self.test_path,
            db_path = self.test_db,
            sub_state = test_sub_state,
        )

        cmd = m.Cmd.SAVE_TO_DB
        new_state, new_cmd = r.handle_command(test_state, cmd)

        conn = sqlite3.connect(new_state.db_path)

        try:
            with conn:
                c = conn.cursor()
                c.execute('SELECT * FROM problem_history WHERE exec_time = (SELECT MAX(exec_time) FROM problem_history);')
                test_data = c.fetchone()
        finally:
            conn.close()

        assert new_state == test_state
        assert new_cmd == m.Cmd.NONE
        assert test_data[0] == test_sub_state['start_time']
        assert test_data[1] == test_sub_state['question_type']
        assert test_data[2] == test_sub_state['question_module']
        assert test_data[3] == test_sub_state['is_answer_correct']
        assert test_data[4] == exec_time.total_seconds()

    def test_pull_stats(self):
        test_state = replace(
            self.initial_state,
            view_type = 'module view',
            app_path = self.test_path,
            db_path = self.test_db
        )

        new_state, new_cmd = r.handle_command(test_state, m.Cmd.PULL_STATS)

        assert new_cmd == m.Cmd.NONE
        assert new_state.state == m.AppStatus.STATS_PULLED
        assert new_state.problem_history != None

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
            'view_type': None,
            'problem_history': None,
        }
    }

    def test_other_target(self):
        json_dump = self.json_data.copy()
        json_dump['target'] = 'Math Server'

        msg = r.msg_factory(json_dump)
        assert msg == m.QueriedSubstate(message = json_dump['message'], payload = json_dump['payload'])

    def test_quit(self):
        json_dump = self.json_data.copy()
        msg = r.msg_factory(json_dump)
        assert msg == m.Msg.QUIT

    def test_write_db(self):
        json_dump = self.json_data.copy()
        json_dump['message'] = 'WRITE DB'
        msg = r.msg_factory(json_dump)
        assert msg == m.Msg.WRITE_DB

    def test_stats_requested(self):
        json_dump = self.json_data.copy()
        json_dump['message'] = 'StatsRequested'
        json_dump['payload']['view_type'] = 'create module view'
        msg = r.msg_factory(json_dump)
        assert msg == m.StatsRequested(view_type = json_dump['payload']['view_type'])

    def test_stats_loaded(self):
        problem_history = {
            'Foundations': {
                'test1': 1,
                'test2': 2,
            }
        }

        json_dump = self.json_data.copy()
        json_dump['message'] = 'StatsLoaded'
        json_dump['payload']['problem_history'] = problem_history
        msg = r.msg_factory(json_dump)
        assert msg == m.StatsLoaded(history = problem_history)

    def test_error(self):
        json_dump = self.json_data.copy()
        json_dump['message'] = 'Test'
        msg = r.msg_factory(json_dump)
        assert msg == m.Msg.ERROR

class TestRuntime():
    test_path = path.expanduser('~/.local/share/gre-prep/test/')
    test_socket = path.join(test_path, 'backend.sock')
    test_json = path.join(test_path, 'backend_model.json')
    initial_state = m.GlobalState(
        json_path = test_json,
        socket_path = test_socket
    )

    def test_runtime(self):
        runtime = r.Runtime(self.initial_state)
        json_data = dumps({
            'target': 'Backend',
            'message': 'StatsRequested',
            'payload': {
                'view_type': 'overview'
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
