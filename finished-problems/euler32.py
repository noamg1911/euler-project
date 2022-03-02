"""
FileName: Pandigital products
Author: N.G 3.4.21
Purpose: Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital
"""

import time

LENGTH_ID = 9


def main():
    start = time.time()
    max_power = 0

    pandigital_order = '123456789'
    for multiplicand in range(1, LENGTH_ID - 1):
        for multiplier in range(1, LENGTH_ID - 1):
            if len(str(10 ** multiplier) + str(10 ** multiplicand) +
                   str((10 ** multiplicand) * (10 ** multiplier))) == LENGTH_ID:
                max_power = len(str((10 ** multiplicand) * (10 ** multiplier)))

    length_left = LENGTH_ID - max_power
    pandigital_values = set()

    for num in range(2, 10 ** int(length_left / 2) + 1):
        min_range_value = length_left - len(str(num)) - 1
        for pos_divisor in range(10 ** min_range_value, 10 ** (min_range_value + 2)):
            if len(str(num * pos_divisor)) == max_power and \
                    ''.join(sorted(str(num) + str(pos_divisor) + str(num * pos_divisor))) == pandigital_order:
                pandigital_values.add(num * pos_divisor)

    print(sum(pandigital_values))
    print(time.time() - start)


if __name__ == "__main__":
    main()
