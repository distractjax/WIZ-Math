from random import randint, getrandbits

def int_reversal_quiz(num1: int = 0, num2: int = 0) -> tuple[str, str]:
    num1 = num1 or randint(1,9)
    num2 = num2 or randint(1,9)

    if num1 > 9 or num1 < 1:
        raise ValueError("num1 must be between 1 and 9.")
    if num2 > 9 or num2 < 1:
        raise ValueError("num2 must be between 1 and 9.")

    final_num = num1 * 1001 + num2 * 110

    question = f"When the digits of a number are inverted and added to itself, the result is {final_num}. What is the smallest possible value of that number?"

    answer = str(1000 + num2 * 10 + num1 - 1)

    return (question, answer)

if __name__ == "__main__":
    print(int_reversal_quiz())
