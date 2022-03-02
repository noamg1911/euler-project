"""
FileName: Consecutive prime sum
Author: N.G 1.5.21
Purpose: Find which prime below one-million can be
written as the sum of the most consecutive primes
"""

import time
from euler26 import get_primes
from euler3 import check_if_prime

LIMIT = pow(10, 6)
MOST_STREAK_MIN = 21


def get_max_prime_index(primes: list) -> int:
    """
    Gets the largest index in the primes list that
    the sum up to it is smaller than the limit
    :param primes: The primes list, up until the specified limit
    :return: The largest index
    """
    max_prime_sum = 0
    curr_index = 0
    while max_prime_sum < LIMIT:
        max_prime_sum += primes[curr_index]
        curr_index += 1
    return curr_index


def get_longest_streak_and_sum(curr_sum: int, max_sum: int,
                               curr_streak: int, max_streak: int) -> tuple:
    """
    Checks if the current sum is prime and the
    current streak is longer than the current longest
    :param curr_sum: The current sum
    :param max_sum: The current maximum prime sum
    :param curr_streak: The current streak
    :param max_streak: The current longest streak
    :return: The longest streak and the largest prime sum
    """
    if check_if_prime(curr_sum) and curr_streak > max_streak:
        max_streak = curr_streak
        max_sum = curr_sum
    return max_streak, max_sum


def main():
    start = time.time()
    primes = sorted(get_primes(LIMIT))
    max_index = get_max_prime_index(primes)
    max_streak = MOST_STREAK_MIN
    max_sum = 0

    for start_prime_index in range(max_index):
        curr_sum = primes[start_prime_index]
        curr_streak = 1
        for end_prime in primes[start_prime_index + 1:
                                max_index + start_prime_index]:
            curr_sum += end_prime
            curr_streak += 1
            if curr_sum > LIMIT:
                curr_sum -= end_prime
                curr_streak -= 1
                max_streak, max_sum =\
                    get_longest_streak_and_sum(curr_sum, max_sum,
                                               curr_streak, max_streak)
                break
            max_streak, max_sum =\
                get_longest_streak_and_sum(curr_sum, max_sum,
                                           curr_streak, max_streak)
    print(max_sum, max_streak)
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
