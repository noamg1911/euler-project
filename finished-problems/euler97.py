"""
Large Non-Mersenne Prime
"""

import time


def main():
    start = time.time()
    large_prime = (28433 << 7830457) + 1
    num_digits_to_get = 10
    last_digits = large_prime % 10 ** num_digits_to_get
    print(last_digits)
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
