from math_server import model as m, update as u
from datetime import datetime
import pytest

class TestUpdate:
    initial_state = m.MathState()
    def test_quit(self):
        msg = m.Msg.QUIT
        new_state, cmd = u.update(self.initial_state, msg)

        assert not new_state.is_running
        assert cmd == m.Cmd.NONE

    def test_new_question_flow(self):
        msg = m.NewQuestionRequested(question_type = "Foundations", question_module = "multiply by fractions")
        new_state, cmd = u.update(self.initial_state, msg)

        assert new_state.state == m.AppStatus.GENERATING_QUESTION
        assert new_state.question_type == msg.question_type
        assert new_state.question_module == msg.question_module
        assert cmd == m.Cmd.GENERATE_QUESTION

    def test_generated_question_flow(self):
        msg = m.NewQuestionGenerated(question = "1+1", answer = "2")
        new_state, cmd = u.update(self.initial_state, msg)

        assert new_state.state == m.AppStatus.GENERATED_QUESTION
        assert new_state.question == msg.question
        assert new_state.question == msg.question
        assert cmd == m.Cmd.NONE

    def test_answer_submitted_flow(self):
        end_time = datetime.now()
        msg = m.AnswerSubmitted(user_answer = "2", end_time = end_time)
        new_state, cmd = u.update(self.initial_state, msg)

        assert new_state.state == m.AppStatus.ANSWER_SUBMITTED
        assert new_state.user_answer == "2"
        assert new_state.end_time == end_time
        assert cmd == m.Cmd.CHECK_ANSWER

    @pytest.mark.parametrize("is_correct",[True,False])
    def test_answer_checked_flow(self,is_correct):
        msg = m.AnswerChecked(is_correct)
        new_state, cmd = u.update(self.initial_state, msg)

        assert new_state.state == m.AppStatus.ANSWER_CHECKED
        assert new_state.is_answer_correct == is_correct
        assert cmd == m.Cmd.NONE
