from typing import Union
import model as m
from dataclasses import replace

Message = Union[m.Msg, m.RequestNewQuestion]

def update(model: m.TuiState, message: Message):
    match message:
        case m.Msg.QUIT:
            return replace(model, is_running = False)
        case _:
            return model
