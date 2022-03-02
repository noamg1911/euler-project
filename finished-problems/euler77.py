"""
FileName: Prime summations
Author: N.G 28.5.21
Purpose: Find the first value which can be written as the sum of primes
         in over five thousand different ways
"""

import time
from euler3 import check_if_prime

LIMIT = 5000


def main():
    start = time.time()
    primes = []
    curr_num = 1
    known_prime_sums = [1] + [0] * curr_num
    while known_prime_sums[-1] <= LIMIT:
        curr_num += 1
        if check_if_prime(curr_num):
            primes.append(curr_num)
        known_prime_sums = [1] + [0] * curr_num
        for prime in primes:
            for num in range(prime, curr_num + 1):
                known_prime_sums[num] += known_prime_sums[num - prime]

    print(curr_num)
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
