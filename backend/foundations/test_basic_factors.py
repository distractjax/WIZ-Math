import backend.foundations.basic_factors as bf
import pytest
import datetime
import config
import sqlite3

# Factor Quiz Dataset
standard_data = [
    (36, 1, 2, ('What is the largest even factor of 36?\n','18','Factor Operations', 'Foundations')),
    (36, 1, 1, ('What is the largest odd factor of 36?\n','9','Factor Operations', 'Foundations')),
    (36, 2, 2, ('What is the smallest even factor of 36 that is not 2?\n','4','Factor Operations', 'Foundations')),
    (36, 2, 1, ('What is the smallest odd factor of 36 that is not 1?\n','3','Factor Operations', 'Foundations')),
    (36, 3, 2, ('How many even factors of 36 are there?\n','6','Factor Operations', 'Foundations')),
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
power_of_two_data = [
    (4, 1, 2, ('What is the largest even factor of 4?\n', '2')),
    (4, 1, 1, ('What is the largest even factor of 4?\n', '2')),
    (4, 1, 0, ('What is the largest even factor of 4?\n', '2')),
    (4, 2, 2, ('What is the smallest even factor of 4?\n', '2')),
    (4, 2, 1, ('What is the smallest even factor of 4?\n', '2')),
    (4, 2, 0, ('What is the smallest even factor of 4?\n', '2')),
    (16, 1, 2, ('What is the largest even factor of 16?\n', '8')),
    (16, 1, 1, ('What is the largest even factor of 16?\n', '8')),
    (16, 1, 0, ('What is the largest even factor of 16?\n', '8')),
    (16, 2, 2, ('What is the smallest even factor of 16 that is not 2?\n', '4')),
    (16, 2, 1, ('What is the smallest even factor of 16 that is not 2?\n', '4')),
    (16, 2, 0, ('What is the smallest even factor of 16 that is not 2?\n', '4')),
]
power_of_three_data = [
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
    (83, 1, 2, ('What is the largest even factor of 84?\n', '42', 'Factor Operations', 'Foundations')),
    (83, 1, 1, ('What is the largest odd factor of 84?\n', '21', 'Factor Operations', 'Foundations')),
    (83, 2, 2, ('What is the smallest even factor of 84 that is not 2?\n', '4', 'Factor Operations', 'Foundations')),
    (83, 2, 1, ('What is the smallest odd factor of 84 that is not 1?\n', '3', 'Factor Operations', 'Foundations')),
    (83, 3, 2, ('How many even factors of 84 are there?\n','8','Factor Operations', 'Foundations')),
    (83, 3, 1, ('How many odd factors of 84 are there?\n','4','Factor Operations', 'Foundations')),
]

class TestFactorQuiz:
    def setup_method(self):
        self.test_start_time = datetime.datetime.now()

    def teardown_method(self):
        with sqlite3.connect(config.SQLITE_PATH) as conn:
            c = conn.cursor()
            c.execute("DELETE FROM problem_history WHERE exec_time > ?", (self.test_start_time,))
            conn.commit()

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

# Prime Factor Quiz Dataset
prime_standard_data = [
    (126, 1, ('What is the largest prime factor of 126?\n','7','Prime Factor Operations', 'Foundations')),
    (126, 2, ('What is the smallest prime factor of 126 that is not 1 or 2?\n','3','Prime Factor Operations', 'Foundations')),
    (126, 3, ('How many prime factors of 126 are there?\n','4','Prime Factor Operations', 'Foundations')),
]
prime_exception_data = [
    (36, 4),
    (36, -1),
    (3, 1),
    (201, 1),
]
prime_power_of_two_data = [
    (4, 1, ('What is the largest prime factor of 4?\n', '2')),
    (4, 2, ('What is the smallest prime factor of 4 that is not 1 or 2?\n', '2')),
    (16, 1, ('What is the largest prime factor of 16?\n', '8')),
    (16, 2, ('What is the smallest prime factor of 16 that is not 1 or 2?\n', '4')),
]
prime_power_of_three_data = [
    (9, 1, ('What is the largest prime factor of 9?\n', '3')),
    (9, 2, ('What is the smallest prime factor of 9 that is not 1?\n', '3')),
    (27, 1, ('What is the largest prime factor of 27?\n', '3')),
    (27, 2, ('What is the smallest prime factor of 27 that is not 1?\n', '3')),
]
prime_test_recursion_data = [
    (83, 1, ('What is the largest prime factor of 84?\n', '7', 'Prime Factor Operations', 'Foundations')),
    (83, 2, ('What is the smallest prime factor of 84 that is not 2?\n', '3', 'Prime Factor Operations', 'Foundations')),
    (83, 3, ('How many prime factors of 84 are there?\n','4','Prime Factor Operations', 'Foundations')),
]

class TestPrimeFactorQuiz:
    def setup_method(self):
        self.test_start_time = datetime.datetime.now()

    def teardown_method(self):
        with sqlite3.connect(config.SQLITE_PATH) as conn:
            c = conn.cursor()
            c.execute("DELETE FROM problem_history WHERE exec_time > ?", (self.test_start_time,))
            conn.commit()

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
