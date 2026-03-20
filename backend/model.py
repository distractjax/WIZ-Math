from dataclasses import dataclass, field, replace
from datetime import datetime
from enum import Enum, auto
from os import path
from backend.function_dicts import category_dict
from typing import Union

class Cmd(Enum):
    GENERATE_QUESTION = auto()
    PULL_STATS = auto()
    SAVE_A_TO_DB = auto()
    SAVE_Q_TO_DB = auto()
    CHECK_ANSWER = auto()
    NONE = auto()

# Message classes
class Msg(Enum):
    # End the program
    QUIT = auto()
    ERROR = auto()
    STATS_REQUESTED = auto()

# Status classes
class AppStatus(Enum):
    IDLE = auto()
    STATS_REQUESTED = auto()
    STATS_PULLED = auto()
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

# STATS PULLED state
@dataclass(frozen=True)
class StatsLoaded:
    history: dict

# GET STATS state
@dataclass(frozen=True)
class StatsRequested:
    view_type: str

# State classes
@dataclass(frozen=True)
class MathState:
    question: str = ""
    question_type: str = ""
    question_module: str = ""
    # This doesn't currently work, I need to change how category_dict works.
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

@dataclass(frozen=True)
class GlobalState:
    # History components
    problem_history: Union[dict, None]
    view_type: str = ""

    # Path elements
    app_path: str = path.expanduser('~/.local/share/gre-prep')
    backend_json_path: str = path.join(app_path,'backend_model.json')
    socket_path: str = path.join(app_path,'backend.sock')
    db_path: str = path.join(app_path,'gre_prep.db')

    # State components
    math: MathState = field(default_factory = MathState)

    # Loop components
    is_running: bool = True
    state: AppStatus = AppStatus.IDLE

