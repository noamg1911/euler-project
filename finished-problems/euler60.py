"""
FileName: Prime pair sets
Author: N.G 13.5.21
Purpose: Find the lowest sum for a set of five primes for which
         any two primes concatenate to produce another prime
"""

import time
from euler3 import check_if_prime
from euler26 import get_primes

NUM_PRIMES = 5


def concatenate_numbers(first_num: int, second_num: int) -> int:
    """
    Concatenates two numbers and returns the value
    :param first_num: The first number (first half of concatenation)
    :param second_num: The second number (second half of concatenation)
    :return: The value of the concatenated number
    """
    con_str = str(first_num) + str(second_num)
    return int(con_str)


def check_primes_concatenate_to_prime(first_num: int, second_num: int) -> bool:
    """
    Checks if the two variations of concatenations of two numbers are prime
    :param first_num: The first number
    :param second_num: The second number
    :return: A boolean value of whether both of the variations are prime
    """
    first_con = concatenate_numbers(first_num, second_num)
    second_con = concatenate_numbers(second_num, first_num)
    return check_if_prime(first_con) and check_if_prime(second_con)


def check_concat_for_curr_prime(curr_prime: int, pos_primes: list) -> bool:
    """
    Checks if a prime has the concatenation property with a list of some primes
    :param curr_prime: The prime to check if it has the property
    :param pos_primes: The primes to check if they share the property
    :return: A boolean value of whether the prime has the property with the
             list of primes or not
    """
    for prime in pos_primes:
        if not check_primes_concatenate_to_prime(curr_prime, prime):
            return False
    return True


def get_all_primes_that_concatenate(primes: list, curr_primes: list) -> list:
    """
    Gets a list of a specified size of primes that all have
    the concatenation property with each other
    :param primes: The list of primes to check with for the rest of the list
    :param curr_primes: The primes that are currently in the property list
    :return: The list itself, either not full (recursive) or in the end, full
    """
    relevant_curr_primes = [prime for prime in curr_primes if prime]
    con_primes = []
    for i in range(len(primes)):
        if check_concat_for_curr_prime(primes[i], relevant_curr_primes):
            con_primes.append(primes[i])
    if not con_primes:
        curr_primes[len(relevant_curr_primes) - 1] = 0

    for index in range(len(con_primes)):
        curr_primes[len(relevant_curr_primes)] = con_primes[index]
        if curr_primes[NUM_PRIMES - 1]:
            break
        curr_primes = get_all_primes_that_concatenate(con_primes[index + 1:],
                                                      curr_primes)
        if curr_primes[NUM_PRIMES - 1]:
            break
    return curr_primes


def main():
    start = time.time()
    curr_limit = 100
    curr_primes = sorted(get_primes(curr_limit))
    primes_found = [0] * NUM_PRIMES

    while not primes_found[NUM_PRIMES - 1]:
        for i in range(1, len(curr_primes)):
            primes_found[0] = curr_primes[i]
            primes_found = get_all_primes_that_concatenate(curr_primes[i + 1:],
                                                           primes_found)
            if primes_found[NUM_PRIMES - 1]:
                break
            if not primes_found[NUM_PRIMES - 1] and i == len(curr_primes) - 1:
                curr_limit *= 10
                curr_primes = sorted(get_primes(curr_limit))

    print(primes_found, sum(primes_found))
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
