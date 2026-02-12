from random import randint
from math_basics import get_n_digit_multiples, get_least_common_multiple
import config

def common_n_digit_multiples_quiz() -> bool:
    '''
    Generates questions about the common multiples of a set of numbers. 
    '''
    num1 = randint(2,20)
    num2 = randint(2,20)
    n_digits = randint(2,4)

    numbers = [num1, num2]
    numbers.sort()

    least_common_multiple = get_least_common_multiple(numbers[0], numbers[1])

    common_n_digit_multiples = get_n_digit_multiples(least_common_multiple, n_digits)

    questions = {
        1: f'What is the largest {n_digits}-digit multiple of {num1} that is also a multiple of {num2}?\n',
        2: f'What is the smallest {n_digits}-digit multiple of {num1} that is also a multiple of {num2}?\n',
        3: f'How many {n_digits}-digit multiples of {num1} are also multiples of {num2}?\n'
    }
    answers = {
        1: max(common_n_digit_multiples),
        2: min(common_n_digit_multiples),
        3: len(common_n_digit_multiples),
    }

    random_number = randint(1,3)

    config.write_solution(questions[random_number],answers[random_number])

def n_digit_multiples_quiz() -> bool:
    '''
    Generates questions about the properties of the set of multiples of a given number that are n-digits long. 
    '''

    num = randint(2, 25)
    num_digits = randint(2,4)
    multiples = get_n_digit_multiples(number = num, number_of_digits = num_digits)

    questions = {
        1: f'What is the largest {num_digits}-digit multiple of {num}?\n',
        2: f'What is the smallest {num_digits}-digit multiple of {num}?\n',
        3: f'How many {num_digits}-digit multiples are there of {num}?\n'
    }
    answers = {
        1: max(multiples),
        2: min(multiples),
        3: len(multiples),
    }

    random_number = randint(1,3)

    if int(input(questions[random_number])) == answers[random_number]:
        print('Correct!')
        return True
    else:
        print(f'Incorrect, the answer is \n{answers[random_number]}')
        return False

if __name__ == "__main__":
    common_n_digit_multiples_quiz()
    # n_digit_multiples_quiz()

