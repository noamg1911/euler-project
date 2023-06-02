"""
Largest Exponential
"""

import time
from math import log10

FILENAME = "./text-files/euler99_text.txt"


def get_exponents_from_file() -> list:
    """
    Gets a list of exponents (a pair of base and power) from a file
    """
    exponents = []
    with open(FILENAME, 'r') as exponents_file:
        for exponent_str_line in exponents_file:
            exponent = tuple(int(str_num) for str_num in exponent_str_line.split(','))
            exponents.append(exponent)
    return exponents


def get_estimated_num_digits_of_exponent(exponent: tuple) -> float:
    """
    Using a cool math trick, gets the number of digits of a very large exponential number using its base and power
    """
    base, power = exponent
    num_digits = power * log10(base)
    return num_digits


def main():
    start = time.time()
    exponents = get_exponents_from_file()
    largest_exponent_line = 0
    largest_exponent_num_digits = 0
    current_line = 0
    for expo in exponents:
        current_line += 1
        current_exponent_num_digits = get_estimated_num_digits_of_exponent(expo)
        if current_exponent_num_digits > largest_exponent_num_digits:
            largest_exponent_num_digits = current_exponent_num_digits
            largest_exponent_line = current_line
    print(largest_exponent_num_digits, largest_exponent_line)
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
