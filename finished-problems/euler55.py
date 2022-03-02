"""
FileName: Lychrel numbers
Author: N.G 8.5.21
Purpose: Find how many Lychrel numbers are there below ten thousand
"""

import time
from euler4 import check_if_palindrome

LIMIT = 10 ** 4
NUM_ITERATIONS = 50


def check_if_lychrel(num: int) -> bool:
    """
    Checks if a number is lychrel (explained in question)
    :param num: The number to check
    :return: A boolean value of whether the number is lychrel or not
    """
    for iteration in range(NUM_ITERATIONS):
        num += int(str(num)[::-1])
        if check_if_palindrome(str(num)):
            return False
    return True


def main():
    start = time.time()
    num_lychrels = 0
    for num in range(LIMIT + 1):
        num_lychrels += check_if_lychrel(num)
    print(num_lychrels)
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
