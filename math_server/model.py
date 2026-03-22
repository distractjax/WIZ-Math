from dataclasses import dataclass, field, replace
from datetime import datetime
from enum import Enum, auto
from os import path
from math_server.function_dicts import category_dict
from typing import Union

class Cmd(Enum):
    GENERATE_QUESTION = auto()
    CHECK_ANSWER = auto()
    NONE = auto()

# Message classes
class Msg(Enum):
    # End the program
    QUIT = auto()
    WRITE = auto()
    ERROR = auto()

# Status classes
class AppStatus(Enum):
    IDLE = auto()
    GENERATING_QUESTION = auto()
    GENERATED_QUESTION = auto()
    ANSWER_SUBMITTED = auto()
    ANSWER_CHECKED = auto()

# NEW QUESTION state
@dataclass(frozen=True)
class NewQuestionRequested:
    # Derived from side-menu
    question_type: str
    # Derived from header
    question_module: str

@dataclass(frozen=True)
class NewQuestionGenerated:
    question: str
    answer: str

# RETRIVE ANSWER
@dataclass(frozen=True)
class AnswerSubmitted:
    user_answer: str
    end_time: datetime

@dataclass(frozen=True)
class AnswerChecked:
    is_answer_correct: bool

# State classes
@dataclass(frozen=True)
class MathState:
    question: str = ""
    question_type: str = ""
    question_module: str = ""
    math_modules: list = field(default_factory = lambda: [x for x in category_dict.keys()])
    math_functions: list = field(default_factory = lambda: [
        math_function
        for math_module in category_dict.values()
        for math_function in math_module.keys()
        ])
    answer: str = ""
    user_answer: str = ""
    is_answer_correct: bool = False
    start_time: datetime = field(default_factory = datetime.now)
    end_time: datetime = field(default_factory = datetime.now)

   # Path elements
    app_path: str = path.expanduser('~/.local/share/gre-prep')
    bus_path: str = path.join(app_path,'bus')
    json_path: str = path.join(bus_path,'math_model.json')
    socket_path: str = path.join(bus_path,'math_server.sock')

    is_running: bool = True
    state: AppStatus = AppStatus.IDLE
    write_safe: bool = False
