from json import dump
from os import path, replace
from tempfile import NamedTemporaryFile
import backend.model as m
from backend.update import update

def write_json(model: m.GlobalState):
    '''
    This turns my global state into a JSON object and prints it out.
    '''
    dir_name = path.dirname(model.app_path)

    global_state = {
        "problem_history": model.problem_history,
        "app_path": model.app_path,
        "backend_json_path": model.backend_json_path,
        "socket_path": model.socket_path,
        "db_path": model.db_path,
        "math": {
            "question": model.math.question,
            "question_type": model.math.question_type,
            "question_module": model.math.question_module,
            "answer": model.math.answer,
            "user_answer": model.math.user_answer,
            "math_modules": model.math.math_modules,
            "math_functions": model.math.math_functions,
            "is_answer_correct": model.math.is_answer_correct,
            "start_time": model.math.start_time.isoformat(),
            "end_time": model.math.end_time.isoformat(),
        },
        "is_running": model.is_running,
        "state": model.state.name,
    }

    with NamedTemporaryFile('w', dir=dir_name, delete=False) as tf:
        dump(global_state,fp=tf,indent=4)
        temp_name = tf.name

    replace(temp_name, model.backend_json_path)

if __name__ == "__main__":
    write_json(m.GlobalState(problem_history = None))
