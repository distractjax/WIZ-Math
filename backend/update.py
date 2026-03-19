from typing import Union
import model as m
from dataclasses import replace
import function_dicts
from datetime import datetime

Message = Union[
    m.Msg, 
    m.NewQuestionRequested,
    m.NewQuestionGenerated,
    m.AnswerSubmitted,
    m.AnswerChecked,
    m.StatsLoaded,
]

# update just updates the model's state
def update(model: m.GlobalState, message: Message) -> tuple[m.GlobalState, m.Cmd]:
    match message:
        case m.Msg.QUIT:
            return replace(model, is_running = False), m.Cmd.NONE

        case m.NewQuestionRequested(q_type, q_module):
            return replace(model, state = m.AppStatus.GENERATING_QUESTION,
                           math = replace(model.math, question_type = q_type, question_module = q_module)), m.Cmd.GENERATE_QUESTION

        case m.NewQuestionGenerated(q, a):
            return replace(model, state = m.AppStatus.GENERATED_QUESTION,
                           math = replace(model.math, question = q, answer = a)), m.Cmd.SAVE_Q_TO_DB

        case m.AnswerSubmitted(u_answer, end_time):
            return replace(model, state = m.AppStatus.ANSWER_SUBMITTED,
                           math = replace(model.math, user_answer = u_answer, end_time = end_time)), m.Cmd.CHECK_ANSWER

        case m.AnswerChecked(is_correct):
            return replace(model, state = m.AppStatus.ANSWER_CHECKED,
                           math = replace(model.math, is_answer_correct = is_correct)), m.Cmd.SAVE_A_TO_DB

        case m.Msg.STATS_REQUESTED:
            return replace(model, state = m.AppStatus.STATS_REQUESTED), m.Cmd.PULL_STATS

        case m.StatsLoaded(df): 
            return replace(model, state = m.AppStatus.STATS_PULLED, problem_history = df), m.Cmd.NONE

        case _:
            return model, m.Cmd.NONE
