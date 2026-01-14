from random import randint
from basics import find_factors, multiply_by_result

def divide_by_fractions() -> bool:
    '''
    Generates a string that divides two fractions.
    '''
    numerator1 = randint(1,100)
    numerator2 = randint(1,100)
    while denominator1 == numerator:
        denominator1 = randint(2, 100)

    denominator1 = randint(2,100)
    denominator2 = randint(2,100)

    while denominator1 == numerator1:
        denominator1 = randint(2, 100)
    while denominator2 == numerator2:
        denominator2 = randint(2, 100)

    solution_numerator = numerator1 * denominator2
    solution_denominator = numerator2 * denominator1

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
    numerator1 = randint(1,100)
    numerator2 = randint(1,100)
    while denominator1 == numerator:
        denominator1 = randint(2, 100)

    denominator1 = randint(2,100)
    denominator2 = randint(2,100)

    while denominator1 == numerator1:
        denominator1 = randint(2, 100)
    while denominator2 == numerator2:
        denominator2 = randint(2, 100)

    solution_numerator = numerator1 * denominator1
    solution_denominator = numerator2 * denominator2

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
        print(f'Incorrect, the solution is: \n{solution_numerator} * {solution_denominator}')
        return False
