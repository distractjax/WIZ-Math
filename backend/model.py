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
# 3. It writes the question metadata to a database. (LOG QUESTION)
# 4. It sends a JSON object to the frontend containing the question and the answer. (PUSH QUESTION)
# 5. It waits to receive the answer status and completion time from the frontend. (This can re-use the IDLE state).
# 6. It writes the answer status and completion time to the database. (LOG ANSWER)
# 7. It returns to IDLE.
# 8. It queries the database and converts that to a dataframe, manipulates data to get the right shape. (GET HISTORY)
    # 8a. I do think this qualifies as one event, even though there are multiple sub-parts.
# 9. It converts the dataframe to a JSON object and pushes it to the frontend (PUSH HISTORY)

# State classes
@dataclass(frozen=True)
class MathState:
    question: str = ""
    question_type: str = ""
    question_module: str = ""
    answer: str = ""
    is_answer_correct: bool = False
    user_input: str = ""
    start_time: datetime = datetime.now()
    question_time: float = 0.0

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
    state: str = "IDLE"

# Message classes
class Msg(Enum):
    # End the program
    QUIT = auto()

# NEW QUESTION state
@dataclass(frozen=True)
class RequestNewQuestion:
    question_type: str
    question_module: str

# LOG QUESTION state
@dataclass(frozen=True)
class RequestLogQuestion:
    question_type: str
    question_module: str

# PUSH QUESTION state
@dataclass(frozen=True)
class RequestPushQuestion:
    question_type: str
    question_module: str

# NEW QUESTION state
@dataclass(frozen=True)
class RequestNewQuestion:
    question_type: str
    question_module: str

# NEW QUESTION state
@dataclass(frozen=True)
class RequestNewQuestion:
    question_type: str
    question_module: str

# NEW QUESTION state
@dataclass(frozen=True)
class RequestNewQuestion:
    question_type: str
    question_module: str

# NEW QUESTION state
@dataclass(frozen=True)
class RequestNewQuestion:
    question_type: str
    question_module: str
    
# NEW QUESTION state
@dataclass(frozen=True)
class RequestNewQuestion:
    question_type: str
    question_module: str
