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

class TestFormattingMultiplicationQuiz:
    # Data
    standard_data = [
        # Example from the book
        (7, 3, 2, 2, 3, ('What is the value of \u221A63 x \u221B56 x 7^1/6', '42')),
    ]
    exception_data = [
        # base Exceptions
        (10, 4, 4, 4, 4),
        (1, 4, 4, 4, 4),
        # num1 Exceptions
        (4, 10, 4, 4, 4),
        (4, 1, 4, 4, 4),
        # num2 Exceptions
        (4, 4, 10, 4, 4),
        (4, 4, 1, 4, 4),
        # num1_exp Exceptions
        (4, 4, 4, 5, 4),
        (4, 4, 4, 1, 4),
        # num2_exp Exceptions
        (4, 4, 4, 4, 5),
        (4, 4, 4, 4, 1),
    ]
    recursion_data = [
        # Standard test
        (7, 3, 2, 2, 2, ('What is the value of \u221B189 x \u221A28 x 7^1/6', '42')),
        # Boundary case
        (7, 3, 2, 4, 4, ('What is the value of \u221B189 x \u221C112 x 7^5/12', '42')),
    ]

    @pytest.mark.parametrize("base,num1,num2,num1_exp,num2_exp,answer", standard_data)
    def test_standard_data(self, base, num1, num2, num1_exp, num2_exp, answer):
        product = bfe.root_formatting_multiplication_quiz(
            base = base,
            num1 = num1,
            num2 = num2,
            num1_exp = num1_exp,
            num2_exp = num2_exp
        )
        assert product == answer

    @pytest.mark.parametrize("base,num1,num2,num1_exp,num2_exp,answer", recursion_data)
    def test_recursion_data(self, base, num1, num2, num1_exp, num2_exp, answer):
        product = bfe.root_formatting_multiplication_quiz(
            base = base,
            num1 = num1,
            num2 = num2,
            num1_exp = num1_exp,
            num2_exp = num2_exp
        )
        assert product == answer

    @pytest.mark.parametrize("base,num1,num2,num1_exp,num2_exp", exception_data)
    def test_exception_data(self, base, num1, num2, num1_exp, num2_exp):
        with pytest.raises(ValueError):
            bfe.root_formatting_multiplication_quiz(
                base = base,
                num1 = num1,
                num2 = num2,
                num1_exp = num1_exp,
                num2_exp = num2_exp
            )
