"""
FileName: Totient permutation
Author: N.G 17.5.21
Purpose: Find the value of n, 1 < n < 10 ** 7, for which φ(n) is a
         permutation of n and the ratio n/φ(n) produces a minimum
"""

import time
from math import sqrt
from euler26 import get_primes

LIMIT = pow(10, 7)


def get_perm_totient(first_prime, second_primes, perms):
    """
    Gets a totient of a number (if it is a permutation of the number)
    and adds their ratio to a dictionary
    :param first_prime: The prime that's less than the root of the limit
    :param second_primes: The primes that are bigger than the root of the limit
    :param perms: The current dictionary of ratios of numbers and their totient
    """
    for second_prime in second_primes:
        if first_prime * second_prime > LIMIT:
            return
        pos_n = first_prime * second_prime
        totient = (first_prime - 1) * (second_prime - 1)
        if sorted(str(pos_n)) == sorted(str(totient)):
            perms[pos_n] = pos_n / totient
            return


def get_middle_index(primes):
    """
    Gets the middle index of primes (that will distinguish between primes
    that are smaller than the root of the limit and bigger than it)
    :param primes: The list of all primes up to some limit
    :return: The index that will cut the list
    """
    root_limit = sqrt(LIMIT)
    curr_index = 0
    while primes[curr_index] <= root_limit:
        curr_index += 1
    return curr_index


def main():
    start = time.time()
    perms = {}

    primes = sorted(get_primes(LIMIT // 2))
    middle_index = get_middle_index(primes)
    first_primes = primes[:middle_index]
    second_primes = primes[middle_index:][:len(first_primes)]

    for first_prime in first_primes:
        get_perm_totient(first_prime, second_primes, perms)

    print(min(perms, key=perms.get))
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
