"""
Prime Power Triples
"""

import time
from math import sqrt
from euler26 import get_primes

LIMIT = 50000000


def main():
    start = time.time()
    prime_limit = int(sqrt(LIMIT))
    primes = sorted(get_primes(prime_limit))
    prime_power_triples = set()
    for a in primes:
        for b in primes:
            for c in primes:
                power_triple = a ** 2 + b ** 3 + c ** 4
                if power_triple < LIMIT:
                    prime_power_triples.add(power_triple)
                else:
                    break
    print(len(prime_power_triples))
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
