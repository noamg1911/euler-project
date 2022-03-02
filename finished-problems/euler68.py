"""
FileName: Magic 5-gon ring
Author: N.G 16.5.21
Purpose: Find the maximum 16-digit string for a "magic" 5-gon ring
         (explained in question)
"""

import time
from itertools import permutations

ITEMS = 10
RING = 5
BRANCH_ITEMS = 3


def get_concat_number_gon_ring(gon_ring: list) -> int:
    """
    Gets the concatenated number of the branches of a 5-gon ring
    :param gon_ring: The 5-gon ring to get the string number out of
    :return: The number of the string of the items of the 5-gon ring
    """
    curr_num = ''
    for branch in gon_ring:
        curr_num += ''.join([str(num) for num in branch])
    return int(curr_num)


def is_gon_ring_valid(gon_ring: list) -> bool:
    """
    Checks if a gon ring is a valid 5-gon ring (all branches have the same sum)
    :param gon_ring: The 5-gon ring to check its validity
    :return: A boolean value of whether the 5-gon ring is valid or not
    """
    branch_sum = sum(gon_ring[0])
    for branch in gon_ring:
        if sum(branch) != branch_sum:
            return False
    return True


def get_valid_gon_rings(outer: list):
    """
    Gets from an outer ring of a 5-gon ring all of the valid 5-gon rings
    (with randomized inner rings)
    :param outer: The outer ring of the 5-gon ring
    :return: A list of all the valid 5-gon rings that can be made
             from the given outer ring
    """
    valid_gon_numbers = []
    inner_rings = [list(perm) for perm in
                   list(permutations(range(1, RING + 1), RING))]
    for inner in inner_rings:
        gon_ring = [[outer[item], inner[item], inner[(item + 1) % RING]]
                    for item in range(RING)]
        if is_gon_ring_valid(gon_ring):
            gon_ring_num = get_concat_number_gon_ring(gon_ring)
            valid_gon_numbers.append(gon_ring_num)
    return valid_gon_numbers


def main():
    start = time.time()
    outer_rings = [list(perm) for perm in
                   list(permutations(range(RING + 1, ITEMS + 1), RING))]
    outer_rings = list(filter(lambda perm: perm[0] == RING + 1, outer_rings))
    valid_gon_numbers = []

    for outer_ring in outer_rings:
        valid_gon_numbers += get_valid_gon_rings(outer_ring)

    print(max(valid_gon_numbers))
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
