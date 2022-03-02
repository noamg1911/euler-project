"""
FileName: Truncatable primes
Author: N.G 4.4.21
Purpose: Find the sum of the only eleven primes that are both truncatable from left to right and right to left
"""

import time
from euler3 import check_if_prime
NUM_TRUNC = 11
# PENIS


def is_truncatable(num: int, primes: set) -> bool:
    """
    checks if a prime is truncatable
    :param num: the prime to be checked
    :param primes: the set of known primes
    :return: True if it is, False otherwise
    """
    str_num = str(num)
    for i in range(1, len(str_num)):
        if int(str_num[i:]) not in primes or int(str_num[:i]) not in primes:
            return False
    return True


def main():
    start = time.time()
    truncs = 0
    trunc_count = 0
    primes = {2, 3, 5, 7}
    num = 11
    while trunc_count != NUM_TRUNC:
        str_num = str(num)
        if '0' not in str_num and '4' not in str_num and '6' not in str_num and '8' not in str_num\
                and (num in primes or check_if_prime(num)):
            primes.add(num)
            if is_truncatable(num, primes):
                truncs += num
                trunc_count += 1
        num += 2
    print(truncs)
    print(time.time() - start)


if __name__ == "__main__":
    main()
