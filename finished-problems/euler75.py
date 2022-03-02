"""
FileName: Singular integer right triangles
Author: N.G 22.5.21
Purpose: Find how many values of L ≤ 1,500,000 can exactly one integer sided
         right angle triangle be formed, Given that L is the perimeter of the
         triangle
"""

import time
from math import gcd

LIMIT = int(pow(10, 6) * 1.5)
MAX_M = 865


def get_pythagoras_sums(m: int, n: int) -> list:
    """
    Gets all the sums of a primitive pythagorean sum, using Euclid's equation
    :param m: The first parameter in Euclid's equation
    :param n: The second parameter in Euclid's equation
    :return: The list of pythagorean triangle's lengths
    """
    first_sum = 2 * m * (m + n)
    curr_sum = first_sum
    sums = []
    while curr_sum <= LIMIT:
        sums.append(curr_sum)
        curr_sum += first_sum
    return sums


def main():
    start = time.time()
    single_sum_lengths = set()
    multi_sum_lengths = set()

    for m in range(2, MAX_M + 1):
        starting_num = 2 if m % 2 else 1
        for n in range(starting_num, m, 2):
            if n > 1 and gcd(m, n) != 1:
                continue
            curr_pythagoras_sums = get_pythagoras_sums(m, n)
            for pythagoras_sum in curr_pythagoras_sums:
                if pythagoras_sum in multi_sum_lengths:
                    continue
                if pythagoras_sum in single_sum_lengths:
                    single_sum_lengths.remove(pythagoras_sum)
                    multi_sum_lengths.add(pythagoras_sum)
                else:
                    single_sum_lengths.add(pythagoras_sum)

    print(len(single_sum_lengths))
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
