from random import randint
from math_server.core_math import prime_factorization

# Three problems from the book:
# Cross-multiplication: (sqrt(3) + sqrt(4)) * (sqrt(9) + sqrt(27))
# Different exponent notation (sqrt(3) * 3 ^ 1/2)
# Multiple exponents (sqrt(3) ^ -4)

def root_cross_multiplication_quiz(base: int = 0, num1: int = 0, num2: int = 0):
    '''
    This generates a quiz question about how to cross-multiply square roots.
    '''
    base = base or randint(2,9)
    num1 = num1 or randint(2,9)
    num2 = num2 or randint(2,9)

    if base > 9 or base < 2:
        raise ValueError("base must be between 2 and 9.")
    if num1 > 9 or num1 < 2:
        raise ValueError("num1 must be between 2 and 9.")
    if num2 > 9 or num2 < 2:
        raise ValueError("num2 must be between 2 and 9.")

    soc_base = base ** 2
    exp1 = prime_factorization(soc_base)[0][0]
    exp2 = soc_base // exp1
    root_sign = "\u221A"

    question = f"What is the value of ({root_sign}{exp1} + {num1}{root_sign}{exp2})({num2}{root_sign}{exp1} - {root_sign}{exp2})?"
    answer = ((exp1 * num2) - base + (num1 * num2 * base) - (exp2 * num1))

    return (question, str(answer))


if __name__ == "__main__":
    root_cross_multiplication_quiz()
