"""
FileName: Goldbach's other conjecture
Author: N.G 30.4.21
Purpose: Find the smallest odd composite that cannot be written as the
sum of a prime and twice a square
"""

import time
import math
from euler3 import check_if_prime

MIN_NUM = 9


def break_conjecture(num: int) -> bool:
    """
    checks if an odd number breaks the conjecture (Problem's Purpose, line 4)
    :param num: the odd composite number to check
    :return: True whether the number breaks the conjecture or not
    """
    if check_if_prime(num):
        return False
    for i in range(int(math.sqrt(num))):
        maybe_prime = int(num - 2 * math.pow(i, 2))
        if check_if_prime(maybe_prime):
            return False
    return True


def main():
    start = time.time()
    curr_num = MIN_NUM
    while not break_conjecture(curr_num):
        curr_num += 2
    print(curr_num)
    print(time.time() - start)


if __name__ == "__main__":
    main()
