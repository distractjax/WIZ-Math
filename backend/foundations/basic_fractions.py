from random import randint
from backend.core_math import simplify_fractions
import config

# Fractions

def divide_fractions_quiz() -> bool:
    '''
    Generates a string that divides two fractions.
    '''
    numerator1 = randint(1,20)
    numerator2 = randint(1,20)

    denominator1 = randint(2,20)
    denominator2 = randint(2,20)

    while denominator1 == numerator1:
        denominator1 = randint(2, 20)
    while denominator2 == numerator2:
        denominator2 = randint(2, 20)

    solution_numerator = numerator1 * denominator2
    solution_denominator = denominator1 * numerator2

    simplified_solution = simplify_fractions(solution_numerator,solution_denominator)

    question = f'What is the result of ({numerator1}/{denominator1}) / ({numerator2}/{denominator2})?'
    answer = f'{simplified_solution[0]}/{simplified_solution[1]}'

    config.write_solution_json(question,answer)

def multiply_fractions_quiz() -> bool:
    '''
    Generates a string that multiplies two fractions.
    '''
    numerator1 = randint(1,20)
    numerator2 = randint(1,20)

    denominator1 = randint(2,20)
    denominator2 = randint(2,20)

    while denominator1 == numerator1:
        denominator1 = randint(2, 20)
    while denominator2 == numerator2:
        denominator2 = randint(2, 20)

    solution_numerator = numerator1 * numerator2
    solution_denominator = denominator1 * denominator2

    simplified_solution = simplify_fractions(solution_numerator,solution_denominator)

    question = f'What is the result of ({numerator1}/{denominator1}) * ({numerator2}/{denominator2})?'
    answer = f'{simplified_solution[0]}/{simplified_solution[1]}'

    config.write_solution_json(question,answer)

# TODO: Add in division function for this same process
def multiply_fractions_with_exponents() -> bool:
    '''
    Generates a string that multiplies two fractions that are defined by exponents.
    '''
    numerator1 = randint(2,10)
    numerator2 = randint(2,10)
    denominator = randint(2,10)

    while denominator == numerator1 or denominator == numerator2:
        denominator = randint(2, 20)

    numerator1_exponent = randint(2,5)
    numerator2_exponent = randint(2,5)
    denominator_exponent = randint(2,5)

    solution_numerator = (numerator1 ** numerator1_exponent) * (numerator2 ** numerator2_exponent)
    solution_denominator = denominator ** denominator_exponent

    simplified_solution = simplify_fractions(solution_numerator,solution_denominator)

    question = f'What is the result of ({numerator1}^{numerator1_exponent}) * ({numerator2}^{numerator2_exponent}) / ({denominator}^{denominator_exponent})?'
    answer = f'{simplified_solution[0]}/{simplified_solution[1]}'

    config.write_solution_json(question,answer)

# TODO: Add in division function for this same process
# TODO: This function is going to be added back in when I split out the TUI event loop into two events, the way it's handled right now doesn't work.
def multiply_remainders() -> bool:
    '''
    This generates a question based off the remainders of numbers when divided by a given number.
    '''
    numerator1 = randint(2,20)
    numerator2 = randint(2,20)
    denominator = randint(2,9)

    remainder1 = numerator1 % denominator
    remainder2 = numerator2 % denominator

    answer = (remainder1 * remainder2) % denominator

    question = f'When integer a is divided by {denominator}, the remainder is {remainder1}.\nWhen integer b is divided by {denominator}, the remainder is {remainder2}.\nWhat is the remainder when a x b is divided by {denominator}?'

    config.write_solution_json(question,answer)
