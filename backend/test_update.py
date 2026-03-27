from backend import model as m, update as u
from datetime import datetime
import pytest

class TestUpdate:
    initial_state = m.GlobalState(problem_history = None)
    def test_quit(self):
        msg = m.Msg.QUIT
        new_state, cmd = u.update(self.initial_state, msg)

        assert not new_state.is_running
        assert cmd == m.Cmd.NONE

    def test_stats_requested_flow(self):
        msg = m.StatsRequested(view_type = "overview")
        new_state, cmd = u.update(self.initial_state, msg)

        assert new_state.state == m.AppStatus.STATS_REQUESTED
        assert new_state.view_type == "overview"
        assert cmd == m.Cmd.PULL_STATS

    def test_stats_loaded_flow(self):
        problem_history = {
            "Foundations": {
                "Math": {
                    "correct": 1,
                    "incorrect": 2,
                },
            },
        }
        msg = m.StatsLoaded(history = problem_history)
        new_state, cmd = u.update(self.initial_state, msg)

        assert new_state.state == m.AppStatus.STATS_PULLED
        assert new_state.problem_history == problem_history
        assert cmd == m.Cmd.NONE

    def test_query_flow(self):
        payload = {
           "Foundations": {
               "Math": {
                   "correct": 1,
                   "incorrect": 2,
               },
           },
        }
        msg = m.QueriedSubstate(payload=payload, message="Hello")
        new_state, cmd = u.update(self.initial_state, msg)

        assert new_state.state == m.AppStatus.FETCHING_DATA
        assert new_state.payload == payload
        assert new_state.message == "Hello"
        assert cmd == m.Cmd.QUERY_SUBSTATE

    def test_write_flow(self):
        msg = m.Msg.WRITE_DB
        new_state, cmd = u.update(self.initial_state, msg)

        assert new_state.state == m.AppStatus.WRITING_DB
        assert cmd == m.Cmd.SAVE_TO_DB
