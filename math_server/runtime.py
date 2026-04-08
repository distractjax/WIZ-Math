from math_server import function_dicts as fd, model as m
from math_server.update import update, Message
from math_server.view import view
from typing import TypedDict
from json import loads, dumps
from datetime import datetime
import socket
from os import path, remove
import config

def msg_factory(json_data: dict) -> Message: 
    '''
    This converts the JSON message received from the backend into a message class defined on the math server.
    '''
    match json_data['message']:
        case "QUIT":
            return m.Msg.QUIT
        case "NewQuestionRequested":
            return m.NewQuestionRequested(
                json_data['payload']['question_type'],
                json_data['payload']['question_module']
            )
        case "AnswerSubmitted":
            try:
                end_time = datetime.strptime(json_data['payload']['end_time'], "%Y-%m-%dT%H:%M:%S.%f")
            except Exception:
                end_time = datetime.now()
            return m.AnswerSubmitted(json_data['payload']['user_answer'], end_time)
        case _:
            return m.Msg.ERROR

def handle_command(model: m.MathState, cmd: m.Cmd) -> tuple[m.MathState, m.Cmd]:
    match cmd:
        case m.Cmd.GENERATE_QUESTION:
            question, answer = fd.category_dict[model.question_module][model.question_type]()
            return update(model, m.NewQuestionGenerated(question, answer))
        case m.Cmd.CHECK_ANSWER:
            is_correct = model.answer == model.user_answer
            return update(model, m.AnswerChecked(is_correct))
        case m.Cmd.WRITE:
            return update(model, m.Msg.WRITE_SAFE)
        case m.Cmd.NONE:
            return model, cmd
        case _:
            return model, m.Cmd.ERROR

class Runtime():
    def __init__(self, init_state: m.MathState = m.MathState()):
        self.state = init_state
        self.clean_sock()
        
    def clean_sock(self):
        '''
        Unix sockets have to be deleted before they can be bound again.
        '''
        if path.exists(self.state.socket_path):
            remove(self.state.socket_path)

    def run(self):
        '''
        This is the math server runtime loop.
        '''
        print("Math server is running...")
        view(self.state)
        server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        server.bind(self.state.socket_path)
        server.listen(1)

        try:
            while self.state.is_running:
                conn, _ = server.accept()
                with conn:
                    data = conn.recv(4096).decode()
                    if not data:
                        continue
                    json_data = loads(data)
                    msg = msg_factory(json_data)
                    self.state, command = update(self.state, msg)
                    while command != m.Cmd.NONE:
                        self.state, command = handle_command(self.state, command)
                    response = {"status": "ok", "state": self.state.state.name}
                    conn.sendall(dumps(response).encode())
                    view(self.state)
        except Exception as e:
            print(f"Loop Error: {e}")
        finally:
            self.clean_sock()

if __name__ == "__main__":
    app = Runtime()
    app.run()
