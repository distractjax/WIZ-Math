from random import randint
from backend.core_math import find_factors, prime_factorization
from fractions import Fraction
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

    # I don't really care if cross-wise equality happens (ex: 5/6 / 6/5) because that won't simplify down to 1. This just keeps problems interesting.
    if denominator1 == numerator1 or numerator1 == numerator2:
        return divide_fractions_quiz(numerator1 = numerator1 + 1 if numerator1 < 20 else numerator1 - 1,
                                     numerator2 = numerator2, denominator1 = denominator1, denominator2 = denominator2)
    if denominator2 == numerator2 or denominator1 == denominator2:
        return divide_fractions_quiz(numerator1 = numerator1, numerator2 = numerator2, denominator1 = denominator1,
                                     denominator2 = denominator2 + 1 if denominator2 < 20 else denominator2 - 1)

    solution = Fraction(numerator = (numerator1 * denominator2),
                        denominator = (numerator2 * denominator1))

    question = f'What is the result of ({numerator1}/{denominator1}) / ({numerator2}/{denominator2})?\n'
    answer = f'{solution.numerator}/{solution.denominator}'

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

    if numerator1 > 20 or numerator1 < 1:
        raise ValueError("Numerator 1 must be a number between 1 and 20.")
    if numerator2 > 20 or numerator2 < 1:
        raise ValueError("Numerator 2 must be a number between 1 and 20.")
    if denominator1 > 20 or denominator1 < 2:
        raise ValueError("Denominator 1 must be a number between 2 and 20.")
    if denominator2 > 20 or denominator2 < 2:
        raise ValueError("Denominator 2 must be a number between 2 and 20.")

    # I don't care about horizontal equality here (ex: 5/6 * 5/6) because it won't simplify to 1. This just keeps problems more interesting.
    if numerator1 == denominator1 or numerator1 == denominator2:
        return multiply_fractions_quiz(numerator1 = numerator1 + 1 if numerator1 < 20 else numerator1 - 1,
                                     numerator2 = numerator2, denominator1 = denominator1, denominator2 = denominator2)
    if numerator2 == denominator1 or numerator2 == denominator2:
        return multiply_fractions_quiz(numerator1 = numerator1, 
                                     numerator2 = numerator2 + 1 if numerator2 < 20 else numerator2 - 1,
                                     denominator1 = denominator1, denominator2 = denominator2)

    solution = Fraction(numerator = (numerator1 * numerator2),
                        denominator = (denominator1 * denominator2))

    question = f'What is the result of ({numerator1}/{denominator1}) * ({numerator2}/{denominator2})?\n'
    answer = f'{solution.numerator}/{solution.denominator}'

    return (question, answer, "Multiply by Fractions", MODULE_NAME)

@config.quiz
def multiply_fractions_with_exponents(denominator_index: int = 0, denominator_exponent: int = 0, numerator_exponent: int = 0, square_or_cube: int = 0) -> tuple[str, str, str, str]:
    '''
    Generates a string that multiplies two fractions that are defined by exponents.
    '''
    # There are special properties of exponents that I can add in later that would make these more interesting, but for right now I think this is fine. I can always come back later and add in some more functionality, and I don't think continuing to work on this is a good use of my dev time.

    compound_numbers = [6, 10, 12, 14, 15, 18, 20]
    denominator_index = denominator_index or randint(1,7)
    denominator_exponent = denominator_exponent or randint(2,9)
    numerator_exponent = numerator_exponent or randint(1,9)
    square_or_cube = square_or_cube or randint(2,3)

    denominator_index -= 1

    if denominator_index > 6 or denominator_index < 0:
        raise ValueError("Denominator must be between 0 and 6")
    if denominator_exponent > 9 or denominator_exponent < 2:
        raise ValueError("Denominator's exponent must be between 2 and 9")
    if numerator_exponent > 9 or numerator_exponent < 1:
        raise ValueError("Numerator's exponent must be between 1 and 3")
    if square_or_cube > 3 or square_or_cube < 2:
        raise ValueError("square_or_cube must be either 2 or 3")

    denominator = compound_numbers[denominator_index]

    denominator_primes = prime_factorization(denominator)
    numerator1 = denominator_primes[0][0]
    numerator1_exponent = denominator_primes[0][1]
    numerator2 = denominator_primes[1][0]
    numerator2_exponent = denominator_primes[1][1]

    numerator_exponent = numerator_exponent * square_or_cube

    numerator1_exponent += numerator_exponent - 1
    numerator2_exponent += numerator_exponent - 1

    answer = f'{denominator}^{numerator_exponent - denominator_exponent}'

    question = f'What is the result of ({numerator1}^{numerator1_exponent}) * ({numerator2}^{numerator2_exponent}) / ({denominator}^{denominator_exponent})?\n'

    return (question, answer, "Multiply Fractions with Exponents", MODULE_NAME)

# TODO: Add in division function for this same process
# TODO: This function is going to be added back in when I split out the TUI event loop into two events, the way it's handled right now doesn't work.
@config.quiz
def multiply_remainders(numerator1: int = 0, numerator2: int = 0, denominator: int = 0) -> tuple[str, str, str, str]:
    '''
    This generates a question based off the remainders of numbers when divided by a given number.
    '''
    numerator1 = numerator1 or randint(1, 20)
    numerator2 = numerator2 or randint(1, 20)
    denominator = denominator or randint(2, 9)

    # Out of bounds exceptions

    if numerator1 > 20 or numerator1 < 1:
        raise ValueError("Numerator 1 must be between 1 and 20.")
    if numerator2 > 20 or numerator2 < 1:
        raise ValueError("Numerator 2 must be between 1 and 20.")
    if denominator > 9 or denominator < 2:
        raise ValueError("Denominator must be between 2 and 20.")

    # Recursion for handling if numerator1 == numerator 2 or denominator is a factor of either.
    if numerator1 == numerator2 or not numerator1 % denominator:
        return multiply_remainders(
            numerator1 = numerator1 + 1 if numerator1 < 20 else numerator1 -1,
            numerator2 = numerator2 if numerator2 < 19 else numerator2 % denominator,
            denominator = denominator)
    elif not numerator2 % denominator:
        return multiply_remainders(
            numerator1 = numerator1 if numerator1 < 19 else numerator1 % denominator,
            numerator2 = numerator2 + 1 if numerator2 < 20 else numerator2 -1,
            denominator = denominator)

    remainder1 = numerator1 % denominator
    remainder2 = numerator2 % denominator

    answer = (remainder1 * remainder2) % denominator

    question = f'When integer a is divided by {denominator}, the remainder is {remainder1}.\nWhen integer b is divided by {denominator}, the remainder is {remainder2}.\nWhat is the remainder when a x b is divided by {denominator}?\n'

    return (question, str(answer), "Multiply Remainders", MODULE_NAME)

if __name__ == "__main__":
    # divide_fractions_quiz()
    # multiply_fractions_quiz()
    multiply_fractions_with_exponents()
    # multiply_remainders()
