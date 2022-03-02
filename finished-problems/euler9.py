"""
FileName: Special Pythagorean triplet
Author: N.G 29.3.21
Purpose: Find the product of the Pythagorean triplet abc for which a + b + c = 1000.
"""

import math
import time
SUM = 1000
HIGHEST_C = SUM - 3
LOWEST_C = 5


def main():
    start = time.time()
    for c in range(HIGHEST_C, LOWEST_C, -1):
        for b in range(SUM - c - 1, 1, -1):
            a = SUM - c - b
            if c == math.sqrt(b ** 2 + a ** 2):
                print(a * b * c)
                print(time.time() - start)
                return


if __name__ == "__main__":
    main()
