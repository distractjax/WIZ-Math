from backend.core_math import find_factors
from backend.foundations.common import MODULE_NAME
from random import randint, getrandbits
import config
from datetime import datetime

@config.quiz
def factor_quiz(num1: int = 0, question_num: int = 0, is_even: bool = False) -> tuple[str, str, str, str]:
    '''
    This generates simple quiz questions about the factors of a number.
    '''
    num1 = num1 or randint(4, 200)
    question_num = question_num or randint(1,3)

    if num1 > 200 or num1 < 4:
        raise ValueError("Your number must be between 4 and 200.")
    if question_num > 3 or question_num < 1:
        raise ValueError("The question list only has 3 entries.")

    # Handle prime number
    if len(find_factors(num1)) == 2:
        # This is the old logic
        # num1 = randint(num_range[0],num_range[1])
        find_factors(num1 + 1)
    num1_factors = find_factors(num1)

    if 2 in num1_factors:
        is_even = bool(num1_factors[2] % 2)

    if is_even:
        is_even_string = 'even'
        output_factors = [x for x in num1_factors if x % 2 == 0]
    else:
        is_even_string = 'odd'
        output_factors = [x for x in num1_factors if x % 2 == 1]

    questions = [
        f'What is the largest {is_even_string} factor of {num1}?\n',
        f'What is the smallest {is_even_string} factor of {num1}?\n',
        f'How many {is_even_string} factors of {num1} are there?\n'
    ]

    answers = [
        # Output_factors is sorted.
        output_factors[-2],
        output_factors[1],
        len(output_factors),
    ]

    responses = [
        f'The largest {is_even_string} factor of {num1} is \n{answers[question_num - 1]}',
        f'The smallest {is_even_string} factor of {num1} is \n{answers[question_num - 1]}',
        f'The {is_even_string} factors of {num1} are \n{output_factors}',
    ]
 
    return (questions[question_num - 1], str(answers[question_num - 1]), "Factor Operations", MODULE_NAME)

@config.quiz
def prime_factor_quiz(num1: int = 0, question_num: int = 0) -> tuple[str, str, str, str]:
    '''
    This generates simple quiz questions about the prime factors of a number.
    '''
    num1 = num1 or randint(4, 200)
    question_num = question_num or randint(1,3)

    if num1 > 200 or num1 < 4:
        raise ValueError("Your number must be between 4 and 200.")
    if question_num > 3 or question_num < 1:
        raise ValueError("The question list only has 3 entries.")

    num1_factors = find_factors(num1)

    prime_factors = [x for x in num1_factors[1:] if len(find_factors(x)) == 2]
    prime_factors.insert(0,1)

    questions = [
        f'What is the largest prime factor of {num1}?\n',
        f'What is the smallest prime factor of {num1}?\n',
        f'How many prime factors of {num1} are there?\n'
    ]

    answers = [
        prime_factors[-2],
        prime_factors[1],
        len(prime_factors),
    ]

    return (questions[question_num - 1], str(answers[question_num - 1]), "Prime Factor Operations", MODULE_NAME)

if __name__ == "__main__":
    factor_quiz()
    # prime_factor_quiz()
