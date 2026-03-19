import backend.foundations.basic_fractions as bf
import pytest

# Test Divide Fractions
class TestDivideFractionsQuiz:
    # Data
    standard_data = [
        # Testing the questions and calculations for easy numbers.
        (5, 7, 13, 16, ('What is the result of (5/13) / (7/16)?\n', '80/91')),
        (5, 6, 15, 20, ('What is the result of (5/15) / (6/20)?\n', '10/9')),
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
        (5, 5, 13, 16, ('What is the result of (6/13) / (5/16)?\n', '96/65')),
        (20, 20, 13, 16, ('What is the result of (19/13) / (20/16)?\n', '76/65')),
        # Num1 == Den1
        (5, 6, 5, 20, ('What is the result of (7/5) / (6/20)?\n', '14/3')),
        (20, 7, 20, 16, ('What is the result of (19/20) / (7/16)?\n', '76/35')),
        # Num2 == Den2
        (5, 6, 15, 6, ('What is the result of (5/15) / (6/7)?\n', '7/18')),
        (5, 20, 13, 20, ('What is the result of (5/13) / (20/19)?\n', '19/52')),
        # Den1 == Den2
        (5, 6, 15, 15, ('What is the result of (5/15) / (6/16)?\n', '8/9')),
        (5, 7, 20, 20, ('What is the result of (5/20) / (7/19)?\n', '19/28')),
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
    # Data
    standard_data = [
        # Testing the questions and calculations for easy numbers.
        (5, 7, 13, 16, ('What is the result of (5/13) * (7/16)?\n', '35/208')),
        (5, 6, 15, 20, ('What is the result of (5/15) * (6/20)?\n', '1/10')),
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
        (5, 6, 5, 20, ('What is the result of (6/5) * (6/20)?\n', '9/25')),
        (20, 7, 20, 16, ('What is the result of (19/20) * (7/16)?\n', '133/320')),
        # Num1 == Den2
        (5, 16, 13, 5, ('What is the result of (6/13) * (16/5)?\n', '96/65')),
        (20, 16, 13, 20, ('What is the result of (19/13) * (16/20)?\n', '76/65')),
        # Num2 == Den1
        (5, 10, 10, 16, ('What is the result of (5/10) * (11/16)?\n', '11/32')),
        (5, 20, 20, 16, ('What is the result of (5/20) * (19/16)?\n', '19/64')),
        # Num2 == Den2
        (5, 6, 15, 6, ('What is the result of (5/15) * (7/6)?\n', '7/18')),
        (5, 20, 13, 20, ('What is the result of (5/13) * (19/20)?\n', '19/52')),
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
class TestMultiplyFractionsExponentsQuiz:
    # Data
    standard_data = [
        # Full set of standard data tests for every possible denominator
        (1, 5, 3, 2, ('What is the result of (2^6) * (3^6) / (6^5)?\n', '6^1')),
        (2, 5, 3, 2, ('What is the result of (2^6) * (5^6) / (10^5)?\n', '10^1')),
        (3, 5, 3, 2, ('What is the result of (2^7) * (3^6) / (12^5)?\n', '12^1')),
        (4, 5, 3, 2, ('What is the result of (2^6) * (7^6) / (14^5)?\n', '14^1')),
        (5, 5, 3, 2, ('What is the result of (3^6) * (5^6) / (15^5)?\n', '15^1')),
        (6, 5, 3, 2, ('What is the result of (2^6) * (3^7) / (18^5)?\n', '18^1')),
        (7, 5, 3, 2, ('What is the result of (2^7) * (5^6) / (20^5)?\n', '20^1')),
        # Test on changed denominator_exponent
        (1, 7, 3, 2, ('What is the result of (2^6) * (3^6) / (6^7)?\n', '6^-1')),
        # Test on changed numerator_exponent
        (1, 5, 9, 2, ('What is the result of (2^18) * (3^18) / (6^5)?\n', '6^13')),
        # Test on changed square_or_cube
        (1, 5, 3, 3, ('What is the result of (2^9) * (3^9) / (6^5)?\n', '6^4')),
    ]
    exception_data = [
        # denominator Exceptions
        (8, 4, 3, 2),
        (-1, 4, 3, 2),
        # denominator_exponent Exceptions
        (4, 10, 3, 2),
        (4, -1, 3, 2),
        # numerator_exponent Exceptions
        (4, 4, 10, 2),
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

class TestMultiplyRemaindersQuiz:
    # Data
    standard_data = [
        (10, 5, 3, (
            'When integer a is divided by 3, the remainder is 1.\nWhen integer b is divided by 3, the remainder is 2.\nWhat is the remainder when a x b is divided by 3?\n', 
            '2')),
    ]
    exception_data = [
        # numerator1 Exceptions
        (21, 11, 5),
        (-1, 11, 5),
        # numerator2 Exceptions
        (11, 21, 5),
        (11, -1, 5),
        # denominator Exceptions
        (11, 12, 10),
        (11, 12, 1),
    ]
    recursion_data = [
        # Need to fix all these because I changed how recursion worked.
        # numerator1 == numerator2
        (10, 10, 3, (
            'When integer a is divided by 3, the remainder is 2.\nWhen integer b is divided by 3, the remainder is 1.\nWhat is the remainder when a x b is divided by 3?\n', 
            '2')),
        # numerator1 % divisor == 0
        (10, 9, 5, (
            'When integer a is divided by 5, the remainder is 1.\nWhen integer b is divided by 5, the remainder is 4.\nWhat is the remainder when a x b is divided by 5?\n', 
            '4')),
        # numerator2 % divisor == 0
        (9, 10, 5, (
            'When integer a is divided by 5, the remainder is 4.\nWhen integer b is divided by 5, the remainder is 1.\nWhat is the remainder when a x b is divided by 5?\n', 
            '4')),
        # numerator1 == numerator2, then recursion causes numerator1 % divisor == 0
        (9, 9, 5, (
            'When integer a is divided by 5, the remainder is 1.\nWhen integer b is divided by 5, the remainder is 4.\nWhat is the remainder when a x b is divided by 5?\n', 
            '4')),
        # numerator1 == numerator2, then recursion causes numerator1 % divisor == 0
        (19, 19, 5, (
            'When integer a is divided by 5, the remainder is 4.\nWhen integer b is divided by 5, the remainder is 4.\nWhat is the remainder when a x b is divided by 5?\n', 
            '1')),
        (19, 18, 6, (
            'When integer a is divided by 6, the remainder is 1.\nWhen integer b is divided by 6, the remainder is 1.\nWhat is the remainder when a x b is divided by 6?\n', 
            '1')),
    ]

    @pytest.mark.parametrize("n_1,n_2,d,answer", standard_data)
    def test_standard_data(self, n_1, n_2, d, answer):
        remainder = bf.multiply_remainders(
            numerator1 = n_1,
            numerator2 = n_2,
            denominator = d,
        )
        assert remainder == answer

    @pytest.mark.parametrize("n_1,n_2,d", exception_data)
    def test_exception_data(self, n_1, n_2, d):
        with pytest.raises(ValueError):
            bf.multiply_remainders(
                numerator1 = n_1,
                numerator2 = n_2,
                denominator = d,
            )

    @pytest.mark.parametrize("n_1,n_2,d,answer", recursion_data)
    def test_recursion_data(self, n_1, n_2, d, answer):
        remainder = bf.multiply_remainders(
            numerator1 = n_1,
            numerator2 = n_2,
            denominator = d,
        )
        assert remainder == answer

