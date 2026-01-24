from foundations.basic_fractions import multiply_fractions_quiz, divide_fractions_quiz, multiply_fractions_with_exponents, multiply_remainders
from foundations.basic_multiples import n_digit_multiples_quiz, common_n_digit_multiples_quiz
from foundations.basic_factors import factor_quiz, prime_factor_quiz
from random import randint
from collections import defaultdict

function_dict = {
'multiply by fractions': multiply_fractions_quiz,
'divide by fractions': divide_fractions_quiz,
'multiply fractions with exponents': multiply_fractions_with_exponents,
'multiply remainders': multiply_remainders,
'n-digit multiples': n_digit_multiples_quiz,
'common n-digit multiples': common_n_digit_multiples_quiz,
'factor operations': factor_quiz,
'prime factor operations': prime_factor_quiz,
}

def function_picker(user_in: str, function_dict: dict[str]):
    user_in = user_in.lower().strip()
    keys = list(function_dict.keys())

    def show_options():
        print('\n'.join(x.title() for x in keys))
        return 1

    def run_random():
        random_key = keys[randint(0,len(keys)-1)]
        function_dict[random_key]()

    def handle_error():
        print("I'm sorry, I didn't understand your input. The options are:\n"+'\n'.join(x.title() for x in keys))
        return 1 

    function_map = defaultdict(lambda: handle_error)
    function_map.update(function_dict)
    function_map['get options'] = show_options
    function_map['random'] = run_random
    function_map['exit'] = lambda: "exit"
    result = function_map[user_in]()

    if result == "exit":
        return

    exit_code = result if isinstance(result, int) else 0
    if exit_code != 1:
        if input('Would you like to go again?\n').lower().strip() == 'no':
            return

    user_in = input('Which would you like to try?\n')
    function_picker(user_in,function_dict)

def main():
    user_in = input('What would you like to do? Type "Get Options" if you want to see all the available functions, or just select "Random" to get started.\nYou can also type "Exit" to quit the program.\n')
    function_picker(user_in, function_dict)

if __name__ == "__main__":
    main()
