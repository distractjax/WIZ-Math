# Arithmetic and Number Properties Practice

from foundations.basic_fractions import multiply_by_fractions_quiz, divide_by_fractions_quiz, multiply_fractions_with_exponents
from foundations.basic_multiples import n_digit_multiples_quiz, common_n_digit_multiples_quiz
from foundations.basic_factors import factor_quiz, prime_factor_quiz
from random import randint
from collections import defaultdict

def function_picker(user_in: str):
    function_dict = {
    'multiply by fractions': multiply_by_fractions_quiz,
    'divide by fractions': divide_by_fractions_quiz,
    'multiply fractions with exponents': multiply_fractions_with_exponents,
    'n-digit multiples': n_digit_multiples_quiz,
    'common n-digit multiples': common_n_digit_multiples_quiz,
    'factor operations': factor_quiz,
    'prime factor operations': prime_factor_quiz,
    }
    keys = list(function_dict.keys())
    user_in = user_in.lower().strip()
    if user_in in keys:
        function_dict[user_in]()
    elif user_in == 'get options':
        print('\n'.join(x.title() for x in keys))
        return 2 
    elif user_in == 'random':
        random_key = keys[randint(0,len(keys)-1)]
        function_dict[random_key]()
    else:
        print("I'm sorry, I didn't understand your input. The options are:\n"+'\n'.join(x.title() for x in keys))
        return 2 

def main():
    user_in = input('What would you like to do? Type "Get Options" if you want to see all the available functions, or just select "Random" to get started.\nYou can also type "Exit" to quit the program.\n')
    while user_in.lower().strip() != "exit":
        problem_result = function_picker(user_in)
        if problem_result != 2:
            user_in = input('Would you like to go again?\n')
            if user_in.lower().strip() == "no":
                break
        user_in = input('Which would you like to try?\n')

if __name__ == "__main__":
    main()
