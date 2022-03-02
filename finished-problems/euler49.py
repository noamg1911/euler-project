"""
FileName: Prime permutations
Author: N.G 1.5.21
Purpose: Find the 12-digit number that you form by concatenating
the three terms in the sequence (explained in question)
"""

import time
from itertools import permutations
from euler3 import check_if_prime

MIN_NUM = pow(10, 3) + 1
MAX_NUM = pow(10, 4) - 1
NUM_PERMUTATIONS = 3
OTHER_PROPERTY_NUM = 1487


def is_num_permutations_prime_same_distance(num_perms: list) -> str:
    """
    checks if some permutations of a number creates a sequence that has
    the properties wanted in the question
    :param num_perms: the permutations of the number
    :return: An empty string if the sequence doesn't has the properties,
    the sequence itself otherwise
    """
    new_perms = []
    for perm in num_perms:
        if check_if_prime(perm) and perm > MIN_NUM:
            new_perms.append(perm)
    if len(new_perms) < NUM_PERMUTATIONS:
        return ''

    for perm_index in range(len(new_perms)):
        first_perm = new_perms[perm_index]
        for second_perm in new_perms[perm_index:]:
            difference = second_perm - first_perm
            for third_perm in new_perms[perm_index:]:
                if difference and third_perm - second_perm == difference:
                    return str(first_perm) + str(second_perm) + str(third_perm)
    return ''


def main():
    start = time.time()
    sequence = ''
    for num in range(MIN_NUM, MAX_NUM, 2):
        num_perms = list(set(permutations(str(num))))
        num_perms = sorted(int(''.join(perm)) for perm in num_perms)
        if OTHER_PROPERTY_NUM in num_perms:
            continue
        sequence = is_num_permutations_prime_same_distance(num_perms)
        if sequence:
            break
    print(sequence)
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
