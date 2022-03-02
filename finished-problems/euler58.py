"""
FileName: Spiral primes
Author: N.G 13.5.21
Purpose: Find the side length of the square spiral (explained in question)
         for which the ratio of primes along the diagonals is first below 10%
"""

import time
from euler3 import check_if_prime

PRIME_FRACTION = 0.1
NUM_SIDES = 4


def main():
    start = time.time()
    difference = 2
    curr_num = 1
    total_diagonal_primes = 0
    curr_prime_fraction = 0

    while curr_prime_fraction > PRIME_FRACTION or total_diagonal_primes == 0:
        for _ in range(NUM_SIDES):
            curr_num += difference
            total_diagonal_primes += check_if_prime(curr_num)
        difference += 2
        curr_prime_fraction = total_diagonal_primes / (2 * difference - 1)
    print(difference - 1)
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
