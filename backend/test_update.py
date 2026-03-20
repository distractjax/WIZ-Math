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

    def test_new_question_flow(self):
        msg = m.NewQuestionRequested(question_type = "Foundations", question_module = "multiply by fractions")
        new_state, cmd = u.update(self.initial_state, msg)

        assert new_state.state == m.AppStatus.GENERATING_QUESTION
        assert new_state.math.question_type == msg.question_type
        assert new_state.math.question_module == msg.question_module
        assert cmd == m.Cmd.GENERATE_QUESTION

    def test_generated_question_flow(self):
        msg = m.NewQuestionGenerated(question = "1+1", answer = "2")
        new_state, cmd = u.update(self.initial_state, msg)

        assert new_state.state == m.AppStatus.GENERATED_QUESTION
        assert new_state.math.question == msg.question
        assert new_state.math.question == msg.question
        assert cmd == m.Cmd.SAVE_Q_TO_DB

    def test_answer_submitted_flow(self):
        end_time = datetime.now()
        msg = m.AnswerSubmitted(user_answer = "2", end_time = end_time)

        new_state, cmd = u.update(self.initial_state, msg)

        assert new_state.state == m.AppStatus.ANSWER_SUBMITTED
        assert new_state.math.user_answer == "2"
        assert new_state.math.end_time == end_time
        assert cmd == m.Cmd.CHECK_ANSWER

    @pytest.mark.parametrize("is_correct",[True,False])
    def test_answer_checked_flow(self,is_correct):
        msg = m.AnswerChecked(is_correct)
        new_state, cmd = u.update(self.initial_state, msg)
        assert new_state.state == m.AppStatus.ANSWER_CHECKED
        assert new_state.math.is_answer_correct == is_correct
        assert cmd == m.Cmd.SAVE_A_TO_DB

    def test_stats_requested_flow(self):
        msg = m.StatsRequested("test")
        new_state, cmd = u.update(self.initial_state, msg)
        assert new_state.state == m.AppStatus.STATS_REQUESTED
        assert new_state.view_type == "test"
        assert cmd == m.Cmd.PULL_STATS

    def test_stats_loaded_flow(self):
        test_stats = {
            "One": 1,
            "Two": 2,
            "Three": 3,
        }
        msg = m.StatsLoaded(test_stats)
        new_state, cmd = u.update(self.initial_state, msg)
        assert new_state.state == m.AppStatus.STATS_PULLED
        assert new_state.problem_history["One"] == 1
        assert new_state.problem_history["Two"] == 2
        assert new_state.problem_history["Three"] == 3
        assert cmd == m.Cmd.NONE
