# Arithmetic and Number Properties Practice

from math_basics import multiply_by_fractions, divide_by_fractions, n_digit_multiples
from random import randint

def function_picker(user_in: str):
    function_dict = {
    'multiply by fractions': multiply_by_fractions,
    'divide by fractions': divide_by_fractions,
    'n-digit multiples': n_digit_multiples,
    }
    keys = list(function_dict.keys())
    user_in = user_in.lower().strip()
    if user_in == 'get options':
        print('\n'.join(x.title() for x in keys))
        return 2 
    elif user_in == 'random':
        random_key = keys[randint(0,len(keys)-1)]
        function_dict[random_key]()
    else:
        function_dict[user_in]()

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
