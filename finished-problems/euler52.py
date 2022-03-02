"""
FileName: Permuted multiples
Author: N.G 8.5.21
Purpose: Find the smallest positive integer that its
         first 6 multiples contain the same digits
"""

import time

MULTIPLE_NUM = 6


def contain_same_digits(first_num: int, second_num: int) -> bool:
    """
    checks if two numbers are permutations of each other
    :param first_num: The first number
    :param second_num: The second numbers
    :return: A boolean value of whether the two numbers
             are permutations of each other
    """
    str_first = str(first_num)
    str_second = str(second_num)
    first_digits = set(str_first)
    second_digits = set(str_second)

    if len(first_digits) != len(second_digits) or \
       len(str_first) != len(second_digits):
        return False
    for digit in first_digits:
        if str_first.count(digit) != str_second.count(digit):
            return False
    return True


def check_multiples_contain_same_digits(num: int) -> bool:
    """
    checks if a number's multiples are permutations of the number
    :param num: The number to check
    :return: A boolean value of whether the number's multiples
             are permutations of the number
    """
    for multiple in range(2, MULTIPLE_NUM + 1):
        if not contain_same_digits(num, num * multiple):
            return False
    return True


def main():
    start = time.time()
    curr_num = 1

    while not check_multiples_contain_same_digits(curr_num):
        curr_num += 1

    print(curr_num)
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
