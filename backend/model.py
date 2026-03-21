from backend.get_stats import function_dict
from dataclasses import dataclass, field, replace
from datetime import datetime
from enum import Enum, auto
from os import path
from typing import Union

class Cmd(Enum):
    PULL_STATS = auto()
    SAVE_A_TO_DB = auto()
    SAVE_Q_TO_DB = auto()
    QUERY_SUBSTATE = auto()
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
    FETCHING_DATA = auto()
    WRITING_DB = auto()

# STATS PULLED state
@dataclass(frozen=True)
class StatsLoaded:
    history: dict

# GET STATS state
@dataclass(frozen=True)
class StatsRequested:
    view_type: str

@dataclass(frozen=True)
class QueriedSubstate:
    message: str
    payload: dict

# State classes
# The new way that the backend is going to work:
# 1. The backend receives a message from the frontend.
# 2. The backend determines if it needs to send that message to the math server (m.ForwardMessage)
# 3. The backend receives the updated state from the math server and writes it (this doesn't need to be a message)
# 4. The backend checks the status of write_safe and, if true, writes its sub state to the db. (m.Msg.WRITE_DB)
@dataclass(frozen=True)
class GlobalState:
    # History components
    # Move these to the math_server
    problem_history: Union[dict, None] = None
    view_type: str = ""
    stats_functions: list = field(default_factory = lambda: [x for x in function_dict.keys()])

    # Path elements
    app_path: str = path.expanduser('~/.local/share/gre-prep')
    db_path: str = path.join(app_path,'gre_prep.db')
    bus_path: str = path.join(app_path,'bus')
    json_path: str = path.join(bus_path,'backend_model.json')
    socket_path: str = path.join(bus_path,'backend.sock')

    # State components
    sub_state: dict = field(default_factory = dict)

    # Loop components
    is_running: bool = True
    state: AppStatus = AppStatus.IDLE

