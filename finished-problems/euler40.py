"""
FileName: Champernowne's constant
Author: N.G 10.4.21
Purpose: Find the value of the following expression if d(n) represents
the nth digit of the fractional part (explained in Q)
"""

import time
NUM_POWERS = 7


def main():
    start = time.time()
    constant = ''
    constant_length = 0
    curr_num = 1
    while constant_length < 10 ** (NUM_POWERS - 1):
        str_num = str(curr_num)
        constant += str_num
        constant_length += len(str_num)
        curr_num += 1
    total_value = 1
    for power in range(NUM_POWERS):
        total_value *= int(constant[10 ** power - 1])
    print(total_value)
    print(time.time() - start)


if __name__ == "__main__":
    main()
