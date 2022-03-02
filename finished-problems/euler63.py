"""
FileName: Powerful digit counts
Author: N.G 14.5.21
Purpose: Find how many n-digit integers exist which are also an nth power
"""

import time

BASE_LIMIT = 10


def is_pow_nums_equal_pow(power: int) -> bool:
    """
    Checks if a power n has an n digit number which is also an nth power
    :param power: The power to check
    :return: A boolean value of whether the power has such a number
    """
    for num in range(1, BASE_LIMIT):
        if len(str(pow(num, power))) == power:
            return True
    return False


def get_pow_limit() -> int:
    """
    Gets the maximum power n which has an n digit number which
    is also an nth power
    :return: The highest power that has that condition
    """
    curr_pow = 1
    while is_pow_nums_equal_pow(curr_pow):
        curr_pow += 1
    return curr_pow - 1


def main():
    start = time.time()
    pow_limit = get_pow_limit()
    num_of_ints_equal_power = 0
    for power in range(1, pow_limit + 1):
        for num in range(1, BASE_LIMIT + 1):
            len_power = len(str(pow(num, power)))
            if len_power == power:
                num_of_ints_equal_power += 1
    print(num_of_ints_equal_power)
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
