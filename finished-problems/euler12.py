"""
FileName: Highly divisible triangular number
Author: N.G 29.3.21
Purpose: Find the value of the first triangle number to have over five hundred divisors
"""

import time

DIVISORS = 500


def main():
    start = time.time()
    curr_num = 1
    curr_sum = 1
    while not len([num for num in range(1, int(curr_sum ** 0.5 + 1)) if curr_sum % num == 0] * 2) >= DIVISORS:
        curr_sum += curr_num + 1
        curr_num += 1
    print(curr_num - 1)
    print(curr_sum)
    print(time.time() - start)


if __name__ == "__main__":
    main()
