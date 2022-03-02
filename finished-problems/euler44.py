"""
FileName: Pentagon numbers
Author: N.G 16.4.21
Purpose: Find the value of D, being the difference of a pair of pentagonal
numbers for which their sum and difference are pentagonal and D is minimised
"""

import time
from math import sqrt


def main():
    start = time.time()
    curr_n = 1
    curr_pent = 1
    min_difference = 0
    while min_difference == 0:
        curr_pent += 3 * curr_n + 1
        check_pent = 1
        for n in range(1, curr_n):
            check_pent += 3 * n + 1
            if sqrt(24 * (curr_pent + check_pent) + 1) % 6 == 5 and\
                    sqrt(24 * (curr_pent - check_pent) + 1) % 6 == 5:
                min_difference = curr_pent - check_pent
                break
        curr_n += 1
    print(min_difference)
    print(time.time() - start)


if __name__ == "__main__":
    main()
