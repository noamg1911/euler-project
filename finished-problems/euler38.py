"""
FileName: Pandigital multiples
Author: N.G 9.4.21
Purpose: Find the largest 1 to 9 pandigital 9-digit number that can be formed
as the concatenated product of an integer with (1,2, ... , n) where n > 1
"""

import time
CURRENT_LARGEST = 918273645
NUM_LENGTH = 9
DIGITS = '123456789'


def main():
    start = time.time()
    largest_pandigital = 0
    largest_num = 1
    while len(str(largest_num)) < NUM_LENGTH // 2 + 1:
        largest_num *= 10

    for num in range(int(str(CURRENT_LARGEST)[0]), largest_num):
        total_length = 0
        curr_multiplier = 1
        pos_pandigital = ''
        while total_length < NUM_LENGTH:
            curr_product = str(num * curr_multiplier)
            total_length += len(curr_product)
            pos_pandigital += curr_product
            curr_multiplier += 1
        if ''.join(sorted(list(pos_pandigital))) == DIGITS and\
                int(pos_pandigital) > largest_pandigital:
            largest_pandigital = int(pos_pandigital)
    print(largest_pandigital)
    print(time.time() - start)


if __name__ == "__main__":
    main()
