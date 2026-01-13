# Arithmetic and Number Properties Practice

from myfractions import multiply_by_fractions, divide_by_fractions
from random import randint

def function_picker(user_in: str):
    function_dict = {
    'multiply by fractions': multiply_by_fractions,
    'divide by fractions': divide_by_fractions,
    }
    keys = list(function_dict.keys())
    user_in = user_in.lower().strip()
    if user_in == 'get options':
        print('\n'.join(x.title() for x in keys))
    elif user_in == 'random':
        random_key = keys[randint(0,len(keys)-1)]
        function_dict[random_key]()
    else:
        function_dict[user_in]()

def main():
    user_in = input('What would you like to do? Type "Get Options" if you want to see all the available functions, or just select "Random" to get started.\n')
    function_picker(user_in)

if __name__ == "__main__":
    main()
