from dataclasses import dataclass, field, replace
from datetime import datetime
from enum import Enum, auto
from os import path
from typing import TYPE_CHECKING, Union

if TYPE_CHECKING:
    import pandas as pd

# Okay, let's think about what the actual events are
# Step-by-step, what is my backend doing?
# 1. It's sitting idle and waiting for a request. (IDLE)
# 2. It receives a message to generate a new question and it then generates the question-answer pair. (NEW QUESTION)
# 5. It waits to receive the answer status and completion time from the frontend. (This can re-use the IDLE state).
# 6. It writes the answer status and completion time to the database. (LOG ANSWER)
# 7. It returns to IDLE.
# 8. It queries the database and converts that to a dataframe, manipulates data to get the right shape. (GET HISTORY)
    # 8a. I do think this qualifies as one event, even though there are multiple sub-parts.

# Okay, let's re-think this. Don't think of every event, just think: when does the backend change?
# 1. It's sitting idle
# 2. The user inputs a command to generate a new question. (GENERATE QUESTION)
# 3. A command runs and generates that question, returning the question and answer (RETRIEVE QUESTION)
# 4. A command runs and logs that question to the database

class Cmd(Enum):
    GENERATE_QUESTION = auto()
    SAVE_A_TO_DB = auto()
    SAVE_Q_TO_DB = auto()
    CHECK_ANSWER = auto()
    PULL_STATS = auto()
    NONE = auto()

# Message classes
class Msg(Enum):
    # End the program
    QUIT = auto()
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

# GET HISTORY state
@dataclass(frozen=True)
class StatsLoaded:
    df: "pd.DataFrame"

# State classes
@dataclass(frozen=True)
class MathState:
    question: str = ""
    question_type: str = ""
    question_module: str = ""
    answer: str = ""
    user_answer: str = ""
    is_answer_correct: bool = False
    start_time: datetime = field(default_factory = datetime.now)
    end_time: datetime = field(default_factory = datetime.now)

@dataclass(frozen=True)
class GlobalState:
    # History components
    problem_history: "pd.DataFrame"

    # Path elements
    app_path: str = path.expanduser('~/.local/share/gre-prep')
    json_path: str = path.join(app_path,'print_contents.json')
    db_path: str = path.join(app_path,'gre_prep.db')

    # State components
    math: MathState = field(default_factory = MathState)

    # Loop components
    is_running: bool = True
    state: AppStatus = AppStatus.IDLE

