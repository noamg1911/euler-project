"""
FileName: Counting fractions
Author: N.G 21.5.21
Purpose: Find how many elements would be contained in the
         set of reduced proper fractions for d ≤ 1,000,000
"""

import time

LIMIT = pow(10, 6)


def main():
    start = time.time()
    num_list = list(range(LIMIT + 1))

    for num in range(2, LIMIT // 2 + 1):
        if num == num_list[num]:
            for multiple in range(num, LIMIT + 1, num):
                num_list[multiple] *= ((num - 1) / num)
    for num in range(LIMIT // 2 + 1, LIMIT + 1):
        if num == num_list[num]:
            num_list[num] -= 1
    num_reduced_fractions = int(sum(num_list) - 1)

    print(num_reduced_fractions)
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
