from math import sqrt, ceil
from functools import reduce
from array import array, ArrayType
from random import randint

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
def simplify_fractions(numerator: int, denominator: int) -> tuple[int, int]:
    '''
    This returns the most simplified version of a given fraction.
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
    Generates a sorted array of the multiples of a number that are n-number of digits
    '''
    digits_check = int('1'+''.join(['0' for x in range(1,number_of_digits)]))
    multiple = (ceil(digits_check / number))
    digits_check *= 10

    multiples = array('I')
    while multiple * number < digits_check:
        multiples.append(multiple * number)
        multiple += 1

    return multiples

def get_least_common_multiple(lower_number: int, higher_number: int) -> int:
    '''
    This function returns the lowest common multiple between two numbers.
    '''
    higher_number_multiples = [x * higher_number for x in range(1, lower_number + 1)]
    for multiple in higher_number_multiples:
        if multiple % lower_number == 0:
            return multiple
    return 0

def get_greatest_common_factor(lower_number: int, higher_number: int) -> int:
    '''
    This function returns the greatest common factor between two numbers.
    '''
    higher_number_factors = find_factors(higher_number)
    for factor in higher_number_factors[::-1]:
        if lower_number % factor == 0:
            return factor
    return 0

def is_power_of_two(num):
    # This uses some bit manipulation. The first argument checks if num == 0 and the second checks if the binary of a number (say 4, which in 8-bit would be 00000100) minus the binary of the number one less than it ( which here would be 00000011) is equal to 0 (00000000).
    return (num != 0) and (num & (num - 1) == 0)

def prime_factorization(num):
    '''
    This returns the prime factors with exponents of a given number.
    '''
    if num < 2:
        return []

    factors = {}

    while 0 == num % 2:
        factors[2] = factors.get(2,0) + 1
        num //= 2

    divisor = 3
    while divisor * divisor <= num:
        while 0 == num % divisor:
            factors[divisor] = factors.get(divisor, 0) + 1
            num //= divisor
        divisor += 2

    if num > 2:
        factors[num] = 1

    return list(factors.items())

def simplify_exponents(num):
    '''
    This simplies any number that is the power of another number down to itself raised by an exponent.
    '''
    if num <= 3:
        return num, 1

    prime_factors = dict(prime_factorization(num))
    exponents = list(prime_factors.values())
    common_exponent = reduce(get_greatest_common_factor, exponents)

    new_base = 1
    for p, e in prime_factors.items():
        new_base *= (p ** (e // common_exponent))
    
    return new_base, common_exponent


if __name__ == "__main__":
    find_factors(9)
    # simplify_fractions(2,4)
    # get_n_digit_multiples(4,2)
    # print(is_power_of_two(28))
