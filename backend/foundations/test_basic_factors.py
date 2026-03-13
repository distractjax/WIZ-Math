import backend.foundations.basic_factors as bf
import pytest

testdata = [
    (36, 1, 2, ('What is the largest even factor of 36?\n','18','Factor Operations', 'Foundations')),
    (36, 1, 1, ('What is the largest odd factor of 36?\n','9','Factor Operations', 'Foundations')),
    (36, 2, 2, ('What is the smallest even factor of 36 that is not 2?\n','4','Factor Operations', 'Foundations')),
    (36, 2, 1, ('What is the smallest odd factor of 36 that is not 1?\n','3','Factor Operations', 'Foundations')),
    (36, 3, 2, ('How many even factors of 36 are there?\n','5','Factor Operations', 'Foundations')),
    (36, 3, 1, ('How many odd factors of 36 are there?\n','3','Factor Operations', 'Foundations')),
]

@pytest.mark.parametrize("num,question,even,answer", testdata)
def test_factor_quiz(num, question, even, answer):
    factors = bf.factor_quiz(num1 = num, question_num = question, is_even = even)
    assert factors == answer

