"""
FileName: Convergents of e
Author: N.G 15.5.21
Purpose: Find the sum of digits in the nominator of the 100th convergent
         of the continued fraction for e
"""

import time

LIMIT = 100


def get_list_period() -> list:
    """
    Gets the list of first LIMIT elements of the period of the
    continuing fraction of e, using a known formula
    :return: The list of the continuing fraction of e
    """
    period_list = [2]
    curr_2_multiple = 2
    while len(period_list) != LIMIT:
        period_list.append(1)
        if not len(period_list) % 3:
            period_list[-1] = curr_2_multiple
            curr_2_multiple += 2
    return period_list


def get_nom_denom_sum_two_num(first_nom: int, first_denom: int,
                              second_nom: int) -> tuple:
    """
    Gets the nominator and denominator of the sum of two fractions
    (second denominator is 1)
    :param first_nom: The nominator of the first number
    :param first_denom: The denominator of the first number
    :param second_nom: The nominator of the second number
    :return: The nominator and denominator of the sum of the two fractions
    """
    nom_sum = first_nom + first_denom * second_nom
    denom_sum = first_denom
    return nom_sum, denom_sum


def main():
    start = time.time()
    e_period_list = get_list_period()
    curr_nom = e_period_list[-1]
    curr_denom = 1

    for period_num in e_period_list[-2::-1]:
        curr_nom, curr_denom = get_nom_denom_sum_two_num(curr_denom, curr_nom,
                                                         period_num)
    nom_sum = sum(list(map(int, str(curr_nom))))
    print(nom_sum)
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
