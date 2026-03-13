import backend.foundations.basic_factors as bf
import pytest
import datetime
import config
import sqlite3

testdata = [
    (36, 1, 2, ('What is the largest even factor of 36?\n','18','Factor Operations', 'Foundations')),
    (36, 1, 1, ('What is the largest odd factor of 36?\n','9','Factor Operations', 'Foundations')),
    (36, 2, 2, ('What is the smallest even factor of 36 that is not 2?\n','4','Factor Operations', 'Foundations')),
    (36, 2, 1, ('What is the smallest odd factor of 36 that is not 1?\n','3','Factor Operations', 'Foundations')),
    (36, 3, 2, ('How many even factors of 36 are there?\n','5','Factor Operations', 'Foundations')),
    (36, 3, 1, ('How many odd factors of 36 are there?\n','3','Factor Operations', 'Foundations')),
]

exception_data = [
    (36, 4, 2),
    (36, -1, 2),
    (3, 1, 2),
    (201, 1, 2),
    (201, 1, 3),
    (201, 1, -1),
]

class TestBasicFactors:

    def setup_method(self):
        self.test_start_time = datetime.datetime.now()

    def teardown_method(self):
        with sqlite3.connect(config.SQLITE_PATH) as conn:
            c = conn.cursor()
            c.execute("DELETE FROM problem_history WHERE exec_time > ?", (self.test_start_time,))
            conn.commit()

    @pytest.mark.parametrize("num,question,even,answer", testdata)
    def test_factor_quiz(self, num, question, even, answer):
        factors = bf.factor_quiz(num1 = num, question_num = question, is_even = even)
        assert factors == answer

    @pytest.mark.parametrize("num,question,even", exception_data)
    def test_factor_quiz_exceptions(self, num, question, even):
        with pytest.raises(ValueError):
            bf.factor_quiz(num1 = num, question_num = question, is_even = even)
