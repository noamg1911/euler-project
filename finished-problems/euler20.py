"""
FileName: Factorial digit sum
Author: N.G 29.3.21
Purpose: Find the sum of the digits in the number 100!
"""

NUMBER = 100


def factorial(num):
    """
    gets the factorial of a number
    :param num: the number to calculate its factorial
    :return: the factorial of the number that was given
    """
    factorial_answer = 1
    for i in range(num, 1, -1):
        factorial_answer *= i
    return factorial_answer


def main():
    print(sum([int(digit) for digit in str(factorial(NUMBER))]))


if __name__ == "__main__":
    main()
