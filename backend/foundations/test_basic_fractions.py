import backend.foundations.basic_fractions as bf
import pytest
import datetime
import config
import sqlite3
from backend.core_math import find_factors
from itertools import product

# Test Divide Fractions
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
    equality_data = [
        # Num1 == Num2
        (5, 5, 13, 16, ('What is the result of (6/13) / (5/16)?\n', '96/65',
                      'Divide by Fractions', 'Foundations')),
        (20, 20, 13, 16, ('What is the result of (19/13) / (20/16)?\n', '76/65',
                      'Divide by Fractions', 'Foundations')),
        # Num1 == Den1
        (5, 6, 5, 20, ('What is the result of (7/5) / (6/20)?\n', '14/3',
                      'Divide by Fractions', 'Foundations')),
        (20, 7, 20, 16, ('What is the result of (19/20) / (7/16)?\n', '76/35',
                      'Divide by Fractions', 'Foundations')),
        # Num2 == Den2
        (5, 6, 15, 6, ('What is the result of (5/15) / (6/7)?\n', '7/18',
                      'Divide by Fractions', 'Foundations')),
        (5, 20, 13, 20, ('What is the result of (5/13) / (20/19)?\n', '19/52',
                      'Divide by Fractions', 'Foundations')),
        # Den1 == Den2
        (5, 6, 15, 15, ('What is the result of (5/15) / (6/16)?\n', '8/9',
                      'Divide by Fractions', 'Foundations')),
        (5, 7, 20, 20, ('What is the result of (5/20) / (7/19)?\n', '19/28',
                      'Divide by Fractions', 'Foundations')),
    ]

    @pytest.mark.parametrize("num1,num2,den1,den2,answer", standard_data)
    def test_standard_data(self, num1, num2, den1, den2, answer):
        fraction = bf.divide_fractions_quiz(numerator1 = num1, numerator2 = num2, denominator1 = den1, denominator2 = den2)
        assert fraction == answer

    @pytest.mark.parametrize("num1,num2,den1,den2", exception_data)
    def test_exceptions(self, num1, num2, den1, den2):
        with pytest.raises(ValueError):
            bf.divide_fractions_quiz(numerator1 = num1, numerator2 = num2, denominator1 = den1 ,denominator2 = den2)

    @pytest.mark.parametrize("num1,num2,den1,den2,answer", equality_data)
    def test_equality(self, num1, num2, den1, den2, answer):
        fraction = bf.divide_fractions_quiz(numerator1 = num1, numerator2 = num2, denominator1 = den1, denominator2 = den2)
        assert fraction == answer

class TestMultiplyFractionsQuiz:
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
        (5, 7, 13, 16, ('What is the result of (5/13) * (7/16)?\n', '35/208',
                      'Multiply by Fractions', 'Foundations')),
        (5, 6, 15, 20, ('What is the result of (5/15) * (6/20)?\n', '1/10',
                      'Multiply by Fractions', 'Foundations')),
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
    equality_data = [
        # Num1 == Den1
        (5, 6, 5, 20, ('What is the result of (6/5) * (6/20)?\n', '9/25',
                       'Multiply by Fractions', 'Foundations')),
        (20, 7, 20, 16, ('What is the result of (19/20) * (7/16)?\n', '133/320',
                         'Multiply by Fractions', 'Foundations')),
        # Num1 == Den2
        (5, 16, 13, 5, ('What is the result of (6/13) * (16/5)?\n', '96/65',
                        'Multiply by Fractions', 'Foundations')),
        (20, 16, 13, 20, ('What is the result of (19/13) * (16/20)?\n', '76/65',
                          'Multiply by Fractions', 'Foundations')),
        # Num2 == Den1
        (5, 10, 10, 16, ('What is the result of (5/10) * (11/16)?\n', '11/32',
                        'Multiply by Fractions', 'Foundations')),
        (5, 20, 20, 16, ('What is the result of (5/20) * (19/16)?\n', '19/64',
                        'Multiply by Fractions', 'Foundations')),
        # Num2 == Den2
        (5, 6, 15, 6, ('What is the result of (5/15) * (7/6)?\n', '7/18',
                       'Multiply by Fractions', 'Foundations')),
        (5, 20, 13, 20, ('What is the result of (5/13) * (19/20)?\n', '19/52',
                         'Multiply by Fractions', 'Foundations')),
    ]

    @pytest.mark.parametrize("num1,num2,den1,den2,answer", standard_data)
    def test_standard_data(self, num1, num2, den1, den2, answer):
        fraction = bf.multiply_fractions_quiz(numerator1 = num1, numerator2 = num2, denominator1 = den1, denominator2 = den2)
        assert fraction == answer

    @pytest.mark.parametrize("num1,num2,den1,den2", exception_data)
    def test_exceptions(self, num1, num2, den1, den2):
        with pytest.raises(ValueError):
            bf.multiply_fractions_quiz(numerator1 = num1, numerator2 = num2, denominator1 = den1 ,denominator2 = den2)

    @pytest.mark.parametrize("num1,num2,den1,den2,answer", equality_data)
    def test_equality(self, num1, num2, den1, den2, answer):
        fraction = bf.multiply_fractions_quiz(numerator1 = num1, numerator2 = num2, denominator1 = den1, denominator2 = den2)
        assert fraction == answer

# Just test your edge cases here. 
# You can test the simplify_exponents function in a config test.
class TestMultiplyFractionsExponentsQuiz:
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
        # This is working now.
        (1, 5, 3, 2, ('What is the result of (2^6) * (3^6) / (6^5)?\n', '6^1',
              'Multiply Fractions with Exponents', 'Foundations')),
        (2, 5, 3, 2, ('What is the result of (2^6) * (5^6) / (10^5)?\n', '10^1',
              'Multiply Fractions with Exponents', 'Foundations')),
        (3, 5, 3, 2, ('What is the result of (2^7) * (3^6) / (12^5)?\n', '12^1',
              'Multiply Fractions with Exponents', 'Foundations')),
        (4, 5, 3, 2, ('What is the result of (2^6) * (7^6) / (14^5)?\n', '14^1',
              'Multiply Fractions with Exponents', 'Foundations')),
    ]
    exception_data = [
        # denominator Exceptions
        (21, 4, 3, 2),
        (-1, 4, 3, 2),
        # denominator_exponent Exceptions
        (4, 10, 3, 2),
        (4, -1, 3, 2),
        # numerator_exponent Exceptions
        (4, 4, 4, 2),
        (4, 4, -1, 2),
        # square_or_cube Exceptions
        (4, 4, 3, 4),
        (4, 4, 3, 1),
    ]

    @pytest.mark.parametrize("d_ind,d_exp,n_exp,soc,answer", standard_data)
    def test_standard_data(self, d_ind, d_exp, n_exp, soc, answer):
        fraction = bf.multiply_fractions_with_exponents(denominator_index = d_ind,
                                                        denominator_exponent = d_exp,
                                                        numerator_exponent = n_exp,
                                                        square_or_cube = soc)
        assert fraction == answer

    @pytest.mark.parametrize("d_ind,d_exp,n_exp,soc", exception_data)
    def test_exceptions(self, d_ind, d_exp, n_exp, soc):
        with pytest.raises(ValueError):
            bf.multiply_fractions_with_exponents(denominator_index = d_ind,
                                                 denominator_exponent = d_exp,
                                                 numerator_exponent = n_exp,
                                                 square_or_cube = soc)

