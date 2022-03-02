"""
FileName: Square root digital expansion
Author: N.G 4.6.21
Purpose: Find the total of the digital sums of the first one hundred
         decimal digits of all the irrational square roots for the first
         one hundred natural numbers
"""
# Can be done with importing decimal, but I want a more mathematical way

import time
from decimal import *
from math import sqrt

LIMIT = 100
DEFAULT_B = 5


def easy_answer():
    """
    The easy answer, uses a library for precision point floats (cheating)
    """
    start = time.time()
    getcontext().prec = LIMIT + 2
    sum_digits = 0
    for num in range(1, LIMIT + 1):
        if sqrt(num) % 1:
            str_digits = str(Decimal(num).sqrt())
            sum_digits += int(sqrt(num)) + sum(map(int, str_digits[2:-2]))

    print(sum_digits)
    print(f"Solution took {time.time() - start} seconds!")


def get_sum_num_sqrt(num: int) -> int:
    """
    Gets the sum of the first 101 digits of a number's square root
    :param num: The number to get the sum of its square root's digits
    :return: The sum of the root's digits
    """
    a = 5 * num
    b = DEFAULT_B
    while len(str(b)) < LIMIT + 2:
        if a >= b:
            a -= b
            b += 10
        else:
            a *= 100
            b = (b - DEFAULT_B) * 10 + DEFAULT_B
    return sum(map(int, str(b))) - DEFAULT_B


def main():
    start = time.time()
    sum_digits = 0
    for num in range(1, LIMIT + 1):
        if sqrt(num) % 1:
            sum_digits += get_sum_num_sqrt(num)

    print(sum_digits)
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
