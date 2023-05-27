"""
Concealed Square
"""

import time
from math import sqrt, ceil, floor

DIGITS = [1, 2, 3, 4, 5, 6, 7, 8, 9]
MIN_NUM = 1020304050607080900
MAX_NUM = 1929394959697989990


def check_if_num_is_in_format(num: int):
    """
    Checks if a number is of the format 1_2_3_4_5_6_7_8_9_0, where each _ is a digit.
    """
    if num % 100:
        return False
    num //= 100
    for digit in DIGITS[::-1]:
        if num % 10 != digit:
            return False
        num //= 100
    return True


def main():
    start = time.time()
    min_num = floor(sqrt(MIN_NUM))
    max_num = ceil(sqrt(MAX_NUM))
    for num in range(min_num, max_num, 10):
        checked_num = num ** 2
        if check_if_num_is_in_format(checked_num):
            print(num, checked_num)
            break
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
