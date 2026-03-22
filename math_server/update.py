from typing import Union
import math_server.model as m
from dataclasses import replace
from datetime import datetime

Message = Union[
    m.Msg, 
    m.NewQuestionRequested,
    m.NewQuestionGenerated,
    m.AnswerSubmitted,
    m.AnswerChecked,
]

# update just updates the model's state
def update(model: m.MathState, message: Message) -> tuple[m.MathState, m.Cmd]:
    match message:
        case m.Msg.QUIT:
            return replace(model, state = m.AppStatus.IDLE, is_running = False), m.Cmd.NONE

        case m.Msg.WRITE_SAFE:
            return replace(model, state = m.AppStatus.IDLE, write_safe = True), m.Cmd.NONE

        case m.NewQuestionRequested(q_type, q_module):
            fresh_math = m.MathState(question_type = q_type, question_module = q_module)
            return (
                replace(model, 
                    state = m.AppStatus.GENERATING_QUESTION,
                    question_type = q_type,
                    question_module = q_module),
                m.Cmd.GENERATE_QUESTION
            )

        case m.NewQuestionGenerated(q, a):
            return (
                replace(model, 
                    state = m.AppStatus.GENERATED_QUESTION,
                    question = q, 
                    answer = a), 
                m.Cmd.NONE
            )

        case m.AnswerSubmitted(u_answer, end_time):
            return (
                replace(model, 
                    state = m.AppStatus.ANSWER_SUBMITTED,
                    user_answer = u_answer,
                    end_time = end_time),
                m.Cmd.CHECK_ANSWER
            )

        case m.AnswerChecked(is_correct):
            return (
                replace(model, 
                    state = m.AppStatus.ANSWER_CHECKED,
                    is_answer_correct = is_correct), 
                m.Cmd.WRITE
            )

        case _:
            return model, m.Cmd.NONE
