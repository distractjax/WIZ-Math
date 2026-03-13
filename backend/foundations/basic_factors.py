from backend.core_math import find_factors, is_power_of_two
from backend.foundations.common import MODULE_NAME
from random import randint, getrandbits
import config
from datetime import datetime

# Current issues with factor_quiz:
# 1. It breaks on numbers that only have the factors [1, sqrt(x), x]
# 2. It breaks on the number 4 when is_even is set to False
@config.quiz
def factor_quiz(num1: int = 0, question_num: int = 0, is_even: int = 0) -> tuple[str, str, str, str]:
    '''
    This generates simple quiz questions about the factors of a number.
    '''
    num1 = num1 or randint(4, 200)
    question_num = question_num or randint(1,3)

    if num1 > 200 or num1 < 4:
        raise ValueError("Your number must be between 4 and 200.")
    if question_num > 3 or question_num < 1:
        raise ValueError("The question list only has 3 entries.")
    if is_even > 2 or is_even < 0:
        raise ValueError("The is_even argument of this function must be between 0 and 2, inclusive.")

    # Handle prime number
    if len(find_factors(num1)) == 2:
        # This is the old logic
        # num1 = randint(num_range[0],num_range[1])
        return factor_quiz(num1 = num1 + 1, question_num = question_num, is_even = is_even)
    num1_factors = find_factors(num1)

    if 2 in num1_factors:
        if is_power_of_two(num1):
            is_even = True
        elif 0 == is_even:
            is_even = bool(getrandbits(1))
        else:
            is_even = bool(is_even - 1)
    else:
        is_even = 0

    if is_even:
        is_even_string = 'even'
        output_factors = [x for x in num1_factors if x % 2 == 0]
    else:
        is_even_string = 'odd'
        output_factors = [x for x in num1_factors if x % 2 == 1]

    output_len = len(output_factors)

    try:
        output_factors.remove(num1)
    except Exception:
        pass

    if 4 == num1 and 2 == question_num:
        question = f'What is the smallest even factor of {num1}?\n'
        answer = 2
    elif 1 == question_num:
        question = f'What is the largest {is_even_string} factor of {num1}?\n'
        answer = output_factors[-1]
        response = f'The largest {is_even_string} factor of {num1} is {answer}'
    elif 2 == question_num:
        question = f'What is the smallest {is_even_string} factor of {num1} that is not {output_factors[0]}?\n'
        answer = output_factors[1]
        response = f'The smallest {is_even_string} factor of {num1} is {answer}'
    else:
        question = f'How many {is_even_string} factors of {num1} are there?\n'
        answer = output_len
        response = f'The {is_even_string} factors of {num1} are {output_factors}'
 
    return (question, str(answer), "Factor Operations", MODULE_NAME)

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

    if 2 == len(num1_factors):
        return prime_factor_quiz(num1 = num1 + 1, question_num = question_num)

    prime_factors = [x for x in num1_factors[1:] if len(find_factors(x)) == 2]
    prime_factors.insert(0,1)

    questions = [
        f'What is the largest prime factor of {num1}?\n',
        f'What is the smallest prime factor of {num1} that is not 1 or 2?\n',
        f'How many prime factors of {num1} are there?\n'
    ]

    answers = [
        prime_factors[-2],
        prime_factors[1],
        len(prime_factors),
    ]

    return (questions[question_num - 1], str(answers[question_num - 1]), "Prime Factor Operations", MODULE_NAME)

if __name__ == "__main__":
    factor_quiz(num1=18,question_num=1,is_even=1)
    # prime_factor_quiz()
