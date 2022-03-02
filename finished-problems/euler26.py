"""
FileName: Reciprocal cycles
Author: N.G
Purpose: Find the value of d < 1000 for which 1/d contains
the longest recurring cycle in its decimal fraction part
"""

import time
from math import sqrt

LIMIT = pow(10, 3)


def get_primes(limit: int) -> set:
    """
    returns all primes under a certain limit
    :param limit: the limit to check up to
    :return: a set of all the primes up to the limit
    """
    primes = [True for _ in range(limit + 1)]
    primes[0] = False
    primes[1] = False
    for num in range(1, int(sqrt(limit)) + 1, 2):
        if primes[num]:
            for i in range(num * 2, limit + 1, num):
                primes[i] = False
    all_primes = set(prime for prime in range(1, limit + 1, 2) if primes[prime])
    all_primes.add(2)
    return all_primes


def get_recurring(num: int) -> int:
    """
    gets the length of the recurring decimal of 1 / some number
    :param num: the number to check its recurring decimal length
    :return: the length of the recurring decimal
    """
    length = 1
    curr_mod = 10 % num
    while curr_mod != 1:
        length += 1
        curr_mod = (curr_mod * 10) % num
    return length


def main():
    start = time.time()
    primes = get_primes(LIMIT)
    non_recurring_primes = (2, 5)
    max_recurring_length = 0
    max_recurring_num = 0
    for num in primes:
        if num not in non_recurring_primes:
            curr_recurring = get_recurring(num)
            if curr_recurring > max_recurring_length:
                max_recurring_num = num
                max_recurring_length = curr_recurring
    print(max_recurring_length, max_recurring_num, time.time() - start)


if __name__ == "__main__":
    main()
