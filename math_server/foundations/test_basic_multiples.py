import math_server.foundations.basic_multiples as bm
import pytest

# Common N-Digit Multiples Data

class TestCommonNDigitMultipleQuiz:
    # Data
    standard_data = [
        # Testing the questions and calculations for easy numbers.
        (5, 7, 2, 1, ('What is the largest 2-digit multiple of 5 that is also a multiple of 7?\n', '70')),
        (5, 7, 2, 2, ('What is the smallest 2-digit multiple of 5 that is also a multiple of 7?\n', '35')),
        (5, 7, 2, 3, ('How many 2-digit multiples of 5 are also multiples of 7?\n', '2')),
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
    # Test if the least common multiple of num1 and num2 is greater than the n-digit boundary.
    n_digit_bound_data = [
        (19, 18, 2, 1, ('What is the largest 3-digit multiple of 19 that is also a multiple of 18?\n', '684')),
        (19, 18, 2, 2, ('What is the smallest 3-digit multiple of 19 that is also a multiple of 18?\n', '342')),
        (19, 18, 2, 3, ('How many 3-digit multiples of 19 are also multiples of 18?\n', '2')),
    ]
    # Test if num2 is a factor of num1 and vice versa.
    factors_data = [
        (10, 5, 2, 1, ('What is the largest 2-digit multiple of 9 that is also a multiple of 5?\n', '90')),
        (10, 5, 2, 2, ('What is the smallest 2-digit multiple of 9 that is also a multiple of 5?\n', '45')),
        (10, 5, 2, 3, ('How many 2-digit multiples of 9 are also multiples of 5?\n', '2')),
        (5, 10, 2, 1, ('What is the largest 2-digit multiple of 4 that is also a multiple of 10?\n', '80')),
        (5, 10, 2, 2, ('What is the smallest 2-digit multiple of 4 that is also a multiple of 10?\n', '20')),
        (5, 10, 2, 3, ('How many 2-digit multiples of 4 are also multiples of 10?\n', '4')),
        (5, 5, 2, 1, ('What is the largest 2-digit multiple of 4 that is also a multiple of 5?\n', '80')),
        (5, 5, 2, 2, ('What is the smallest 2-digit multiple of 4 that is also a multiple of 5?\n', '20')),
        (5, 5, 2, 3, ('How many 2-digit multiples of 4 are also multiples of 5?\n', '4')),
        (20, 5, 2, 1, ('What is the largest 2-digit multiple of 19 that is also a multiple of 5?\n', '95')),
        (20, 5, 2, 2, ('What is the smallest 2-digit multiple of 19 that is also a multiple of 5?\n', '95')),
        (20, 5, 2, 3, ('How many 2-digit multiples of 19 are also multiples of 5?\n', '1')),
        (5, 20, 2, 1, ('What is the largest 2-digit multiple of 3 that is also a multiple of 20?\n', '60')),
        (5, 20, 2, 2, ('What is the smallest 2-digit multiple of 3 that is also a multiple of 20?\n', '60')),
        (5, 20, 2, 3, ('How many 2-digit multiples of 3 are also multiples of 20?\n', '1')),
    ]
    # Test if num1 is 2 and num1 is even.
    two_and_even_data = [
        (2, 20, 2, 1, ('What is the largest 2-digit multiple of 3 that is also a multiple of 20?\n', '60')),
        (2, 20, 2, 2, ('What is the smallest 2-digit multiple of 3 that is also a multiple of 20?\n', '60')),
        (2, 20, 2, 3, ('How many 2-digit multiples of 3 are also multiples of 20?\n', '1')),
    ]

    @pytest.mark.parametrize("num1,num2,n_digits,question,answer", standard_data)
    def test_standard_data(self, num1, num2, n_digits, question, answer):
        multiples = bm.common_n_digit_multiples_quiz(num1 = num1, num2 = num2, n_digits= n_digits,question_num=question)
        assert multiples == answer

    @pytest.mark.parametrize("num1,num2,n_digits,question,answer", n_digit_bound_data)
    def test_n_digit_bound(self, num1, num2, n_digits, question, answer):
        multiples = bm.common_n_digit_multiples_quiz(num1 = num1, num2 = num2, n_digits= n_digits,question_num=question)
        assert multiples == answer

    @pytest.mark.parametrize("num1,num2,n_digits,question,answer", factors_data)
    def test_mutual_factors(self, num1, num2, n_digits, question, answer):
        multiples = bm.common_n_digit_multiples_quiz(num1 = num1, num2 = num2, n_digits= n_digits,question_num=question)
        assert multiples == answer

    @pytest.mark.parametrize("num1,num2,n_digits,question,answer", two_and_even_data)
    def test_two_and_even(self, num1, num2, n_digits, question, answer):
        multiples = bm.common_n_digit_multiples_quiz(num1 = num1, num2 = num2, n_digits= n_digits,question_num=question)
        assert multiples == answer

    @pytest.mark.parametrize("num1,num2,n_digits,question", exception_data)
    def test_exceptions(self, num1, num2, n_digits, question):
        with pytest.raises(ValueError):
            bm.common_n_digit_multiples_quiz(num1 = num1, num2 = num2, n_digits= n_digits,question_num=question)

class TestNDigitMultipleQuiz:
    # Data
    standard_data = [
        # Testing the questions and calculations for easy numbers.
        (5, 2, 1, ('What is the largest 2-digit multiple of 5?\n', '95')),
        (5, 2, 2, ('What is the smallest 2-digit multiple of 5?\n', '10')),
        (5, 2, 3, ('How many 2-digit multiples are there of 5?\n', '18')),
        (5, 3, 1, ('What is the largest 3-digit multiple of 5?\n', '995')),
        (5, 3, 2, ('What is the smallest 3-digit multiple of 5?\n', '100')),
        (5, 3, 3, ('How many 3-digit multiples are there of 5?\n', '180')),
    ]
    exception_data = [
        # num1 Exceptions
        (26, 2, 1),
        (1, 2, 1),
        # n_digits Exceptions
        (10, 5, 1),
        (10, 1, 1),
        # question_num Exceptions
        (10, 2, -1),
        (10, 2, 4),
    ]

    @pytest.mark.parametrize("num1,n_digits,question,answer", standard_data)
    def test_standard_data(self, num1, n_digits, question, answer):
        multiples = bm.n_digit_multiples_quiz(num = num1, n_digits= n_digits,question_num=question)
        assert multiples == answer

    @pytest.mark.parametrize("num1,n_digits,question", exception_data)
    def test_exceptions(self, num1, n_digits, question):
        with pytest.raises(ValueError):
            bm.n_digit_multiples_quiz(num = num1, n_digits= n_digits,question_num=question)
