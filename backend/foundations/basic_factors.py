from math_basics import find_factors
from random import randint, getrandbits

def factor_quiz() -> bool:
    '''
    This generates simple quiz questions about the factors of a number.
    '''
    num1 = randint(4, 200)
    while len(find_factors(num1)) == 2:
        num1 = randint(4,200)
    num1_factors = find_factors(num1)
    num1_factors.pop(0)
    num1_factors.pop(-1)

    if 2 not in num1_factors:
        is_even = False
    else:
        is_even = bool(getrandbits(1))

    if is_even:
        is_even_string = 'even'
        output_factors = [x for x in num1_factors if x % 2 == 0]
    else:
        is_even_string = 'odd'
        output_factors = [x for x in num1_factors if x % 2 == 1]

    random_number = randint(1,3)

    # This is kind of a micro-optimization thing, but these dictionaries are running these functions regardless of the input
    questions = {
        1: f'What is the largest {is_even_string} factor of {num1}?\n',
        2: f'What is the smallest {is_even_string} factor of {num1}?\n',
        3: f'How many {is_even_string} factors of {num1} are there?\n'
    }
    answers = {
        1: max(output_factors),
        2: min(output_factors),
        3: len(output_factors),
    }
    responses = {
        1: f'The largest {is_even_string} factor of {num1} is \n{answers[random_number]}',
        2: f'The smallest {is_even_string} factor of {num1} is \n{answers[random_number]}',
        3: f'The {is_even_string} factors of {num1} are \n{output_factors}',
    }

    if int(input(questions[random_number])) == answers[random_number]:
        print(f'Correct! {responses[random_number]}')
        return True
    else:
        print(f'Incorrect! {responses[random_number]}')
        return False

def prime_factor_quiz() -> bool:
    '''
    This generates simple quiz questions about the prime factors of a number.
    '''
    num1 = randint(4, 200)
    num1_factors = find_factors(num1)

    prime_factors = [x for x in num1_factors[1:] if len(find_factors(x)) == 2]
    prime_factors.insert(0,1)

    questions = {
        1: f'What is the largest prime factor of {num1}?\n',
        2: f'What is the smallest prime factor of {num1}?\n',
        3: f'How many prime factors of {num1} are there?\n'
    }
    answers = {
        1: max(prime_factors),
        2: min(prime_factors),
        3: len(prime_factors),
    }

    random_number = randint(1,3)

    if int(input(questions[random_number])) == answers[random_number]:
        print(f'Correct! The prime factors of {num1} are \n{prime_factors}')
        return True
    else:
        print(f'Incorrect, the prime factors of {num1} are \n{prime_factors}')
        return False

if __name__ == "__main__":
    factor_quiz()
    # prime_factor_quiz()
