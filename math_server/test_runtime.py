from math_server import model as m, runtime as r
from datetime import datetime
from dataclasses import replace
import pytest

class TestHandleCommand:
    initial_state = m.MathState()
    
    def test_generate_question(self):
        question_type = "Foundations"
        question_module = "multiply by fractions"
        test_state = replace(self.initial_state, 
            question_type = "Foundations",
            question_module = "multiply by fractions"
        )
        cmd = m.Cmd.GENERATE_QUESTION
        new_state, new_cmd = r.handle_command(test_state, cmd)
        assert new_state.state == m.AppStatus.GENERATED_QUESTION
        assert new_state.question != ""
        assert new_state.answer != ""
        assert new_cmd == m.Cmd.NONE

    def test_check_answer(self):
        test_state = replace(self.initial_state,
            answer = "2",
            user_answer = "2"
        )
        cmd = m.Cmd.CHECK_ANSWER
        new_state, new_cmd = r.handle_command(test_state, cmd)
        assert new_state.state == m.AppStatus.ANSWER_CHECKED
        assert new_state.is_answer_correct
        assert new_cmd == m.Cmd.WRITE

    def test_write(self):
        test_state = replace(self.initial_state,
            write_safe = True
        )
        cmd = m.Cmd.WRITE
        new_state, new_cmd = r.handle_command(test_state, cmd)
        assert new_state.state == m.AppStatus.IDLE
        assert new_cmd == m.Cmd.NONE
