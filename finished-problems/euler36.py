"""
FileName: Double-base palindromes
Author: N.G 4.4.21
Purpose: Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2
"""

import time
from euler4 import check_if_palindrome
LIMIT = 10 ** 6

# PENIS


def main():
    start = time.time()
    pal_sum = 0
    for num in range(LIMIT + 1):
        if check_if_palindrome(str(num)) and check_if_palindrome(bin(num)[2:]):
            pal_sum += num
    print(pal_sum)
    print(time.time() - start)


if __name__ == "__main__":
    main()
