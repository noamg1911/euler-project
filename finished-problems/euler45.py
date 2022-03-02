"""
FileName: Triangular, pentagonal, and hexagonal
Author: N.G 17.4.21
Purpose: Find the next pentagonal number that is also triangular and hexagonal
"""

import time
from math import sqrt
MIN_LIMIT = 40755


def main():
    start = time.time()
    all_num = 0
    pent = 1
    n = 1
    while all_num <= MIN_LIMIT:
        pent += 3 * n + 1
        n += 1
        test_equation = sqrt(8 * pent + 1)
        if test_equation == int(test_equation) and\
                (1 + test_equation) / 4 == (1 + test_equation) // 4:
            all_num = pent
    print(all_num)
    print(time.time() - start)


if __name__ == "__main__":
    main()
