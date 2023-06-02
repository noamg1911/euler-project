"""

"""

import time
from math import sqrt


def get_base_pythagorian_triplet_from_index_var(index_value: int) -> tuple:
    short_side = 2 * index_value + 1
    middle_side = 2 * index_value ** 2 + short_side - 1
    long_side = middle_side + 1
    return short_side, middle_side, long_side


def get_pythagorian_triplet_from_index_var_and_its_multiples(index_value: int) -> list:
    sides = []
    base_triplet = get_base_pythagorian_triplet_from_index_var(index_value)
    short_side, middle_side = base_triplet[:2]
    multiplication_factor = min((limit * 2) // middle_side, limit // short_side)
    relevant_sides = short_side, middle_side
    for multiplication_val in range(1, multiplication_factor + 1):
        multiplied_sides = tuple((side * multiplication_val for side in relevant_sides))
        sides.append(multiplied_sides)
    return sides


def generate_pythagorian_triplet_right_angle_sides() -> list:
    pythagorian_sides = []
    max_n_var = round(sqrt(limit))
    for n in range(1, max_n_var):
        pythagorian_sides.extend(get_pythagorian_triplet_from_index_var_and_its_multiples(n))
    return pythagorian_sides


def generate_possible_cuboid_sizes_no_heights():
    cuboid_plane_sizes = []
    for x in range(1, limit + 1):
        for y in range(x, limit + 1):
            cuboid_plane_sizes.append((x, y))
    return cuboid_plane_sizes


def get_cuboids_for_plane_pair(plane_pair: tuple):
    plane_cuboids = set()
    short_side, long_side = plane_pair
    max_height_for_plane = limit - short_side
    for height in range(1, max_height_for_plane + 1):
        new_pair = short_side, long_side + height
        if new_pair in pythagorean_sides:
            cuboid = tuple(sorted((short_side, long_side, height)))
            plane_cuboids.add(cuboid)
        new_pair = tuple(sorted((short_side + height, long_side)))
        if new_pair in pythagorean_sides:
            cuboid = tuple(sorted((short_side, long_side, height)))
            plane_cuboids.add(cuboid)
    return plane_cuboids


def get_all_cuboids():
    possible_cuboid_planes = generate_possible_cuboid_sizes_no_heights()
    cuboids = set()
    for plane in possible_cuboid_planes:
        cuboids.update(get_cuboids_for_plane_pair(plane))
    return cuboids


limit = 200
pythagorean_sides = generate_pythagorian_triplet_right_angle_sides()


def main():
    start = time.time()
    global limit
    cuboids = get_all_cuboids()
    print(cuboids)
    print(len(cuboids))
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
