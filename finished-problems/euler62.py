"""
FileName: Cubic permutations
Author: N.G 14.5.21
Purpose: Find the smallest cube for which exactly five permutations
         of its digits are cube
"""

import time

NUM_PERMUTATIONS = 5
CUBE_POWER = 3


def get_sorted_str_num(num: int) -> str:
    """
    Gets the sorted (by digits) string of a number
    :param num: The number to sort
    :return: The sorted string of digits of the number
    """
    return ''.join(sorted(str(num)))


def get_cube_index() -> int:
    """
    Gets the number that its cube has 5 permutations that are cube
    :return: The number of that cube (cubic root of the cube)
    """
    curr_index = 1
    cubes = {1: 1}
    while max(cubes.values()) < NUM_PERMUTATIONS:
        curr_cube = pow(curr_index, CUBE_POWER)
        sorted_cube = get_sorted_str_num(curr_cube)
        if sorted_cube not in cubes:
            cubes[sorted_cube] = 0
        cubes[sorted_cube] += 1
        curr_index += 1
    return curr_index - 1


def main():
    start = time.time()
    cube_index = get_cube_index()
    cube_sorted = get_sorted_str_num(pow(cube_index, CUBE_POWER))
    curr_perm_count = 1
    smallest_index = cube_index
    curr_index = cube_index - 1

    while curr_perm_count != NUM_PERMUTATIONS:
        curr_cube = pow(curr_index, CUBE_POWER)
        if get_sorted_str_num(curr_cube) == cube_sorted:
            curr_perm_count += 1
            smallest_index = curr_index
        curr_index -= 1

    print(pow(smallest_index, CUBE_POWER))
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
