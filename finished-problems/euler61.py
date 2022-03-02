"""
FileName: Cyclical figurate numbers
Author: N.G 14.5.21
Purpose:
"""

import time

NUM_DIGITS = 4
HALF_NUM = NUM_DIGITS // 2
MIN_LIMIT = pow(10, NUM_DIGITS - 1)
MAX_LIMIT = pow(10, NUM_DIGITS) - 1

SET_SIZE = 6
TRIANGLE_INDEX = 0
SQUARE_INDEX = 1
PENTAGONAL_INDEX = 2
HEXAGONAL_INDEX = 3
HEPTAGONAL_INDEX = 4
OCTAGONAL_INDEX = 5


def get_polygon_number(n: int, polygon_index: int) -> int:
    """
    Gets a polygon number (shape depends on the index) from an index x
    :param n: The index of the polygon number in the polygon list
    :param polygon_index: The shape of the polygon to get the number for
    :return: The polygon number
    """
    if polygon_index == TRIANGLE_INDEX:
        return int(n * (n + 1) / 2)
    elif polygon_index == SQUARE_INDEX:
        return int(pow(n, 2))
    elif polygon_index == PENTAGONAL_INDEX:
        return int(n * (3 * n - 1) / 2)
    elif polygon_index == HEXAGONAL_INDEX:
        return int(n * (2 * n - 1))
    elif polygon_index == HEPTAGONAL_INDEX:
        return int(n * (5 * n - 3) / 2)
    elif polygon_index == OCTAGONAL_INDEX:
        return int(n * (3 * n - 2))


def get_polygon_options() -> list:
    """
    Gets all polygon options for all the shapes between the limits
    :return: The lsit of lists of shapes and their numbers
    """
    polygons = []
    for i in range(SET_SIZE):
        polygons.append([])

    for shape in range(SET_SIZE):
        index = 1
        curr_shape_num = 1
        while curr_shape_num < MAX_LIMIT + 1:
            index += 1
            curr_shape_num = get_polygon_number(index, shape)
            if MIN_LIMIT < curr_shape_num < MAX_LIMIT + 1:
                polygons[shape].append(str(curr_shape_num))
    return remove_repeating_numbers(polygons)


def remove_repeating_numbers(polygons: list) -> list:
    """
    Removes numbers from the polygon list that appear in more than one shape
    :param polygons: The original polygon list
    :return: The new polygon list, filtered
    """
    for shape in range(len(polygons)):
        for number in polygons[shape]:
            for other_shape in range(len(polygons)):
                if number in polygons[other_shape] and other_shape != shape:
                    polygons[shape].remove(number)
                    break
    return polygons


def get_set(polygons: list, pos_shapes: list, pos_cyclic: list) -> list:
    """
    Gets the set of cyclic numbers as specified in the question
    :param polygons: The list of all the polygon numbers
    :param pos_shapes: The current list of shapes that are in the possible
                       cyclic list
    :param pos_cyclic: The current list of cyclic numbers
    :return: The cyclic list, until it's full (recursive function)
    """
    relevant_family = [num for num in pos_cyclic if num]
    relevant_shapes = [shape for shape in pos_shapes if shape]
    for shape in range(len(polygons)):
        if shape + 1 in pos_shapes:
            continue
        for num in polygons[shape]:
            if relevant_family[-1][HALF_NUM:] == num[:HALF_NUM]:
                pos_cyclic[len(relevant_family)] = num
                pos_shapes[len(relevant_shapes)] = shape + 1

                if pos_cyclic[-1]:
                    if pos_cyclic[-1][HALF_NUM:] == pos_cyclic[0][:HALF_NUM]:
                        return pos_cyclic
                    pos_cyclic[len(relevant_family)] = 0
                    pos_shapes[len(relevant_shapes)] = 0
                    continue

                pos_cyclic = get_set(polygons, pos_shapes, pos_cyclic)
                if pos_cyclic[-1]:
                    return pos_cyclic

    if not pos_cyclic[len(relevant_family)]:
        pos_cyclic[len(relevant_family) - 1] = 0
        pos_shapes[len(relevant_shapes) - 1] = 0
    return pos_cyclic


def main():
    start = time.time()
    polygons = get_polygon_options()
    shape_set = [0] * SET_SIZE
    curr_shapes = [0] * SET_SIZE

    while not shape_set[SET_SIZE - 1]:
        for num in polygons[TRIANGLE_INDEX]:
            shape_set[0] = num
            curr_shapes[0] = TRIANGLE_INDEX + 1
            shape_set = get_set(polygons, curr_shapes, shape_set)
            if shape_set[-1]:
                break
    print(shape_set, sum(list(map(int, shape_set))))
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
