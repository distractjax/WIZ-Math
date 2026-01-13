# Arithmetic and Number Properties Practice

from math import sqrt, ceil
from functools import reduce

def find_factors(input):
    # This applies list.__add__, the internal method that the list class uses to add elements, to the generator function using reduce
    output = set(reduce(list.__add__,([i, input // i] for i in range(1, ceil(sqrt(input))) if input % i == 0)))
    output = list(output)
    output.sort()
    return output

def main():
    print("Hooray!")
    print(find_factors(10))
    print(max(find_factors(20000)))

if __name__ == "__main__":
    main()
