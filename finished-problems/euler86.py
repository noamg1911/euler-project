"""
Cuboid Route
"""

import time
from math import sqrt

limit = 10


def get_base_pythagorian_triplet_from_index_var(index_value: int) -> tuple:
    short_side = 2 * index_value + 1
    middle_side = 2 * index_value ** 2 + short_side - 1
    long_side = middle_side + 1
    return short_side, middle_side, long_side


def get_pythagorian_triplet_from_index_var_and_its_multiples(index_value: int) -> list:
    triplets = []
    base_triplet = get_base_pythagorian_triplet_from_index_var(index_value)
    short_side, middle_side = base_triplet[:2]
    multiplication_factor = min((limit * 2) // middle_side, limit // short_side)
    for multiplication_val in range(1, multiplication_factor + 1):
        multiplied_triplet = tuple((side * multiplication_val for side in base_triplet))
        triplets.append(multiplied_triplet)
    return triplets


def generate_pythagorian_triplets() -> list:
    pythagorian_triplets = []
    max_n_var = round(sqrt(limit))
    for n in range(1, max_n_var):
        pythagorian_triplets.extend(get_pythagorian_triplet_from_index_var_and_its_multiples(n))
    return pythagorian_triplets


def get_max_num_cuts_and_starting_cut_size_for_cuboid_side(side_to_cut: int) -> tuple:
    max_num_cuts = side_to_cut // 2
    starting_cut_size = 1
    if side_to_cut > limit:
        starting_cut_size = side_to_cut - limit
        max_num_cuts = min(max_num_cuts, starting_cut_size // 2, (limit - starting_cut_size) // 2)
    return max_num_cuts, starting_cut_size


def get_cuboid_variations_from_specific_side(side_to_cut: int, other_side: int):
    cuboid_variations = set()
    max_num_cuts, starting_cut_size = get_max_num_cuts_and_starting_cut_size_for_cuboid_side(side_to_cut)
    for cuboid_height in range(starting_cut_size, max_num_cuts + 1):
        side_to_cut -= 1
        cuboid_size = tuple(sorted((other_side, side_to_cut, cuboid_height)))
        if cuboid_size[2] > limit:
            print(cuboid_size, max_num_cuts, side_to_cut, other_side)
        cuboid_variations.add(cuboid_size)
    return cuboid_variations


def get_cuboid_variations_from_triplet(triplet: tuple):
    short_side, middle_side, long_side = triplet
    cuboid_variations = set()
    if middle_side < limit:
        cuboid_variations.update(get_cuboid_variations_from_specific_side(short_side, middle_side))
    cuboid_variations.update(get_cuboid_variations_from_specific_side(middle_side, short_side))
    return cuboid_variations


def get_all_cuboid_variations():
    global limit
    pythagorian_triplets = generate_pythagorian_triplets()
    cuboid_variations = set()
    for triplet in pythagorian_triplets:
        cuboid_variations.update(get_cuboid_variations_from_triplet(triplet))
    return cuboid_variations


def main():
    start = time.time()
    global limit
    cuboids = get_all_cuboid_variations()
    print(cuboids)
    print(len(cuboids))

    print(time.time() - start)


if __name__ == "__main__":
    main()
