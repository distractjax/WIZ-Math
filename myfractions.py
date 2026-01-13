from random import randint
from basics import find_factors, multiply_by_result

def divide_by_fractions() -> bool:
    '''
    Generates a string that divides two fractions.
    '''
    solution_numerator = randint(1, 100)
    solution_denominator = randint(2, 100)

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
    solution_numerator = randint(1, 100)
    solution_denominator = randint(2, 100)

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
    if result == f'{solution_numerator}/{solution_denominator}':
        print('Correct!')
        return True
    else:
        print(f'Incorrect, the solution is: \n{solution_numerator} / {solution_denominator}')
        return False
