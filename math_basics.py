from math import sqrt, ceil
from functools import reduce
from array import array, ArrayType
from random import randrange, randint

# Core Functions

def find_factors(input: int) -> array[int]:
    '''
    Generates a sorted array of all a given number's factors.
    '''
    # This applies list.__add__, the internal method that the list class uses to add elements, to the generator function using reduce
    output = set(reduce(list.__add__,([i, input // i] for i in range(1, ceil(sqrt(input))) if input % i == 0)))
    output = array('I',sorted(output))
    return output

def multiply_by_result(input: int) -> int:
    '''
    Returns two numbers that multiply to create the result.
    '''
    factors = find_factors(input)
    index_int = randrange(len(factors) // 2)
    factor1, factor2 = factors[index_int], factors[-index_int - 1]
    return factor1, factor2

# Fractions

def divide_by_fractions() -> bool:
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

    numerator_factors = find_factors(solution_numerator)
    denominator_factors = find_factors(solution_denominator)

    # This loop logic isn't correct. This loops through all of the factors in the original numerator,
    # it doesn't re-test for factors of the new one.
    while True:
        for factor in numerator_factors:
            if factor in denominator_factors and factor != 1:
                solution_numerator = solution_numerator // factor
                solution_denominator = solution_denominator // factor
        break

    result = input(f'What is the result of ({numerator1}/{denominator1}) / ({numerator2}/{denominator2})?\n')
    result = ''.join([ch for ch in result if not ch.isspace()])
    if result == f'{solution_numerator}/{solution_denominator}':
        print('Correct!')
        return True
    else:
        print(f'Incorrect, the solution is: \n{solution_numerator} / {solution_denominator}')
        return False

def multiply_by_fractions() -> bool:
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

    numerator_factors = find_factors(solution_numerator)
    denominator_factors = find_factors(solution_denominator)

    # This loop logic isn't correct. This loops through all of the factors in the original numerator,
    # it doesn't re-test for factors of the new one.
    while True:
        for factor in numerator_factors:
            if factor in denominator_factors and factor != 1:
                solution_numerator = solution_numerator // factor
                solution_denominator = solution_denominator // factor
        break

    result = input(f'What is the result of ({numerator1}/{denominator1}) * ({numerator2}/{denominator2})?\n')
    result = ''.join([ch for ch in result if not ch.isspace()])
    if result == f'{solution_numerator}/{solution_denominator}':
        print('Correct!')
        return True
    else:
        print(f'Incorrect, the solution is: \n{solution_numerator} / {solution_denominator}')
        return False

# Multiples

def n_digit_multiples(number:int, number_of_digits:int) -> array[int]:
    '''
    Generates the multiples of a number that are n-number of digits
    '''
    digits_check = int('1'+''.join(['0' for x in range(1,number_of_digits)]))
    print(digits_check)
    current_number = (ceil(digits_check / number))
    output = array('I')
    while len(str(current_number * number)) == number_of_digits:
        output.append(current_number)
        current_number += 1
    print(output)
    return True
