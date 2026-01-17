from math_basics import simplify_fractions
from random import randint, getrandbits

def multiplying_remainders() -> bool:
    '''
    This generates a question based off the remainders of numbers when divided by a given number.
    '''
    numerator1 = randint(2,20)
    numerator2 = randint(2,20)
    denominator = randint(2,9)

    remainder1 = numerator1 % denominator
    remainder2 = numerator2 % denominator

    solution_remainder = (remainder1 * remainder2) % denominator

    result = int(input(f'When intger a is divided by {denominator}, the remainder is {remainder1}.\nWhen integer b is divided by {denominator}, the remainder is {remainder2}.\nWhat is the remainder when a x b is divided by {denominator}?\n'))
    if result == solution_remainder:
        print('Correct!')
        return True
    else:
        print(f'Incorrect, the solution is: {solution_remainder}')
        return False

def main():
    multiplying_remainders()

if __name__ == "__main__":
    main()
