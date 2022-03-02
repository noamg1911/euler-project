"""
FileName: Square root convergents
Author: N.G 13.5.21
Purpose: Find how many fractions contain a numerator with more digits
         than the denominator in the first one-thousand expansions
         of the square root of 2 (Explained in question)
"""

import time

LIMIT = 1000
NOM_BASIC = 2
DENOM_BASIC = 1


def get_nom_denom_sum_two_num(nom: int, denom: int) -> tuple:
    """
    Gets the nominator and denominator of the sum of two numbers (first is 2)
    :param nom: The nominator of the second number
    :param denom: The denominator of the second number
    :return: A tuple of the nominator and denominator of the sum
    """
    nom_sum = NOM_BASIC * denom + DENOM_BASIC * nom
    denom_sum = DENOM_BASIC * denom
    return nom_sum, denom_sum


def who_is_longer(nom: int, denom: int) -> bool:
    """
    Checks which of the nominator and the denominator of a number is longer
    :param nom: The nominator of the number
    :param denom: The denominator of the number
    :return: A boolean value of whether the nominator is longer or not
    """
    return len(str(nom)) > len(str(denom))


def main():
    start = time.time()
    curr_nom = 0
    curr_denom = 1
    total_longer_noms = 0
    for _ in range(LIMIT):
        curr_denom, curr_nom = get_nom_denom_sum_two_num(curr_nom, curr_denom)
        total_longer_noms += who_is_longer(curr_nom + curr_denom, curr_denom)

    print(total_longer_noms)
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
