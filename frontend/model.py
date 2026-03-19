from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum, auto
from os import path

# State classes
@dataclass(frozen=True)
class TuiState:
    cursor_pos: tuple[int, int] = (0, 0)
    menu_selection: int = 0
    is_text_entry: bool = False
    header: str = ""
    footer: str = ""
    active_window: int = 0
    screen_width: int = 0
    screen_height: int = 0
    state: str = "MAIN MENU" #"MAIN MENU", "STATS", "QUESTION"
    is_running: bool = True

# Message classes
class Msg(Enum):
    QUIT = auto()

@dataclass(frozen=True)
class RequestNewQuestion:
    question_type: str
    question_module: str
