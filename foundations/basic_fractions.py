from random import randint
from math_basics import simplify_fractions

# Fractions

def divide_by_fractions_quiz() -> bool:
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

def multiply_by_fractions_quiz() -> bool:
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
