import math_server.foundations.digit_reversals as dr
import pytest

# Test Digit Reversals
class TestDigitReversalsQuiz:
    # Data
    standard_data = [
        # Testing the questions and calculations for easy numbers.
        (1, 9, ('When the digits of a number are inverted and added to itself, the result is 1991. What is the smallest possible value of that number?', '1090')),
        (6, 6, ('When the digits of a number are inverted and added to itself, the result is 6666. What is the smallest possible value of that number?', '1065')),
    ]
    exception_data = [
        # num1 Exceptions
        (10, 4),
        (-1, 4),
        # num2 Exceptions
        (4, 10),
        (4, -1),
    ]

    @pytest.mark.parametrize("num1,num2,answer", standard_data)
    def test_standard_data(self, num1, num2, answer):
        reversal = dr.int_reversal_quiz(num1 = num1, num2 = num2)
        assert reversal == answer

