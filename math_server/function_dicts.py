from math_server.foundations import basic_factors, basic_fractions, basic_multiples, digit_reversals

foundations_dict = {
    'multiply by fractions': basic_fractions.multiply_fractions_quiz,
    'divide by fractions': basic_fractions.divide_fractions_quiz,
    'multiply fractions with exponents': basic_fractions.multiply_fractions_with_exponents,
    # This is going to get added back in after I split the TUI event loop into two
    # 'multiply remainders': basic_fractions.multiply_remainders,
    'n-digit multiples': basic_multiples.n_digit_multiples_quiz,
    'common n-digit multiples': basic_multiples.common_n_digit_multiples_quiz,
    'factor operations': basic_factors.factor_quiz,
    'prime factor operations': basic_factors.prime_factor_quiz,
    'digit reversals': digit_reversals.int_reversal_quiz,
}

category_dict = {
    'Foundations': foundations_dict,
}

# This is just to test my imports
if __name__ == "__main__":
    basic_fractions.multiply_fractions_quiz()
