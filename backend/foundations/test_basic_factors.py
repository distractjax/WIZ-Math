import backend.foundations.basic_factors as bf
import pytest

class TestFactorQuiz:
    standard_data = [
        # Checking core functionality with some easy numbers
        (36, 1, 2, ('What is the largest even factor of 36?\n','18')),
        (36, 1, 1, ('What is the largest odd factor of 36?\n','9')),
        (36, 2, 2, ('What is the smallest even factor of 36 that is not 2?\n','4')),
        (36, 2, 1, ('What is the smallest odd factor of 36 that is not 1?\n','3')),
        (36, 3, 2, ('How many even factors of 36 are there?\n','6')),
        (36, 3, 1, ('How many odd factors of 36 are there?\n','3')),
    ]
    exception_data = [
        # Checking the bounds on num1
        (201, 1, 2),
        (3, 1, 2),
        # Checking the bounds on question_num
        (36, 4, 2),
        (36, -1, 2),
        # Checking the bounds on is_even
        (36, 1, 3),
        (36, 1, -1),
    ]
    power_of_two_data = [
        # Checking to make sure that the special case for 4 is working.
        (4, 1, 2, ('What is the largest even factor of 4?\n', '2')),
        (4, 1, 1, ('What is the largest even factor of 4?\n', '2')),
        (4, 1, 0, ('What is the largest even factor of 4?\n', '2')),
        (4, 2, 2, ('What is the smallest even factor of 4?\n', '2')),
        (4, 2, 1, ('What is the smallest even factor of 4?\n', '2')),
        (4, 2, 0, ('What is the smallest even factor of 4?\n', '2')),
        # Checking to make sure that other powers of 2 don't cause issues.
        (16, 1, 2, ('What is the largest even factor of 16?\n', '8')),
        (16, 1, 1, ('What is the largest even factor of 16?\n', '8')),
        (16, 1, 0, ('What is the largest even factor of 16?\n', '8')),
        (16, 2, 2, ('What is the smallest even factor of 16 that is not 2?\n', '4')),
        (16, 2, 1, ('What is the smallest even factor of 16 that is not 2?\n', '4')),
        (16, 2, 0, ('What is the smallest even factor of 16 that is not 2?\n', '4')),
    ]
    power_of_three_data = [
        # Checking to make sure that powers of 3 don't cause any problems.
        (9, 1, 2, ('What is the largest odd factor of 9?\n', '3')),
        (9, 1, 1, ('What is the largest odd factor of 9?\n', '3')),
        (9, 1, 0, ('What is the largest odd factor of 9?\n', '3')),
        (9, 2, 2, ('What is the smallest odd factor of 9 that is not 1?\n', '3')),
        (9, 2, 1, ('What is the smallest odd factor of 9 that is not 1?\n', '3')),
        (9, 2, 0, ('What is the smallest odd factor of 9 that is not 1?\n', '3')),
        (27, 1, 2, ('What is the largest odd factor of 27?\n', '9')),
        (27, 1, 1, ('What is the largest odd factor of 27?\n', '9')),
        (27, 1, 0, ('What is the largest odd factor of 27?\n', '9')),
        (27, 2, 2, ('What is the smallest odd factor of 27 that is not 1?\n', '3')),
        (27, 2, 1, ('What is the smallest odd factor of 27 that is not 1?\n', '3')),
        (27, 2, 0, ('What is the smallest odd factor of 27 that is not 1?\n', '3')),
    ]
    prime_number_recursion_data = [
        # Checking to make sure that recursion activates properly when num1 is a prime number.
        (83, 1, 2, ('What is the largest even factor of 84?\n', '42')),
        (83, 1, 1, ('What is the largest odd factor of 84?\n', '21')),
        (83, 2, 2, ('What is the smallest even factor of 84 that is not 2?\n', '4')),
        (83, 2, 1, ('What is the smallest odd factor of 84 that is not 1?\n', '3')),
        (83, 3, 2, ('How many even factors of 84 are there?\n','8')),
        (83, 3, 1, ('How many odd factors of 84 are there?\n','4')),
    ]

    @pytest.mark.parametrize("num,question,even,answer", standard_data)
    def test_standard_data(self, num, question, even, answer):
        factors = bf.factor_quiz(num1 = num, question_num = question, is_even = even)
        assert factors == answer

    @pytest.mark.parametrize("num,question,even,answer", power_of_two_data)
    def test_powers_of_two(self, num, question, even, answer):
        factors = bf.factor_quiz(num1 = num, question_num = question, is_even = even)
        assert factors[0] == answer[0] and factors[1] == answer[1]

    @pytest.mark.parametrize("num,question,even,answer", power_of_three_data)
    def test_powers_of_three(self, num, question, even, answer):
        factors = bf.factor_quiz(num1 = num, question_num = question, is_even = even)
        assert factors[0] == answer[0] and factors[1] == answer[1]

    @pytest.mark.parametrize("num,question,even,answer", prime_number_recursion_data)
    def test_prime_number_recursion(self, num, question, even, answer):
        factors = bf.factor_quiz(num1 = num, question_num = question, is_even = even)
        assert factors == answer
        
    @pytest.mark.parametrize("num,question,even", exception_data)
    def test_exceptions(self, num, question, even):
        with pytest.raises(ValueError):
            bf.factor_quiz(num1 = num, question_num = question, is_even = even)

class TestPrimeFactorQuiz:
    # Prime Factor Quiz Dataset
    prime_standard_data = [
        # Checking core functionality with some easy numbers
        (126, 1, ('What is the largest prime factor of 126?\n','7')),
        (126, 2, ('What is the smallest prime factor of 126 that is not 1 or 2?\n','3')),
        (126, 3, ('How many prime factors of 126 are there?\n','4')),
    ]
    prime_exception_data = [
        # Checking the bounds on num1
        (201, 1),
        (3, 1),
        # Checking the bounds on question_num
        (36, 4),
        (36, -1),
    ]
    prime_power_of_two_data = [
        # Checking to make sure that the powers of two conditional works properly.
        (4, 1, ('What is the largest prime factor of 4?\n', '2')),
        (4, 2, ('What is the smallest prime factor of 4?\n', '1')),
        (16, 1, ('What is the largest prime factor of 16?\n', '2')),
        (16, 2, ('What is the smallest prime factor of 16?\n', '1')),
    ]
    prime_power_of_three_data = [
        # Checking to make sure that other exponents work properly.
        (9, 1, ('What is the largest prime factor of 9?\n', '3')),
        (9, 2, ('What is the smallest prime factor of 9 that is not 1 or 2?\n', '3')),
        (27, 1, ('What is the largest prime factor of 27?\n', '3')),
        (27, 2, ('What is the smallest prime factor of 27 that is not 1 or 2?\n', '3')),
    ]
    prime_test_recursion_data = [
        # Checking to make sure that recursion activates if num1 is a prime number.
        (83, 1, ('What is the largest prime factor of 84?\n', '7')),
        (83, 2, ('What is the smallest prime factor of 84 that is not 1 or 2?\n', '3')),
        (83, 3, ('How many prime factors of 84 are there?\n','4')),
    ]

    @pytest.mark.parametrize("num,question,answer", prime_standard_data)
    def test_standard_data(self, num, question, answer):
        factors = bf.prime_factor_quiz(num1 = num, question_num = question)
        assert factors == answer

    @pytest.mark.parametrize("num,question,answer", prime_power_of_two_data)
    def test_powers_of_two(self, num, question, answer):
        factors = bf.prime_factor_quiz(num1 = num, question_num = question)
        assert factors[0] == answer[0] and factors[1] == answer[1]

    @pytest.mark.parametrize("num,question,answer", prime_power_of_three_data)
    def test_powers_of_three(self, num, question, answer):
        factors = bf.prime_factor_quiz(num1 = num, question_num = question)
        assert factors[0] == answer[0] and factors[1] == answer[1]

    @pytest.mark.parametrize("num,question,answer", prime_test_recursion_data)
    def test_prime_number_recursion(self, num, question, answer):
        factors = bf.prime_factor_quiz(num1 = num, question_num = question)
        assert factors == answer
        
    @pytest.mark.parametrize("num,question", prime_exception_data)
    def test_exceptions(self, num, question):
        with pytest.raises(ValueError):
            bf.prime_factor_quiz(num1 = num, question_num = question)
