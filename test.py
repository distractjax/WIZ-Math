from math_basics import find_factors

def main():
    solution_numerator = 20
    solution_denominator = 10

    numerator_factors = find_factors(solution_numerator)
    denominator_factors = find_factors(solution_denominator)

    while True:
        common_factors = [x for x in numerator_factors if x in denominator_factors]
        print(common_factors)
        break

if __name__ == "__main__":
    main()
