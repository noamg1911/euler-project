"""
FileName: Quadratic primes
Author: N.G 31.3.21
Purpose: Find the product of the coefficients, a and b, for the quadratic expression
that produces the maximum number of primes for consecutive values of n (n^2 + an + b), starting with n = 0
"""

import time

LIMIT = 10 ** 3
HIGHEST_KNOWN_N = 39


def check_if_prime(num: int) -> bool:
    """
    checks if a number is prime
    :param num: the number to be checked
    :return: True if it's prime, False otherwise
    (if divisible by any number up to the checked number's root)
    """
    if num <= 3:
        return num > 1
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, int(num ** 0.5 + 1), 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True


def main():
    start = time.time()
    longest_a = 0
    longest_b = 0
    longest_n = 0
    possible_bs = [x for x in range(1, LIMIT + 1) if check_if_prime(x)]
    possible_as = [x for x in range(-LIMIT + 1, LIMIT + 1)]

    for a in possible_as:
        for b in possible_bs:
            curr_n = 0
            while check_if_prime(curr_n ** 2 + a * curr_n + b):
                curr_n += 1
            if curr_n > longest_n:
                longest_n = curr_n
                longest_a = a
                longest_b = b
    print(longest_a, longest_b, longest_n)
    print(time.time() - start)


if __name__ == "__main__":
    main()
