# Arithmetic and Number Properties Practice

from math import sqrt, ceil
from functools import reduce
from array import array, ArrayType

def find_factors(input: int) -> array[int]:
    '''
    Generates a sorted array of all a given number's factors.
    '''
    # This applies list.__add__, the internal method that the list class uses to add elements, to the generator function using reduce
    output = set(reduce(list.__add__,([i, input // i] for i in range(1, ceil(sqrt(input))) if input % i == 0)))
    output = array('I',sorted(output))
    return output

def divide_by_fractions(input: int) -> str:
    '''
    Generates a string that divides two fractions made of up a given number's factors.
    '''
    factors = find_factors(input)


def main():
    print("Hooray!")
    print(find_factors(10))
    factors = find_factors(10)
    print(factors[3])

if __name__ == "__main__":
    main()
