"""
FileName: Digit cancelling fractions
Author: N.G
Purpose: Find the value of the denominator if the product of the four fractions is given in its lowest common terms
"""

import time
from euler7 import check_if_prime

UPPER_LIMIT = 10 ** 2 - 1
LOWER_LIMIT = 10
LENGTH_NUM = 2


def main():
    start = time.time()
    final_nom = 1
    final_de = 1

    for nom in range(LOWER_LIMIT, UPPER_LIMIT + 1):
        curr_nom = str(nom)
        for denom in range(nom + 1, UPPER_LIMIT + 1):
            if nom // 10 == denom // 10 or nom % 10 == 0 or denom % 10 == 0:
                continue
            curr_de = str(denom)
            for i in range(LENGTH_NUM):
                other_i = LENGTH_NUM - 1
                if curr_nom[i] in curr_de and \
                        int(curr_nom[other_i - i]) / \
                        int(curr_de[other_i - curr_de.index(curr_nom[i])]) == nom / denom:
                    final_nom *= int(curr_nom[other_i - i])
                    final_de *= int(curr_de[other_i - curr_de.index(curr_nom[i])])

    if final_de % final_nom == 0:
        final_de /= final_nom
        final_nom = 1
    while final_nom != 1 and not check_if_prime(final_de):

        for num in range(1, int(final_nom ** 0.5) + 1):
            if final_nom % num == 0:
                final_nom /= num
                final_de /= num

    print(int(final_de))
    print(time.time() - start)


if __name__ == "__main__":
    main()
