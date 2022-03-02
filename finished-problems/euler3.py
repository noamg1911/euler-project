
"""
FileName: Largest prime factor
Author: N.G 28.3.21
Purpose: Find the largest prime factor of the number 600851475143
"""

import time
NUM = 600851475143


def check_if_prime(num: int) -> bool:
    """
    checks if a number is prime
    :param num: the number to be checked
    :return: True if it's prime, False otherwise
    (if divisible by any number up to the checked number's root)
    """
    if num <= 3:
        return num > 1
    if not num % 2 or not num % 3:
        return False
    for i in range(5, int(num ** 0.5 + 1), 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True


def main():
    start = time.time()
    for num in range(int(NUM ** 0.5 + 1), 2, -1):
        if NUM % num == 0 and check_if_prime(num):
            print(num)
            print(time.time() - start)
            break


if __name__ == "__main__":
    main()
