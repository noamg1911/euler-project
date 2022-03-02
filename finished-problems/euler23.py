"""
FileName: Non-abundant sums
Author: N.G 30.3.21
Purpose: Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers
"""

import time
LIMIT = 28124


def is_abundant(num: int) -> bool:
    """
    checks if a number is an abundant number
    :param num: the number to be checked
    :return: True if it is, False otherwise
    """
    divisor_sum = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divisor_sum += i
            if num / i != i:
                divisor_sum += num / i
    return int(divisor_sum) > num


def is_sum_of_abundant(num: int, set_abundant: set) -> bool:
    """
    returns whether a number is a sum of two abundant numbers
    :param num: the number to be checked
    :param set_abundant: the set of known abundant numbers (up until the checked number)
    :return: True if it is, False otherwise
    """
    for abundant in set_abundant:
        if num - abundant in set_abundant:
            return True
    return False


def main():
    start = time.time()
    abundant_numbers = set()
    sum_not_two_abundant = 0
    for num in range(1, LIMIT):
        if is_abundant(num):
            abundant_numbers.add(num)
        if not is_sum_of_abundant(num, abundant_numbers):
            sum_not_two_abundant += num
    print(sum_not_two_abundant, time.time() - start)


if __name__ == "__main__":
    main()
