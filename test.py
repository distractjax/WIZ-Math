from math_basics import find_factors

def main():
    solution_numerator = 20
    solution_denominator = 10

    numerator_factors = find_factors(solution_numerator)
    denominator_factors = find_factors(solution_denominator)

    while True:
        if (solution_numerator != 1) and (solution_denominator != 1):
            numerator_factors = find_factors(solution_numerator)
            denominator_factors = find_factors(solution_denominator)

            common_factors = [x for x in numerator_factors if x in denominator_factors]
            print(common_factors)

            if len(common_factors) >= 2:
                solution_numerator = solution_numerator // common_factors[1]
                print(solution_numerator)
                solution_denominator = solution_denominator // common_factors[1]
                print(solution_denominator)

            else:
                print(f'{solution_numerator} / {solution_denominator}')
                break
        else:
            print(f'{solution_numerator} / {solution_denominator}')
            break

if __name__ == "__main__":
    main()
