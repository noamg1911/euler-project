"""
FileName: Lexicographic permutations
Author: N.G 31.3.21
Purpose: Find the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9
"""

import time
INDEX = 10 ** 6
NUM_OF_ITEMS = 10


def factorial(num):
    """
    calculate the factorial of a number
    :param num: the number to be calculated
    :return: the factorial of the number
    """
    factorial_num = 1
    for i in range(num, 1, -1):
        factorial_num *= i
    return factorial_num


def main():
    start = time.time()
    digits = [str(num) for num in range(NUM_OF_ITEMS)]
    final_permutation = []
    curr_permutation = 0
    for digit in range(len(digits)):
        curr_digit = 0
        while curr_permutation < INDEX:
            curr_permutation += factorial(NUM_OF_ITEMS - 1 - digit)
            curr_digit += 1
        final_permutation.append(digits[curr_digit - 1])
        digits.remove(digits[curr_digit - 1])
        curr_permutation -= factorial(NUM_OF_ITEMS - 1 - digit)
    print(''.join(final_permutation), time.time() - start)


if __name__ == "__main__":
    main()
