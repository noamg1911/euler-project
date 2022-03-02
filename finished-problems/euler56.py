"""
FileName: Powerful digit sum
Author: N.G 13.5.21
Purpose: Find the maximum digital sum of a ** b, where a, b < 100
"""

import time
LIMIT = 100


def get_digital_sum(num):
    """
    Gets the sum of digits of a number
    :param num: The number to calculate its digital sum
    :return: The number's digital sum
    """
    return sum([int(digit) for digit in str(num)])


def main():
    max_digital_sum = 1
    start = time.time()

    for a in range(1, LIMIT):
        for b in range(1, LIMIT):
            curr_digital_sum = get_digital_sum(pow(a, b))
            if curr_digital_sum > max_digital_sum:
                max_digital_sum = curr_digital_sum
    print(max_digital_sum)
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
