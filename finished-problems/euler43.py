"""
FileName: Sub-string divisibility
Author: N.G 15.4.21
Purpose: Find the sum of all 0-9 pandigital numbers with this property (in Q)
"""

import time
from itertools import permutations

DIGITS = 10
primes = [2, 3, 5, 7, 11, 13, 17]


def get_endings(prime: int, curr_endings: list) -> list:
    """
    gets a list of numbers and returns these numbers with another digit,
    but only if it is a non repeating number and it divides with a prime
    :param prime: the prime to be divisible with
    :param curr_endings: the list of numbers
    :return: a new list of the numbers from before if they passed the tests
    """
    new_endings = []
    for num in curr_endings:
        new_num = int(str(num)[-2:]) * 10
        leftover = prime - (new_num % prime)
        pos_ending = new_num + leftover if leftover != prime else new_num
        if str(pos_ending)[-2] == str(new_num)[-2] and\
                str(pos_ending).count(str(pos_ending)[-1]) == 1 and\
                '5' not in str(pos_ending):
            new_endings.append(int(str(num)[:-2] + str(pos_ending)))
    return new_endings


def main():
    start = time.time()
    fifth_digit = 5
    pandigitals_sum = 0

    divisible_endings = []
    for ending in range(fifth_digit * 100, (fifth_digit + 1) * 100 + 1):
        if ending % primes[-3] == 0 and ending % 5 != 0:
            divisible_endings.append(ending)
    endings_13 = get_endings(primes[-2], divisible_endings)
    endings_17 = get_endings(primes[-1], endings_13)
    endings_six_digits = []
    for ending in endings_17:
        curr_check = str(ending)[:2]
        for digit in range(1, DIGITS):
            if int(str(digit) + curr_check) % 7 == 0 and\
                    str(digit) not in str(ending):
                endings_six_digits.append(int(str(digit) + str(ending)))

    for ending in endings_six_digits:
        curr_digits = list(range(DIGITS))
        for digit in str(ending):
            curr_digits.remove(int(digit))
        pos_starts = [''.join(num) for num
                      in list(permutations([str(x) for x in curr_digits]))]
        for pos_start in pos_starts:
            if int(pos_start[3]) % primes[0] == 0 and\
                    pos_start[0] != '0' and\
                    int(pos_start[-2:] + str(ending)[0]) % primes[1] == 0:
                pandigitals_sum += int(pos_start + str(ending))

    print(pandigitals_sum)
    print(time.time() - start)


if __name__ == "__main__":
    main()
