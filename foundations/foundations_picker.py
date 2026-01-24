from .basic_fractions import multiply_fractions_quiz, divide_fractions_quiz, multiply_fractions_with_exponents, multiply_remainders
from .basic_multiples import n_digit_multiples_quiz, common_n_digit_multiples_quiz
from .basic_factors import factor_quiz, prime_factor_quiz
from math_basics import function_picker

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

def foundations_function_picker():
    user_in = input('What Foundations concept would you like to practice?\n')
    function_picker(user_in,function_dict)
