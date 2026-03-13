import backend.foundations.basic_factors as bf
import pytest

testdata = [
    (12, 1, False, ('What is the largest odd factor of 12?\n','6','Factor Operations', 'Foundations'))
]

@pytest.mark.parametrize("num,question,even,answer", testdata)
def test_factor_quiz(num, question, even, answer):
    factors = bf.factor_quiz(num1 = num, question_num = question, is_even = even)
    assert factors == answer

