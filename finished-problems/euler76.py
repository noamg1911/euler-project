"""
FileName: Counting summations
Author: N.G 28.5.21
Purpose: Find how many different ways can one hundred be written
         as a sum of at least two positive integers
"""

import time

LIMIT = 100


def main():
    start = time.time()
    num_combinations = [1] + [0] * LIMIT
    for first in range(1, LIMIT + 1):
        for second in range(first, LIMIT + 1):
            num_combinations[second] += num_combinations[second - first]
    print(num_combinations[LIMIT] - 1)
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
