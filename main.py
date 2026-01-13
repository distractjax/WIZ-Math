# Arithmetic and Number Properties Practice

from fractions import multiply_by_fractions
from fractions import divide_by_fractions
from basics import function_picker


def main():
    input1 = input('What would you like to do? Type "Get Options" if you want to see all the available functions, or just select "Random" to get started.')
    function_picker(input1)

if __name__ == "__main__":
    main()
