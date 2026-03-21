from typing import Union
import backend.model as m
from dataclasses import replace
from datetime import datetime

Message = Union[
    m.Msg, 
    m.StatsRequested,
    m.StatsLoaded,
]

# The new way that the backend is going to work:
# 1. The backend receives a message from the frontend.
# 2. The backend determines if it needs to send that message to the math server (m.ForwardMessage)
# 3. The backend receives the updated state from the math server and writes it (this doesn't need to be a message)
# 4. The backend checks the status of write_safe and, if true, writes its sub state to the db. (m.Msg.WRITE_DB)

def update(model: m.GlobalState, message: Message) -> tuple[m.GlobalState, m.Cmd]:
    match message:
        case m.Msg.QUIT:
            return replace(model, is_running = False), m.Cmd.NONE

        case _:
            return model, m.Cmd.NONE

