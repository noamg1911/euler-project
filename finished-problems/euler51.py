"""
FileName: Prime digit replacements
Author: N.G 7.5.21
Purpose: Find the smallest prime which by replacing part of the number
(not necessarily adjacent digits) with the same digit, is part of an eight prime value family
"""

import time
from euler3 import check_if_prime

FAMILY_SIZE = 8
MIN_VALUE = 56993
REPEAT_TIMES = 3
DIGITS = '0123456789'


def get_repeating_digits(num: int) -> list:
    """
    Gets the repeated digits (specific number of repetitions) in a number
    :param num: The number to check its repetitive digits
    :return: The list of repetitive digits in the number
    """
    str_num = str(num)
    repeating_digits = []
    for digit in set(str_num):
        if str_num.count(digit) == REPEAT_TIMES:
            repeating_digits.append(digit)
    return repeating_digits


def get_family_size(num: int, primes: set) -> bool:
    """
    Gets the size of the family of primes of a number
    family explained in question)
    :param num: The number to check its family (if there's one)
    :param primes: The known set of primes
    :return: A boolean value of whether the family is in the wanted size or not
    """
    list_str_num = list(str(num))
    repeating_digits = get_repeating_digits(num)
    for repeating_digit in repeating_digits:
        curr_family = []
        for digit in DIGITS:
            if list_str_num[0] == repeating_digit and digit == DIGITS[0]:
                continue
            new_list_str_num = [digit if item == repeating_digit else item
                                for item in list_str_num]
            check_num = int(''.join(new_list_str_num))
            if check_num in primes or check_if_prime(check_num):
                curr_family.append(check_num)
                primes.add(check_num)
        if len(curr_family) == FAMILY_SIZE:
            print(curr_family[0])
            return True
    return False


def main():
    start = time.time()
    curr_num = MIN_VALUE
    curr_primes = set()

    while not get_family_size(curr_num, curr_primes):
        curr_num += 2
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
