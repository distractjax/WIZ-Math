from math import sqrt, ceil
from functools import reduce
from array import array, ArrayType
from collections import defaultdict
from random import randint

# General Functions
def function_picker(user_in: str, function_dict: dict[str]):
    user_in = user_in.lower().strip()
    keys = list(function_dict.keys())

    def show_options():
        print('\n'.join(x.title() for x in keys))
        return 2

    def run_random():
        random_key = keys[randint(0,len(keys)-1)]
        function_dict[random_key]()

    def handle_error():
        print("I'm sorry, I didn't understand your input. The options are:\n"+'\n'.join(x.title() for x in keys))
        return 2 

    function_map = defaultdict(lambda: handle_error)
    function_map.update(function_dict)
    function_map['get options'] = show_options
    function_map['random'] = run_random
    function_map['exit'] = lambda: "exit"
    result = function_map[user_in]()

    if result == "exit":
        return

    if result != 2:
        if input('Would you like to go again?\n').lower().strip() == 'no':
            return

    user_in = input('Which would you like to try?\n')
    function_picker(user_in,function_dict)

# Basic Factor Functions
def find_factors(input: int) -> array[int]:
    '''
    Generates a sorted array of all a given number's factors.
    '''
    # This applies list.__add__, the internal method that the list class uses to add elements, to the generator function using reduce
    output = set(reduce(list.__add__,([i, input // i] for i in range(1, ceil(sqrt(input))+1) if input % i == 0)))
    output = array('I',sorted(output))
    return output

# Basic Fraction Functions
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

            if len(common_factors) >= 2:
                numerator = numerator // common_factors[1]
                denominator = denominator // common_factors[1]

            else:
                return (numerator, denominator)
        else:
            return (numerator, denominator)

# Basic Multiples Functions
def get_n_digit_multiples(number: int, number_of_digits: int) -> array[int]:
    '''
    Generates the multiples of a number that are n-number of digits
    '''
    digits_check = int('1'+''.join(['0' for x in range(1,number_of_digits)]))
    current_number = (ceil(digits_check / number))

    multiples = array('I')
    while len(str(current_number * number)) == number_of_digits:
        multiples.append(current_number * number)
        current_number += 1

    return multiples

def get_least_common_multiple(lower_number: int, higher_number: int) -> int:
    higher_number_multiples = [x * higher_number for x in range(1, lower_number + 1)]
    for multiple in higher_number_multiples:
        if multiple % lower_number == 0:
            return multiple

if __name__ == "__main__":
    find_factors(9)
    # simplify_fractions(2,4)
    # get_n_digit_multiples(4,2)
