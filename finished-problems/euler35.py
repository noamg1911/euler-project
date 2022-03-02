"""
FileName: Circular primes
Author: N.G 3.4.21
Purpose: Find how many circular primes are there below one million
"""

from euler26 import get_primes
import time

LIMIT = 10 ** 6


def check_circular(num: int, known_primes: set, circulars: set):
    """
    checks if a number is a circular prime (every iteration of the number by moving a digit is prime)
    :param num: the number to be checked
    :param known_primes: the set of known primes up to the limit specified in the question
    :param circulars: the set of known circular primes
    """
    length_num = len(str(num))
    num_combs = set()
    num_combs.add(num)
    for i in range(length_num - 1):
        num = (num % 10) * 10 ** (length_num - 1) + num // 10
        if num not in known_primes or num % 2 == 0 or num % 5 == 0:
            return
        num_combs.add(num)
    for number in num_combs:
        circulars.add(number)


def main():
    start = time.time()
    known_primes = get_primes(LIMIT)
    circulars = set()
    for num in list(known_primes):
        if num not in circulars:
            check_circular(num, known_primes, circulars)
    print(len(circulars))
    print(time.time() - start)


if __name__ == "__main__":
    main()
