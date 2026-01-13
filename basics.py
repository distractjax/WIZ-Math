from math import sqrt, ceil
from functools import reduce
from array import array, ArrayType
from random import randrange, randint
# from myfractions import multiply_by_fractions, divide_by_fractions

# Core Functions

# Math Functions

def find_factors(input: int) -> array[int]:
    '''
    Generates a sorted array of all a given number's factors.
    '''
    # This applies list.__add__, the internal method that the list class uses to add elements, to the generator function using reduce
    output = set(reduce(list.__add__,([i, input // i] for i in range(1, ceil(sqrt(input))) if input % i == 0)))
    output = array('I',sorted(output))
    return output

def multiply_by_result(input: int) -> int:
    '''
    Returns two numbers that multiply to create the result.
    '''
    factors = find_factors(input)
    index_int = randrange(len(factors) // 2)
    factor1, factor2 = factors[index_int], factors[-index_int - 1]
    return factor1, factor2
