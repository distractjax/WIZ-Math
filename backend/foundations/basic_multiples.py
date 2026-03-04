from random import randint
from backend.core_math import get_n_digit_multiples, get_least_common_multiple
from backend.foundations.common import MODULE_NAME
from datetime import datetime
import config

def quiz(func):
    def record_question() -> None:
        question, answer, func_name, module_name = func()
        exec_time = datetime.now()
        config.write_solution_json(exec_time, question, answer)
        config.create_question_row(exec_time, module_name, func_name)
        print(question, answer, func_name)
    return record_question

@quiz
def common_n_digit_multiples_quiz(num1: int = 0, num2: int = 0, n_digits: int = 0, question_num: int = 0) -> tuple[str, str, str, str]:
    '''
    Generates questions about the common multiples of a set of numbers. 
    '''
    # num1 will evaluate to "False" if it equals 0
    num1 = num1 or randint(2,20)
    num2 = num2 or randint(2,20)
    n_digits = n_digits or randint(2,4)
    question_num = question_num or randint(1,3)

    if num1 < 2 or num1 > 20 or num2 < 2 or num2 > 20:
        raise ValueError("This function only accepts numbers as small as 2 and as large as 20.")
    elif n_digits < 2 or n_digits > 4:
        raise ValueError("The number of digits in this function must be greater than 2 and less than 4.")
    elif question_num < 1 or question_num > 3:
        raise ValueError("The question list only has 3 entries.")

    numbers = [num1, num2]
    numbers.sort()

    least_common_multiple = get_least_common_multiple(numbers[0], numbers[1])

    common_n_digit_multiples = get_n_digit_multiples(least_common_multiple, n_digits)

    questions = [
        f'What is the largest {n_digits}-digit multiple of {num1} that is also a multiple of {num2}?\n',
        f'What is the smallest {n_digits}-digit multiple of {num1} that is also a multiple of {num2}?\n',
        f'How many {n_digits}-digit multiples of {num1} are also multiples of {num2}?\n'
    ]
    answers = [
        max(common_n_digit_multiples),
        min(common_n_digit_multiples),
        len(common_n_digit_multiples),
    ]
    return (questions[question_num-1], str(answers[question_num-1]), "Common N-Digit Multiples", MODULE_NAME)

@quiz
def n_digit_multiples_quiz(num: int = 0, n_digits: int = 0, question_num: int = 0) -> tuple[str,str,str,str]:
    '''
    Generates questions about the properties of the set of multiples of a given number that are n-digits long. 
    '''

    num = num or randint(2, 25)
    n_digits = n_digits or randint(2, 4)
    question_num = question_num or randint(1,3)

    if num < 2 or num > 25:
        raise ValueError("This function only accepts numbers as small as 2 and as large as 25.")
    elif n_digits < 2 or n_digits > 4:
        raise ValueError("The number of digits in this function must be greater than 2 and less than 4.")
    elif question_num < 1 or question_num > 3:
        raise ValueError("The question list only has 3 entries.")

    multiples = get_n_digit_multiples(number = num, number_of_digits = n_digits)

    questions = [
        f'What is the largest {n_digits}-digit multiple of {num}?\n',
        f'What is the smallest {n_digits}-digit multiple of {num}?\n',
        f'How many {n_digits}-digit multiples are there of {num}?\n'
    ]
    answers = [
        max(multiples),
        min(multiples),
        len(multiples),
    ]

    return (questions[question_num-1], str(answers[question_num-1]), "N-Digit Multiples", MODULE_NAME)

if __name__ == "__main__":
    # common_n_digit_multiples_quiz()
    n_digit_multiples_quiz()
