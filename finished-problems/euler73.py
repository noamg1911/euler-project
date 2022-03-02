"""
FileName: Counting fractions in a range
Author: N.G 21.5.21
Purpose: Find how many fractions lie between 1/3 and 1/2 in the
         sorted set of reduced proper fractions for d ≤ 12,000
"""

import time

LIMIT = 12000


def main():
    start = time.time()
    curr_nums = set()

    for nom in range(1, LIMIT // 2 + 1):
        for denom in range(nom * 2 + 1, nom * 3):
            if denom > LIMIT:
                break
            curr_nums.add(nom / denom)

    print(len(curr_nums))
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
