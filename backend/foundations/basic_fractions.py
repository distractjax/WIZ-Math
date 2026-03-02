from random import randint
from backend.core_math import simplify_fractions
from backend.foundations.common import MODULE_NAME
import config
from datetime import datetime

# Fractions

def divide_fractions_quiz(numerator_range: tuple[int, int] = (1,20), denominator_range: tuple[int, int] = (2, 20)) -> None:
    '''
    Generates a string that divides two fractions.
    '''
    numerator1 = randint(numerator_range[0],numerator_range[1])
    numerator2 = randint(numerator_range[0],numerator_range[1])

    denominator1 = randint(denominator_range[0],denominator_range[1])
    denominator2 = randint(denominator_range[0],denominator_range[1])

    while denominator1 == numerator1:
        denominator1 = randint(denominator_range[0],denominator_range[1])
    while denominator2 == numerator2:
        denominator2 = randint(denominator_range[0],denominator_range[1])

    solution_numerator = numerator1 * denominator2
    solution_denominator = denominator1 * numerator2

    simplified_solution = simplify_fractions(solution_numerator,solution_denominator)

    question = f'What is the result of ({numerator1}/{denominator1}) / ({numerator2}/{denominator2})?'
    answer = f'{simplified_solution[0]}/{simplified_solution[1]}'

    exec_time = datetime.now()

    config.write_solution_json(exec_time, question, answer)
    config.create_question_row(exec_time,MODULE_NAME,"Divide by Fractions")

def multiply_fractions_quiz(numerator_range: tuple[int, int] = (1,20), denominator_range: tuple[int, int] = (2,20)) -> None:
    '''
    Generates a string that multiplies two fractions.
    '''
    numerator1 = randint(numerator_range[0],numerator_range[1])
    numerator2 = randint(numerator_range[0],numerator_range[1])

    denominator1 = randint(denominator_range[0],denominator_range[1])
    denominator2 = randint(denominator_range[0],denominator_range[1])

    while denominator1 == numerator1:
        denominator1 = randint(denominator_range[0],denominator_range[1])
    while denominator2 == numerator2:
        denominator2 = randint(denominator_range[0],denominator_range[1])

    solution_numerator = numerator1 * numerator2
    solution_denominator = denominator1 * denominator2

    simplified_solution = simplify_fractions(solution_numerator,solution_denominator)

    question = f'What is the result of ({numerator1}/{denominator1}) * ({numerator2}/{denominator2})?'
    answer = f'{simplified_solution[0]}/{simplified_solution[1]}'

    exec_time = datetime.now()

    config.write_solution_json(exec_time, question, answer)
    config.create_question_row(exec_time,MODULE_NAME,"Multiply by Fractions")

# TODO: Add in division function for this same process
def multiply_fractions_with_exponents(num_range: tuple[int, int] = (2,10), exponent_range: tuple[int, int] = (2,3)) -> None:
    '''
    Generates a string that multiplies two fractions that are defined by exponents.
    '''
    numerator1 = randint(num_range[0],num_range[1])
    numerator2 = randint(num_range[0],num_range[1])
    denominator = randint(num_range[0],num_range[1])

    while denominator == numerator1 or denominator == numerator2:
        denominator = randint(num_range[0],num_range[1])

    numerator1_exponent = randint(exponent_range[0],exponent_range[1])
    numerator2_exponent = randint(exponent_range[0],exponent_range[1])
    denominator_exponent = randint(exponent_range[0],exponent_range[1])

    solution_numerator = (numerator1 ** numerator1_exponent) * (numerator2 ** numerator2_exponent)
    solution_denominator = denominator ** denominator_exponent

    simplified_solution = simplify_fractions(solution_numerator,solution_denominator)

    question = f'What is the result of ({numerator1}^{numerator1_exponent}) * ({numerator2}^{numerator2_exponent}) / ({denominator}^{denominator_exponent})?'
    answer = f'{simplified_solution[0]}/{simplified_solution[1]}'

    exec_time = datetime.now()

    config.write_solution_json(exec_time, question, answer)
    config.create_question_row(exec_time,MODULE_NAME,"Multiply Fractions with Exponents")

# TODO: Add in division function for this same process
# TODO: This function is going to be added back in when I split out the TUI event loop into two events, the way it's handled right now doesn't work.
def multiply_remainders(numerator_range: tuple[int, int] = (2,20), denominator_range: tuple[int, int] = (2,9)) -> None:
    '''
    This generates a question based off the remainders of numbers when divided by a given number.
    '''
    numerator1 = randint(numerator_range[0],numerator_range[1])
    numerator2 = randint(numerator_range[0],numerator_range[1])
    denominator = randint(denominator_range[0],denominator_range[1])

    remainder1 = numerator1 % denominator
    remainder2 = numerator2 % denominator

    answer = (remainder1 * remainder2) % denominator

    question = f'When integer a is divided by {denominator}, the remainder is {remainder1}.\nWhen integer b is divided by {denominator}, the remainder is {remainder2}.\nWhat is the remainder when a x b is divided by {denominator}?'

    exec_time = datetime.now()

    config.write_solution_json(exec_time, question, str(answer))
    config.create_question_row(exec_time,MODULE_NAME,"Multiply Remainders")
