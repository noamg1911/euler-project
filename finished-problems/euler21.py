"""
FileName: Amicable numbers
Author: N.G 30.3.21
Purpose: Find the sum of all the amicable numbers under 10000
"""

import math
LIMIT = 10000


def sum_divisors(num: int) -> int:
    """
    returns the sum of the divisors of a number
    :param num: the number to be calculated
    :return: the sum of the number's divisors
    """
    divisor_sum = 1
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            divisor_sum += i
            if num / i != i:
                divisor_sum += num / i
    return int(divisor_sum)


def main():
    known_amicables = {}
    for num in range(2, LIMIT):
        num_divisors_sum = sum_divisors(num)
        if num == sum_divisors(num_divisors_sum) and num != num_divisors_sum:
            known_amicables[num] = num_divisors_sum
    print(sum(known_amicables))


if __name__ == "__main__":
    main()
