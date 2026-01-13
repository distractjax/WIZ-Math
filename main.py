# Arithmetic and Number Properties Practice

from math import sqrt, ceil
from functools import reduce
from array import array, ArrayType
from random import randrange, randint

def divide_by_fractions() -> str:
    '''
    Generates a string that divides two fractions.
    '''
    solution_numerator = randint(1, 100)
    solution_denominator = randint(1, 100)

    numerator_factors = find_factors(solution_numerator)
    denominator_factors = find_factors(solution_denominator)

    numerator1, denominator2 = multiply_by_result(solution_numerator)
    denominator1, numerator2 = multiply_by_result(solution_denominator)

    while True:
        for factor in numerator_factors:
            if factor in denominator_factors and factor != 1:
                solution_numerator = solution_numerator // factor
                solution_denominator = solution_denominator // factor
        break

    result = input(f'What is the result of ({numerator1}/{denominator1}) / ({numerator2}/{denominator2})?\n')
    result = ''.join([ch for ch in result if not ch.isspace()])
    return 'Correct' if result == f'{solution_numerator}/{solution_denominator}' else f'Incorrect, the solution is:\n{solution_numerator} / {solution_denominator}'

def find_factors(input: int) -> array[int]:
    '''
    Generates a sorted array of all a given number's factors.
    '''
    # This applies list.__add__, the internal method that the list class uses to add elements, to the generator function using reduce
    output = set(reduce(list.__add__,([i, input // i] for i in range(1, ceil(sqrt(input))) if input % i == 0)))
    output = array('I',sorted(output))
    return output

def multiply_by_fractions() -> str:
    '''
    Generates a string that multiplies two fractions.
    '''
    solution_numerator = randint(1, 100)
    solution_denominator = randint(1, 100)

    numerator_factors = find_factors(solution_numerator)
    denominator_factors = find_factors(solution_denominator)

    numerator1, numerator2 = multiply_by_result(solution_numerator)
    denominator1, denominator2 = multiply_by_result(solution_denominator)

    while True:
        for factor in numerator_factors:
            if factor in denominator_factors and factor != 1:
                solution_numerator = solution_numerator // factor
                solution_denominator = solution_denominator // factor
        break

    result = input(f'What is the result of ({numerator1}/{denominator1}) * ({numerator2}/{denominator2})?\n')
    result = ''.join([ch for ch in result if not ch.isspace()])
    return 'Correct' if result == f'{solution_numerator}/{solution_denominator}' else f'Incorrect, the solution is:\n{solution_numerator} / {solution_denominator}'

def multiply_by_result(input: int) -> int:
    '''
    Returns two numbers that multiply to create the result.
    '''
    factors = find_factors(input)
    index_int = randrange(len(factors) // 2)
    factor1, factor2 = factors[index_int], factors[-index_int - 1]
    return factor1, factor2

def main():
    print(multiply_by_fractions())
    print(divide_by_fractions())

if __name__ == "__main__":
    main()
