from typing import Union
import model as m
from dataclasses import replace
import function_dicts

Message = Union[m.Msg, m.RequestNewQuestion]

def update(model: m.GlobalState, message: Message):
    match message:
        case m.Msg.QUIT:
            return replace(model, is_running = False)
        case m.RequestNewQuestion(question_module, question_type):
            # Fill in this logic when you're less sleepy.
            function_dicts.category_dict[question_module][question_type]()
            return replace(model, math = 
                replace(model.math, 
                        question_module = question_module,
                        question_type = question_type,
                        )
            )
        case _:
            return model
