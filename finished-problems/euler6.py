"""
FileName: Sum square difference
Author: N.G 28.3.21
Purpose: Find the difference between the
sum of the squares of the first one hundred natural numbers and the square of the sum
"""

import time
LIMIT = 100


def main():
    start = time.time()
    sum_squares = sum([x ** 2 for x in range(LIMIT + 1)])
    square_sum = ((LIMIT + 1) * LIMIT / 2) ** 2
    print(int(square_sum - sum_squares))
    print(time.time() - start)


if __name__ == "__main__":
    main()
