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

    simplified_solution = simplify_fractions(solution_numerator,solution_denominator)

    result = input(f'What is the result of ({numerator1}/{denominator1}) / ({numerator2}/{denominator2})?\n')
    result = ''.join([ch for ch in result if not ch.isspace()])
    if result == f'{simplified_solution[0]}/{simplified_solution[1]}':
        print('Correct!')
        return True
    else:
        print(f'Incorrect, the solution is: \n{simplified_solution[0]} / {simplified_solution[1]}')
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

    simplified_solution = simplify_fractions(solution_numerator,solution_denominator)

    result = input(f'What is the result of ({numerator1}/{denominator1}) * ({numerator2}/{denominator2})?\n')
    result = ''.join([ch for ch in result if not ch.isspace()])
    if result == f'{simplified_solution[0]}/{simplified_solution[1]}':
        print('Correct!')
        return True
    else:
        print(f'Incorrect, the solution is: \n{simplified_solution[0]} / {simplified_solution[1]}')
        return False


def simplify_fractions(numerator: int, denominator: int) -> tuple[int]:
    '''
    This returns the most simplified version of a given fraction
    '''
    numerator_factors = find_factors(numerator)
    denominator_factors = find_factors(denominator)

    while True:
        if (numerator != 1) and (denominator != 1):
            numerator_factors = find_factors(numerator)
            denominator_factors = find_factors(denominator)

            common_factors = [x for x in numerator_factors if x in denominator_factors]
            # print(common_factors)

            if len(common_factors) >= 2:
                numerator = numerator // common_factors[1]
                # print(numerator)
                denominator = denominator // common_factors[1]
                # print(denominator)

            else:
                return (numerator, denominator)
        else:
            return (numerator, denominator)

# Multiples

def n_digit_multiples() -> array[int]:
    '''
    Generates the multiples of a number that are n-number of digits
    '''

    number = randint(1,25)
    number_of_digits = randint(2,5)

    digits_check = int('1'+''.join(['0' for x in range(1,number_of_digits)]))
    # print(digits_check)
    current_number = (ceil(digits_check / number))

    output = array('I')
    while len(str(current_number * number)) == number_of_digits:
        output.append(current_number * number)
        current_number += 1

    random_number = randint(1,3)
    questions = {
        1: f'What is the largest {number_of_digits}-digit multiple of {number}?\n',
        2: f'What is the smallest {number_of_digits}-digit multiple of {number}?\n',
        3: f'How many {number_of_digits}-digit multiples are there of {number}?\n'
    }
    answers = {
        1: max(output),
        2: min(output),
        3: len(output),
    }

    if int(input(questions[random_number])) == answers[random_number]:
        print('Correct!')
        return True
    else:
        print(f'Incorrect, the answer is \n{answers[random_number]}')
        return False
