"""
FileName: Combinatoric selections
Author: N.G 8.5.21
Purpose: Find how many not necessarily distinct values of binomial coefficients
         (n above r) for 1 <= n <= 100, are greater than one million
"""

import time

LIMIT = 100
VALUE_TO_GET = 10 ** 6


def get_factorial_list() -> list:
    """
    Gets a list of factorials up to a certain limit
    :return: The list of factorials up to a certain limit
    """
    factorials = [1] * (LIMIT + 1)
    for num in range(1, LIMIT + 1):
        factorials[num] = factorials[num - 1] * num
    return factorials


def binomial_coefficients_equation(factorials: list, n: int, r: int) -> int:
    """
    Gets the value of he binomial coefficients equation from some n and r
    :param factorials: The list of factorials up to a certain limit
    :param n: The n parameter in the equation (number of elements)
    :param r: The r parameter in the equation (subset number of elements)
    :return: The value of the equation with n and r
    """
    nominator = factorials[n]
    denominator = factorials[r] * factorials[n - r]
    return nominator // denominator


def get_num_rs_for_binomial_above_limit(factorials: list, n: int) -> int:
    """
    Gets for some n the number of rs that give a binomial coefficients
    equation value larger than some limit
    :param factorials: The list of factorials up to a certain limit
    :param n: The specific n in the equation
    :return: The number of rs that give a value larger than the limit
    """
    if factorials[n] < VALUE_TO_GET:
        return 0
    valid_r_count = 0
    for r in range(n + 1):
        if binomial_coefficients_equation(factorials, n, r) >= VALUE_TO_GET:
            valid_r_count += 1
    return valid_r_count


def main():
    start = time.time()
    factorials = get_factorial_list()
    num_values_binomial_coefficients = 0
    for n in range(1, LIMIT + 1):
        valid_r_count = get_num_rs_for_binomial_above_limit(factorials, n)
        num_values_binomial_coefficients += valid_r_count
    print(num_values_binomial_coefficients)
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
