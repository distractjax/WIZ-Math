import math_server.foundations.basic_fractional_exponents as bfe
import pytest

# Test Cross Multiplication
class TestCrossMultiplicationQuiz:
    # Data
    standard_data = [
        # Testing the num1 and num2 behavior
        (4, 2, 3, ('What is the value of (\u221A2 + 2\u221A8)(3\u221A2 - \u221A8)?', '10')),
        # Example from the book
        (9, 3, 2, ('What is the value of (\u221A3 + 3\u221A27)(2\u221A3 - \u221A27)?', '-30')),
    ]
    exception_data = [
        # base Exceptions
        (10, 4, 4),
        (1, 4, 4),
        # num1 Exceptions
        (4, 10, 4),
        (4, 1, 4),
        # num2 Exceptions
        (4, 4, 10),
        (4, 4, 1),
    ]

    @pytest.mark.parametrize("base,num1,num2,answer", standard_data)
    def test_standard_data(self, base, num1, num2, answer):
        product = bfe.root_cross_multiplication_quiz(base = base, num1 = num1, num2 = num2)
        assert product == answer

    @pytest.mark.parametrize("base,num1,num2", exception_data)
    def test_exception_data(self, base, num1, num2):
        with pytest.raises(ValueError):
            bfe.root_cross_multiplication_quiz(base = base, num1 = num1, num2 = num2)
