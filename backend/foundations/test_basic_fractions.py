import backend.foundations.basic_fractions as bf
import pytest
import datetime
import config
import sqlite3

# Test Divide Fractions
# Some potential problems are popping up as I look at the file.
# I want to handle equal numerators and denominators with recursion, but doing that could create the following problems:
# 1. 

class TestDivideFractionsQuiz:
    def setup_method(self):
        self.test_start_time = datetime.datetime.now()

    def teardown_method(self):
        conn = sqlite3.connect(config.SQLITE_PATH)
        try:
            with conn:
                c = conn.cursor()
                c.execute("DELETE FROM problem_history WHERE exec_time > ?", (self.test_start_time,))
        finally:
            conn.close()

    # Data
    standard_data = [
        # Testing the questions and calculations for easy numbers.
        (5, 7, 13, 16, ('What is the result of (5/13) / (7/16)?\n', '80/91',
                      'Divide by Fractions', 'Foundations')),
        (5, 6, 15, 20, ('What is the result of (5/15) / (6/20)?\n', '10/9',
                      'Divide by Fractions', 'Foundations')),
    ]
    exception_data = [
        # numerator1 Exceptions
        (21, 4, 4, 4),
        (-1, 4, 4, 4),
        # numerator2 Exceptions
        (4, 21, 4, 4),
        (4, -1, 4, 4),
        # denominator1 Exceptions
        (4, 4, 21, 4),
        (4, 4, -1, 4),
        # denominator2 Exceptions
        (4, 4, 4, 21),
        (4, 4, 4, -1),
    ]

    @pytest.mark.parametrize("num1,num2,den1,den2,answer", standard_data)
    def test_standard_data(self, num1, num2, den1, den2, answer):
        fraction = bf.divide_fractions_quiz(numerator1 = num1, numerator2 = num2, denominator1 = den1, denominator2 = den2)
        assert fraction == answer

    @pytest.mark.parametrize("num1,num2,den1,den2", exception_data)
    def test_exceptions(self, num1, num2, den1, den2):
        with pytest.raises(ValueError):
            bf.divide_fractions_quiz(numerator1 = num1, numerator2 = num2, denominator1 = den1 ,denominator2 = den2)
