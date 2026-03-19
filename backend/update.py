from typing import Union
import tea_model as tm
from dataclasses import replace

Message = Union[tm.Msg, tm.RequestNewQuestion]

def update(model: tm.GlobalState, message: Message):
    match message:
        case tm.Msg.QUIT:
            return replace(model, is_running = False)
        case tm.RequestNewQuestion(question_module, question_type):
            # Fill in this logic when you're less sleepy.
            return replace(model, math = 
                replace(model.math, 
                        question_module = question_module,
                        question_type = question_type,
                        )
            )
        case _:
            return model
