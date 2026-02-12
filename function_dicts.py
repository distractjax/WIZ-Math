from foundations import basic_factors, basic_fractions, basic_multiples
# This is going to be the holding area for all of my function dicts so I don't end up with an insane
# import statement in my TUI file.

foundations_dict = {
'multiply by fractions': basic_fractions.multiply_fractions_quiz,
'divide by fractions': basic_fractions.divide_fractions_quiz,
'multiply fractions with exponents': basic_fractions.multiply_fractions_with_exponents,
'multiply remainders': basic_fractions.multiply_remainders,
'n-digit multiples': basic_multiples.n_digit_multiples_quiz,
'common n-digit multiples': basic_multiples.common_n_digit_multiples_quiz,
'factor operations': basic_factors.factor_quiz,
'prime factor operations': basic_factors.prime_factor_quiz,
}

category_dict = {
    'Foundations': foundations_dict
}

if __name__ == "__main__":
    basic_fractions.multiply_fractions_quiz()
