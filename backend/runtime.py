from backend import function_dicts as fd, model as m, update as u, view as v, get_stats as gs
from json import loads, dumps
from datetime import datetime
import socket
from os import path, remove
import config

def msg_factory(json_data: dict[str, str]) -> u.Message: 
    '''
    This converts the JSON message received from the frontend into a message class defined on the backend.
    '''
    match json_data['message']:
        case "QUIT":
            return m.Msg.QUIT
        case "STATS REQUESTED":
            return m.Msg.STATS_REQUESTED
        case "NewQuestionRequested":
            return m.NewQuestionRequested(json_data['question_type'], json_data['question_module'])
        case "AnswerSubmitted":
            try:
                end_time = datetime.strptime(json_data['end_time'], "%Y-%m-%dT%H:%M:%S.%f")
            except Exception:
                end_time = datetime.now()
            return m.AnswerSubmitted(json_data['user_answer'], end_time)
        case _:
            return m.Msg.ERROR

def handle_command(model: m.GlobalState, cmd: m.Cmd) -> m.GlobalState:
    match cmd:
        case m.Cmd.GENERATE_QUESTION:
            question, answer = fd.category_dict[model.math.question_type][model.math.question_module]
            new_model, new_command = u.update(model, m.NewQuestionGenerated(question, answer))
            return handle_command(new_model, new_command)
        case m.Cmd.SAVE_A_TO_DB:
            config.update_question_row(was_right = model.math.is_answer_correct,
                exec_time = str(model.math.end_time - model.math.start_time),
                filepath = model.db_path)
            return model
        case m.Cmd.SAVE_Q_TO_DB:
            config.create_question_row(exec_time = model.math.start_time,
                q_type = model.math.question_type,
                q_func = model.math.question_module,
                filepath = model.db_path)
            return model
        case m.Cmd.CHECK_ANSWER:
            is_correct = model.math.answer == model.math.user_answer
            new_model, new_command = u.update(model, m.AnswerChecked(is_correct))
            return handle_command(new_model, new_command)
        case m.Cmd.PULL_STATS:
            view_type = model.view_type
            problem_history = gs.function_dict[view_type]
            new_model, new_command = u.update(model, m.StatsLoaded(problem_history))
            return handle_command(new_model, new_command)
        case m.Cmd.NONE:
            return model

class Runtime():
    def __init__(self):
        self.state = m.GlobalState(problem_history = None)
        self.clean_sock()
        
    def clean_sock(self):
        '''
        Unix sockets have to be deleted before they can be bound again.
        '''
        if path.exists(self.state.socket_path):
            remove(self.state.socket_path)

    def run(self):
        '''
        This is the backend runtime loop.
        '''
        print("Backend is running...")
        v.write_json(self.state)
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
                    self.state, command = u.update(self.state, msg)
                    self.state = handle_command(self.state, command)
                    response = {"status": "ok", "state": self.state.state.name}
                    conn.sendall(dumps(response).encode())
                    v.write_json(self.state)
        except Exception as e:
            print(f"Loop Error: {e}")
        finally:
            self.clean_sock()

if __name__ == "__main__":
    app = Runtime()
    app.run()
