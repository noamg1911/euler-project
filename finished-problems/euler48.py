"""
FileName: Self powers
Author: N.G 30.4.21
Purpose: Find the last ten digits of the sum of 1^1 + 2^2 + ... + 1000^1000
"""

import time

LIMIT = pow(10, 3)
NUM_DIGITS_LAST = 10


def main():
    start = time.time()
    self_power_sum = 0

    for curr_num in range(1, LIMIT + 1):
        self_power_sum += pow(curr_num, curr_num)
    last_digits = str(self_power_sum)[-NUM_DIGITS_LAST:]

    print(last_digits)
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
