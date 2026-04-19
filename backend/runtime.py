from math_server import function_dicts as fd 
from backend import model as m, update as u, view as v, get_stats as gs
from config import ensure_sqlite_table
from json import loads, dumps, load
from datetime import datetime
import socket
from os import path, remove
import sqlite3
import config

def msg_factory(json_data: dict) -> u.Message: 
    '''
    This converts the JSON message received from the frontend into a message class defined on the backend.
    '''
    if json_data['target'].lower() != 'backend':
        print(json_data['target'])
        return m.PostSubstate(message = json_data['message'], payload = json_data['payload'])

    match json_data['message']:
        case "QUIT":
            return m.Msg.QUIT
        case "WRITE DB":
            return m.Msg.WRITE_DB
        case "StatsRequested":
            return m.StatsRequested(view_type = json_data['payload']['view_type'])
        case "StatsLoaded":
            return m.StatsLoaded(history = json_data['payload']['problem_history'])
        case "GetSubstate":
            return m.GetSubstate(sub_state = load())
        case _:
            return m.Msg.ERROR

def handle_command(model: m.GlobalState, cmd: m.Cmd) -> tuple[m.GlobalState, m.Cmd]:
    match cmd:
        case m.Cmd.QUERY_SUBSTATE:
            # Fill this in with the following logic:
            # 1. Pass along the message and payload to the substate.
            # 2. Wait. 
            # 3. Retrieve the new substate.
            # 4. Return the model.
            # This probably needs to get split out among multiple other commands.
            return model, m.Cmd.NONE

        case m.Cmd.SAVE_TO_DB:
            config.ensure_application_path(model.app_path)
            # Down the road I really need to make the database schema and other project-specific things into a config file that can be swapped out per project.
            # I want to keep the backend as project-agnostic as possible.
            start_time = datetime.strptime(model.sub_state['start_time'], "%Y-%m-%d %H:%M:%S.%f") 
            end_time = datetime.strptime(model.sub_state['end_time'], "%Y-%m-%d %H:%M:%S.%f") 
            exec_time = end_time - start_time
            conn = sqlite3.connect(model.db_path)
            try:
                with conn:
                    c = conn.cursor()
                    ensure_sqlite_table(c, "problem_history", ["exec_time primary key","q_type","q_func","was_right","solve_time"])
                    sql = '''INSERT INTO problem_history (exec_time, q_type, q_func, was_right, solve_time)
                        VALUES(?, ?, ?, ?, ?);'''
                    c.execute(sql, (
                        start_time,
                        model.sub_state['question_type'],
                        model.sub_state['question_module'],
                        model.sub_state['is_answer_correct'],
                        exec_time.total_seconds())
                    )
            finally:
                conn.close()
            return model, m.Cmd.NONE

        case m.Cmd.PULL_STATS:
            view_type = model.view_type
            problem_history = gs.function_dict[view_type]
            new_model, new_command = u.update(model, m.StatsLoaded(problem_history))
            return handle_command(new_model, new_command)

        case m.Cmd.NONE:
            return model, cmd

        case _:
            return model, m.Cmd.ERROR

class Runtime():
    def __init__(self, init_state: m.GlobalState = m.GlobalState()):
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
        This is the backend runtime loop.
        '''
        print("Backend is running...")
        v.view(self.state)
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
                    while command != m.Cmd.NONE:
                        self.state, command = handle_command(self.state, command)
                    response = {"status": "ok", "state": self.state.state.name}
                    conn.sendall(dumps(response).encode())
                    v.view(self.state)
        except Exception as e:
            print(f"Loop Error: {e}")
        finally:
            self.clean_sock()

if __name__ == "__main__":
    app = Runtime()
    app.run()
