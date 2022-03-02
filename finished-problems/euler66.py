"""
FileName: Diophantine equation
Author: N.G 15.5.21
Purpose: Find the value of D ≤ 1000 in minimal solutions of x for which
         the largest value of x is obtained in the quadratic Diophantine
         equation (explained in question)
"""

import time
from math import sqrt
from euler65 import get_nom_denom_sum_two_num

LIMIT = 1000


def get_curr_fraction(continuing_fraction_list: list) -> tuple:
    """
    Gets the current fraction from a number's continuing fraction list
    :param continuing_fraction_list: The continuing fraction list of a number
    :return: The nominator and denominator of the fraction from the list
    """
    curr_nom = continuing_fraction_list[-1]
    curr_denom = 1
    for fraction_num in continuing_fraction_list[-2::-1]:
        curr_nom, curr_denom = get_nom_denom_sum_two_num(curr_denom, curr_nom,
                                                         fraction_num)
    return curr_nom, curr_denom


def get_first_x(num: int) -> int:
    """
    Gets the x parameter in the smallest solution of the
    Diophantine equation for some number (D)
    :param num: The number in the equation (D)
    :return: The x in the smallest solution of the equation
    """
    curr_m = 0
    curr_d = 1
    int_part = int(sqrt(num))
    curr_int_part = int_part
    continuing_fraction = [int_part]
    first_x = 0

    while not first_x:
        curr_m = curr_d * curr_int_part - curr_m
        curr_d = (num - pow(curr_m, 2)) / curr_d
        curr_int_part = int((int_part + curr_m) / curr_d)
        continuing_fraction.append(curr_int_part)
        pos_x, pos_y = get_curr_fraction(continuing_fraction)
        if pow(pos_x, 2) - num * pow(pos_y, 2) == 1:
            first_x = pos_x
    return first_x


def main():
    start = time.time()
    max_x = 1
    max_d = 1
    for constant in range(1, LIMIT + 1):
        if sqrt(constant) % 1:
            curr_x = get_first_x(constant)
            if curr_x > max_x:
                max_x = curr_x
                max_d = constant
    print(max_d)
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
