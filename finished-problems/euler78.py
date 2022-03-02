"""
FileName: Coin partitions
Author: N.G 28.5.21
Purpose: Find the least value of n for which p(n) is divisible by one million,
         and p(n) represents the number of different ways in which n coins
         can be separated into piles
"""

import time

LIMIT = pow(10, 6)


def get_next_pentagonal(pentagonals: list, curr_k: int) -> int:
    """
    Gets the next pentagonal for the pentagonal list
    :param pentagonals: The current list of pentagonals
    :param curr_k: The current k parameter in the pentagonal equation
    :return: The next parameter in the equation (for the next number)
    """
    next_k = -curr_k
    next_k += 1 if curr_k < 0 else 0
    next_num = (next_k * (3 * next_k - 1)) // 2
    pentagonals.append(next_num)
    return next_k


def get_sum_from_num(num: int, pentagonals: list, num_sums: list) -> int:
    """
    Gets the partition sum of a number
    :param num: The number to get its partition
    :param pentagonals: The current known list of pentagonals
    :param num_sums: The current known list of partition sums
    :return: The partition sum of the number
    """
    curr_sign = 1
    curr_index = 0
    curr_num_sum = 0
    while pentagonals[curr_index] <= num:
        curr_num_sum += curr_sign * num_sums[num - pentagonals[curr_index]]
        curr_index += 1
        curr_sign = -1 if curr_index % 4 > 1 else 1
    curr_num_sum %= LIMIT
    num_sums.append(curr_num_sum)
    return curr_num_sum


def main():
    start = time.time()
    pentagonals = [1, 2]
    curr_k = -1
    known_sums = [1, 1]
    curr_num_sum = 1
    num = 2
    while curr_num_sum:
        while pentagonals[-1] <= num:
            curr_k = get_next_pentagonal(pentagonals, curr_k)
        curr_num_sum = get_sum_from_num(num, pentagonals, known_sums)
        num += 1

    print(num - 1)
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
