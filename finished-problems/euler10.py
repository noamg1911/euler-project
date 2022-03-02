"""
FileName: Summation of primes
Author: N.G 29.3.21
Purpose: Find the sum of all the primes below two million
"""

import math
import time
from euler26 import get_primes

LIMIT = 2000000


def main():
    start = time.time()
    print(sum(get_primes(LIMIT)))
    print(time.time() - start)


if __name__ == "__main__":
    main()
