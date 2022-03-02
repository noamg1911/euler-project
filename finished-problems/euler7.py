"""
FileName: 10001st prime
Author: N.G 28.3.21
Purpose: Find the 10001st prime number
"""

import time
import math
LIMIT = 10001


def check_if_prime(num: int) -> bool:
    """
    checks if a number is prime
    :param num: the number to be checked
    :return: True if it's prime, False otherwise
    (if divisible by any number up to the checked number's root)
    """
    if num <= 3:
        return num > 1
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(num)) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True


def main():
    start = time.time()
    count = 1
    num = 3
    while count != LIMIT:
        if check_if_prime(num):
            count += 1
        num += 2
    print(num - 2)
    print(time.time() - start)


if __name__ == "__main__":
    main()
