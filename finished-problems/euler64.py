"""
FileName: Odd period square roots
Author: N.G 15.5.21
Purpose: Find how many continued fractions for N <= 10000
         have an odd period (explained in question)
"""

import time
from math import sqrt

LIMIT = 10000


def get_period_len(num: int) -> int:
    """
    Gets the length of the repeating period (continued fraction,
    explained in question) of the square root of a number
    :param num: The number to check its square root's period's length
    :return: The length of the period of the square root of the number
    """
    curr_m = 0
    curr_d = 1
    int_part = int(sqrt(num))
    curr_int_part = int_part
    period_len = 0
    if sqrt(num) % 1:
        while curr_int_part != 2 * int_part:
            curr_m = curr_d * curr_int_part - curr_m
            curr_d = (num - pow(curr_m, 2)) / curr_d
            curr_int_part = int((int_part + curr_m) / curr_d)
            period_len += 1
    return period_len


def main():
    start = time.time()
    odd_period_count = 0
    for num in range(LIMIT + 1):
        odd_period_count += get_period_len(num) % 2
    print(odd_period_count)
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
