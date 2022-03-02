"""
FileName: Ordered fractions
Author: N.G 21.5.21
Purpose: Find the numerator of the fraction immediately to the left of 3/7
         By listing the set of reduced proper fractions for d ≤ 1,000,000
         in ascending order of size
"""

import time

LIMIT = pow(10, 6)
NOMINATOR = 3
DENOMINATOR = 7
MAX_FRACTION = NOMINATOR / DENOMINATOR


def main():
    start = time.time()

    largest_denominator = LIMIT - LIMIT % DENOMINATOR
    largest_nominator = int(largest_denominator / DENOMINATOR * NOMINATOR)
    curr_largest_fraction = (largest_nominator - 1) / largest_denominator
    best_nom = largest_nominator
    best_denom = largest_denominator

    for denom in range(largest_denominator, 1, -1):
        break_check = True
        for nom in range(largest_nominator, 1, -1):
            curr_fraction = nom / denom
            if curr_fraction < curr_largest_fraction:
                break
            if curr_fraction < MAX_FRACTION:
                best_nom = nom
                best_denom = denom
                curr_largest_fraction = best_nom / best_denom
                break_check = False
        if break_check:
            break

    print(best_nom, best_denom)
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
