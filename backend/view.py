from json import dump
from os import path, replace, mkdir
from tempfile import NamedTemporaryFile
import backend.model as m
from backend.update import update

def view(model: m.GlobalState):
    '''
    This turns my global state into a JSON object and prints it out.
    '''
    dir_name = path.dirname(model.app_path)

    global_state = {
        "problem_history": model.problem_history,
        "view_type": model.view_type,
        "stats_functions": model.stats_functions,
        "app_path": model.app_path,
        "db_path": model.db_path,
        "bus_path": model.bus_path,
        "json_path": model.json_path,
        "socket_path": model.socket_path,
        "sub_state": model.sub_state,
        "is_running": model.is_running,
        "state": model.state.name,
    }

    if path.exists(model.json_path):
        with NamedTemporaryFile('w', dir=dir_name, delete=False) as tf:
            dump(global_state,fp=tf,indent=4)
            temp_name = tf.name

        replace(temp_name, model.json_path)
    else:
        if not path.isdir(model.app_path):
            mkdir(model.app_path)
        if not path.isdir(model.bus_path):
            mkdir(model.bus_path)
        with open(file = model.json_path, mode = 'w') as f:
            dump(global_state,fp = f, indent = 4)

if __name__ == "__main__":
    view(m.GlobalState())
