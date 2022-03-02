"""
FileName: Digit factorials
Author: N.G 3.4.21
Purpose: Find the sum of all numbers which are equal to the sum of the factorial of their digits
"""

import time
NUM_DIGITS = 9


def main():
    start = time.time()
    factorial_digits = {'0': 1}
    for digit in range(1, NUM_DIGITS + 1):
        factorial_digits[str(digit)] = factorial_digits[str(digit - 1)] * digit

    max_len = 2
    while 10 ** max_len - 1 < factorial_digits[str(NUM_DIGITS)] * max_len:
        max_len += 1
    max_num = factorial_digits[str(NUM_DIGITS)] * max_len
    max_num = factorial_digits[str(max_num)[0]] + factorial_digits[str(NUM_DIGITS)] * (max_len - 1)

    total_sum = 0
    for num in range(10, max_num + 1):
        string_num = str(num)
        curr_sum = 0
        for digit in string_num:
            curr_sum += factorial_digits[digit]
        if num == curr_sum:
            total_sum += num

    print(total_sum)
    print(time.time() - start)


if __name__ == "__main__":
    main()
