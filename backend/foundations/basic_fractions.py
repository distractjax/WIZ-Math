from random import randint
from backend.core_math import simplify_fractions
from backend.foundations.common import MODULE_NAME
import config
from datetime import datetime

# Fractions

@config.quiz
def divide_fractions_quiz(numerator1: int = 0, numerator2: int = 0, denominator1: int = 0, denominator2: int = 0) -> tuple[str, str, str, str]:
    '''
    Generates a string that divides two fractions.
    '''
    numerator1 = numerator1 or randint(1,20)
    numerator2 = numerator2 or randint(1,20)

    denominator1 = denominator1 or randint(2,20)
    denominator2 = denominator2 or randint(2,20)

    if numerator1 > 20 or numerator1 < 1:
        raise ValueError("Numerator 1 must be a number between 1 and 20.")
    if numerator2 > 20 or numerator2 < 1:
        raise ValueError("Numerator 2 must be a number between 1 and 20.")
    if denominator1 > 20 or denominator1 < 2:
        raise ValueError("Denominator 1 must be a number between 2 and 20.")
    if denominator2 > 20 or denominator2 < 2:
        raise ValueError("Denominator 2 must be a number between 2 and 20.")

    if denominator1 == numerator1 or numerator1 == numerator2:
        return divide_fractions_quiz(numerator1 = numerator1 + 1 if numerator1 < 20 else numerator1 - 1,
                                     numerator2 = numerator2, denominator1 = denominator1, denominator2 = denominator2)
    if denominator2 == numerator2 or denominator1 == denominator2:
        return divide_fractions_quiz(numerator1 = numerator1, numerator2 = numerator2, denominator1 = denominator1,
                                     denominator2 = denominator2 + 1 if denominator2 < 20 else denominator2 - 1)

    solution_numerator = numerator1 * denominator2
    solution_denominator = denominator1 * numerator2

    simplified_solution = simplify_fractions(solution_numerator,solution_denominator)

    question = f'What is the result of ({numerator1}/{denominator1}) / ({numerator2}/{denominator2})?\n'
    answer = f'{simplified_solution[0]}/{simplified_solution[1]}'

    return (question, answer, "Divide by Fractions", MODULE_NAME)

@config.quiz
def multiply_fractions_quiz(numerator1: int = 0, numerator2: int = 0, denominator1: int = 0, denominator2: int = 0) -> tuple[str, str, str, str]:
    '''
    Generates a string that multiplies two fractions.
    '''
    numerator1 = numerator1 or randint(1,20)
    numerator2 = numerator2 or randint(1,20)

    denominator1 = denominator1 or randint(2,20)
    denominator2 = denominator2 or randint(2,20)

    if denominator1 == numerator1:
        denominator1 += numerator1 - 1
    if denominator2 == numerator2:
        denominator2 += numerator2 - 1

    solution_numerator = numerator1 * numerator2
    solution_denominator = denominator1 * denominator2

    simplified_solution = simplify_fractions(solution_numerator,solution_denominator)

    question = f'What is the result of ({numerator1}/{denominator1}) * ({numerator2}/{denominator2})?\n'
    answer = f'{simplified_solution[0]}/{simplified_solution[1]}'

    return (question, answer, "Multiply by Fractions", MODULE_NAME)

# TODO: Add in division function for this same process
@config.quiz
def multiply_fractions_with_exponents(numerator1: int = 0, numerator2: int = 0, denominator: int = 0, numerator1_exponent: int = 0, numerator2_exponent: int = 0, denominator_exponent: int = 0) -> tuple[str, str, str, str]:
    '''
    Generates a string that multiplies two fractions that are defined by exponents.
    '''
    numerator1 = numerator1 or randint(2,10)
    numerator2 = numerator2 or randint(2,10)
    denominator = denominator or randint(2,10)

    if denominator == numerator1 or denominator == numerator2:
        denominator += (numerator1 + numerator2) // 2

    numerator1_exponent = numerator1_exponent or randint(2,3)
    numerator2_exponent = numerator2_exponent or randint(2,3)
    denominator_exponent = denominator_exponent or randint(2,3)

    solution_numerator = (numerator1 ** numerator1_exponent) * (numerator2 ** numerator2_exponent)
    solution_denominator = denominator ** denominator_exponent

    simplified_solution = simplify_fractions(solution_numerator,solution_denominator)

    question = f'What is the result of ({numerator1}^{numerator1_exponent}) * ({numerator2}^{numerator2_exponent}) / ({denominator}^{denominator_exponent})?\n'
    answer = f'{simplified_solution[0]}/{simplified_solution[1]}'

    return (question, answer, "Multiply Fractions with Exponents", MODULE_NAME)

# TODO: Add in division function for this same process
# TODO: This function is going to be added back in when I split out the TUI event loop into two events, the way it's handled right now doesn't work.
@config.quiz
def multiply_remainders(numerator1: int = 0, numerator2: int = 0, denominator: int = 0) -> tuple[str, str, str, str]:
    '''
    This generates a question based off the remainders of numbers when divided by a given number.
    '''
    numerator1 = numerator1 or randint(2, 20)
    numerator2 = numerator2 or randint(2, 20)
    denominator = denominator or randint(2, 9)

    remainder1 = numerator1 % denominator
    remainder2 = numerator2 % denominator

    answer = (remainder1 * remainder2) % denominator

    question = f'When integer a is divided by {denominator}, the remainder is {remainder1}.\nWhen integer b is divided by {denominator}, the remainder is {remainder2}.\nWhat is the remainder when a x b is divided by {denominator}?\n'

    return (question, str(answer), "Multiply Remainders", MODULE_NAME)
