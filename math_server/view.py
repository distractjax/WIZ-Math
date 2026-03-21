from json import dump
from os import path, replace, mkdir
from tempfile import NamedTemporaryFile
import math_server.model as m
from math_server.update import update

def view(model: m.MathState):
    '''
    This turns my global state into a JSON object and prints it out.
    '''
    dir_name = path.dirname(model.bus_path)

    math_state = {
        "app_path": model.app_path,
        "bus_path": model.bus_path,
        "json_path": model.json_path,
        "socket_path": model.socket_path,
        "question": model.question,
        "question_type": model.question_type,
        "question_module": model.question_module,
        "answer": model.answer,
        "user_answer": model.user_answer,
        "math_modules": model.math_modules,
        "math_functions": model.math_functions,
        "is_answer_correct": model.is_answer_correct,
        "start_time": model.start_time.isoformat(),
        "end_time": model.end_time.isoformat(),
        "is_running": model.is_running,
        "state": model.state.name,
    }

    if path.exists(model.json_path):
        with NamedTemporaryFile('w', dir=dir_name, delete=False) as tf:
            dump(math_state,fp=tf,indent=4)
            temp_name = tf.name

        replace(temp_name, model.json_path)
    else:
        if not path.isdir(model.app_path):
            mkdir(model.app_path)
        if not path.isdir(model.bus_path):
            mkdir(model.bus_path)
        with open(file = model.json_path, mode = 'w') as f:
            dump(math_state,fp = f, indent = 4)

if __name__ == "__main__":
    write_json(m.MathState())
