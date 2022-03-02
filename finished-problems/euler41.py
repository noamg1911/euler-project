"""
FileName: Pandigital prime
Author: N.G 10.4.21
Purpose: Find the largest n-digit pandigital prime that exists
"""

import time
from euler3 import check_if_prime
LIMIT = 10 ** 9
NUM_DIGITS = 9


def main():
    start = time.time()

    good_lengths = []
    curr_sum = 1
    for num in range(2, NUM_DIGITS + 1):
        curr_sum += num
        if curr_sum % 3 != 0:
            good_lengths.append(num)

    pandigital_order = '123456789'
    largest_pan_prime = 0
    for length in good_lengths[::-1]:
        max_limit = ''
        for digit in range(length, 0, -1):
            max_limit += str(digit)
        min_limit = max_limit[::-1]
        for num in range(int(max_limit), int(min_limit), -1):
            if ''.join(sorted(str(num))) == pandigital_order[:length] and\
                    check_if_prime(num):
                largest_pan_prime = num
                break
        if largest_pan_prime > 0:
            break
    print(largest_pan_prime)
    print(time.time() - start)


if __name__ == "__main__":
    main()
