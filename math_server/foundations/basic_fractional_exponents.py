from random import randint
from math_server.core_math import prime_factorization
from math import lcm
from fractions import Fraction

# Three problems from the book:
# Cross-multiplication: (sqrt(3) + sqrt(4)) * (sqrt(9) + sqrt(27))
# Different exponent notation (sqrt(3) * 3 ^ 1/2)
# Multiple exponents (sqrt(3) ^ -4)

def root_cross_multiplication_quiz(base: int = 0, num1: int = 0, num2: int = 0) -> tuple[str, str]:
    '''
    This generates a quiz question about how to cross-multiply square roots.
    '''
    base = base or randint(2,9)
    num1 = num1 or randint(2,9)
    num2 = num2 or randint(2,9)

    if base > 9 or base < 2:
        raise ValueError('base must be between 2 and 9.')
    if num1 > 9 or num1 < 2:
        raise ValueError('num1 must be between 2 and 9.')
    if num2 > 9 or num2 < 2:
        raise ValueError('num2 must be between 2 and 9.')

    soc_base = base ** 2
    exp1 = prime_factorization(soc_base)[0][0]
    exp2 = soc_base // exp1
    root_sign = '\u221A'

    question = f'What is the value of ({root_sign}{exp1} + {num1}{root_sign}{exp2})({num2}{root_sign}{exp1} - {root_sign}{exp2})?'
    answer = ((exp1 * num2) - base + (num1 * num2 * base) - (exp2 * num1))

    return (question, str(answer))

def root_formatting_multiplication_quiz(base: int = 0, num1: int = 0, num2: int = 0, num1_exp: int = 0, num2_exp: int = 0) -> tuple[str, str]:
    '''
    This generates a quiz question about how to multiply fractional exponents with a common denominator.
    '''
    base = base or randint(2,9)
    num1 = num1 or randint(2,9)
    num2 = num2 or randint(2,9)
    num1_exp = num1_exp or randint(2,4)
    num2_exp = num2_exp or randint(2,4)

    if base > 9 or base < 2:
        raise ValueError('base must be between 2 and 9.')
    if num1 > 9 or num1 < 2:
        raise ValueError('num1 must be between 2 and 9.')
    if num2 > 9 or num2 < 2:
        raise ValueError('num2 must be between 2 and 9.')
    if num1_exp > 4 or num1_exp < 2:
        raise ValueError('num1_exp must be between 2 and 4.')
    if num2_exp > 4 or num2_exp < 2:
        raise ValueError('num2_exp must be between 2 and 4.')

    if num1_exp == num2_exp:
        return root_formatting_multiplication_quiz(
            base = base,
            num1 = num1,
            num2 = num2,
            num1_exp = num1_exp + 1 if num1_exp != 4 else 3,
            num2_exp = num2_exp
        )

    base_exp_d = lcm(num1_exp, num2_exp)
    # This is how I'm converting the exponents to fractions for a moment.
    # This just solves an edge case that pops up when num1 = 2 and num2 = 4.
    base_exp_n = base_exp_d - (num1_exp + num2_exp)
    base_exp = Fraction(base_exp_n,base_exp_d)

    root_signs = ['\u221A','\u221B','\u221C']
    num1_sign = root_signs[num1_exp - 2]
    num2_sign = root_signs[num2_exp - 2]

    num1_prod = num1 ** num1_exp
    num2_prod = num2 ** num2_exp

    question = f'What is the value of {num1_sign}{num1_prod * base} x {num2_sign}{num2_prod * base} x {base}^{base_exp}'
    answer = f'{num1 * num2 * base}'

    return (question, str(answer))

if __name__ == '__main__':
    # print(root_cross_multiplication_quiz())
    print(root_formatting_multiplication_quiz(7,3,2,4,4))
