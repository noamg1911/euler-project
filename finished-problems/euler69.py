"""
FileName: Totient maximum
Author: N.G 16.5.21
Purpose: Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum
         (Euler's totient function, explained in question)
"""

import time
from euler26 import get_primes
from math import sqrt

LIMIT = pow(10, 6)


def main():
    start = time.time()
    primes = sorted(get_primes(int(sqrt(LIMIT)) + 1))
    curr_max_totient = 1
    for prime in primes:
        curr_max_totient *= prime
        if curr_max_totient > LIMIT:
            curr_max_totient /= prime
            break
    print(int(curr_max_totient))
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
