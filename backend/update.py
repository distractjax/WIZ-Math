from typing import Union
import backend.model as m
from dataclasses import replace
from datetime import datetime

Message = Union[
    m.Msg, 
    m.StatsRequested,
    m.StatsLoaded,
    m.QueriedSubstate,
]

# The new way that the backend is going to work:
# 1. The backend receives a message from the frontend.
# 2. The backend determines if it needs to send that message to the math server (m.ForwardMessage)
# 3. The backend receives the updated state from the math server and writes it (this doesn't need to be a message)
# 4. The backend checks the status of write_safe and, if true, writes its sub state to the db. (m.Msg.WRITE_DB)

def update(model: m.GlobalState, message: Message) -> tuple[m.GlobalState, m.Cmd]:
    match message:
        case m.Msg.QUIT:
            return (
                replace (
                    model, 
                    is_running = False
                ), 
                m.Cmd.NONE
            )

        case m.Msg.WRITE_DB:
            return (
                replace (
                    model,
                    state = m.AppStatus.WRITING_DB
                ),
                m.Cmd.SAVE_TO_DB
            )

        case m.StatsRequested(view_type):
            return (
                replace (
                    model, 
                    view_type = view_type, 
                    state = m.AppStatus.STATS_REQUESTED
                ), 
                m.Cmd.PULL_STATS
            )

        case m.StatsLoaded(history):
            return (
                replace (
                    model, 
                    problem_history = history, 
                    state = m.AppStatus.STATS_PULLED
                ), 
                m.Cmd.NONE
            )

        case m.QueriedSubstate(msg, payload):
            return (
                replace (
                    model, 
                    state = m.AppStatus.FETCHING_DATA, 
                    message = msg, 
                    payload = payload
                ), 
                m.Cmd.QUERY_SUBSTATE
            )

        case _:
            return (
                model, 
                m.Cmd.NONE
            )

