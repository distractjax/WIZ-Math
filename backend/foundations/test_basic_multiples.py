import backend.foundations.basic_multiples as bm
import pytest
import datetime
import config
import sqlite3

# Common N-Digit Multiples Data

class TestNDigitMultipleQuiz:
    def setup_method(self):
        self.test_start_time = datetime.datetime.now()

    def teardown_method(self):
        with sqlite3.connect(config.SQLITE_PATH) as conn:
            c = conn.cursor()
            c.execute("DELETE FROM problem_history WHERE exec_time > ?", (self.test_start_time,))
            conn.commit()

    # Data
    standard_data = [
        # Testing the questions and calculations for easy numbers.
        (5, 7, 2, 1, ('What is the largest 2-digit multiple of 5 that is also a multiple of 7?\n', '70',
                      'Common N-Digit Multiples', 'Foundations')),
        (5, 7, 2, 2, ('What is the smallest 2-digit multiple of 5 that is also a multiple of 7?\n', '35',
                      'Common N-Digit Multiples', 'Foundations')),
        (5, 7, 2, 3, ('How many 2-digit multiples of 5 are also multiples of 7?\n', '2',
                      'Common N-Digit Multiples', 'Foundations')),
    ]
    exception_data = [
        # num1 and num2 Exceptions
        (21, 4, 2, 1),
        (4, 21, 2, 1),
        (1, 4, 2, 1),
        (4, 1, 2, 1),
        # n_digits Exceptions
        (10, 10, 5, 1),
        (10, 10, 1, 1),
        # question_num Exceptions
        (10, 10, 2, -1),
        (10, 10, 2, 4),
    ]
    n_digit_bound_data = [
        (19, 18, 2, 1, ('What is the largest 3-digit multiple of 19 that is also a multiple of 18?\n', '684',
                      'Common N-Digit Multiples', 'Foundations')),
        (19, 18, 2, 2, ('What is the smallest 3-digit multiple of 19 that is also a multiple of 18?\n', '342',
                      'Common N-Digit Multiples', 'Foundations')),
        (19, 18, 2, 3, ('How many 3-digit multiples of 19 are also multiples of 18?\n', '2',
                      'Common N-Digit Multiples', 'Foundations')),
    ]

    # Potential edge cases: numbers that may not have a common multiples within the specified range and numbers that are both primes.

    @pytest.mark.parametrize("num1,num2,n_digits,question,answer", standard_data)
    def test_standard_data(self, num1, num2, n_digits, question, answer):
        factors = bm.common_n_digit_multiples_quiz(num1 = num1, num2 = num2, n_digits= n_digits,question_num=question)
        assert factors == answer

    @pytest.mark.parametrize("num1,num2,n_digits,question,answer", n_digit_bound_data)
    def test_n_digit_bound(self, num1, num2, n_digits, question, answer):
        factors = bm.common_n_digit_multiples_quiz(num1 = num1, num2 = num2, n_digits= n_digits,question_num=question)
        assert factors == answer

    @pytest.mark.parametrize("num1,num2,n_digits,question", exception_data)
    def test_exceptions(self, num1, num2, n_digits, question):
        with pytest.raises(ValueError):
            bm.common_n_digit_multiples_quiz(num1 = num1, num2 = num2, n_digits= n_digits,question_num=question)
