"""
FileName: Distinct primes factors
Author: N.G 30.4.21
Purpose: Find the first four consecutive integers
to have four distinct prime factors each
"""

import time
import math
from euler3 import check_if_prime

NUM_CONSECUTIVE = 4
MIN_PRIME = 2


def is_distinct_prime_factors(num: int, num_primes: list) -> bool:
    """
    Checks if the number of distinct prime factors of a number
    is the wanted number
    :param num: The number to check its prime factors
    :param num_primes: The list of primes up to the checked number
    :return: Whether the number of the distinct factors is the wanted number
    """
    if check_if_prime(num):
        num_primes.append(num)
        return False

    distinct_factors = set()
    for prime in num_primes:
        if num < prime:
            break
        while not num % prime:
            num //= prime
            distinct_factors.add(prime)
            if check_if_prime(num):
                distinct_factors.add(num)
                return len(distinct_factors) == NUM_CONSECUTIVE
    return len(distinct_factors) == NUM_CONSECUTIVE


def is_consecutive_numbers(num: int, curr_primes: list):
    """
    Checks if the number of conscutive numbers that have some number
    of prime factors is the number of prime factors
    :param num: The number to start the consecutive streak with
    :param curr_primes: The known primes up until that number
    :return: Whether the consecutive number is the same as the prime factors
    number, and the skip number for checking the next number (faster checking)
    """
    for num_step in range(NUM_CONSECUTIVE):
        if not is_distinct_prime_factors(num + num_step, curr_primes):
            return num_step + 1
    return 0


def main():
    start = time.time()
    curr_num = MIN_PRIME
    curr_primes = []
    step_forward = 1

    while step_forward:
        step_forward = is_consecutive_numbers(curr_num, curr_primes)
        curr_num += step_forward

    print(curr_num)
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
