"""
Counting Rectangles
"""

import time

CONTAIN_LIMIT = 2000000
BIGGEST_POSSIBLE_WIDTH = 200


def get_rectangle_count(length: int, width: int) -> int:
    """
    Gets the number of rectangles in the specified grid
    """
    return (length * (length + 1) * width * (width + 1)) // 4


def find_length_and_difference_for_closest_rectangle_num(width: int) -> tuple:
    """
    For some width, finds the length so that their grid gives the closest amount of rectangles to the limit (2 Million)
    """
    closest_difference = CONTAIN_LIMIT
    closest_length = width
    current_length = width
    while True:
        current_difference = abs(CONTAIN_LIMIT - get_rectangle_count(current_length, width))
        if current_difference < closest_difference:
            closest_difference = current_difference
            closest_length = current_length
        else:
            return closest_difference, closest_length
        current_length += 1


def main():
    start = time.time()
    closest_difference_width = closest_difference_length = closest_difference = CONTAIN_LIMIT
    for width in range(1, BIGGEST_POSSIBLE_WIDTH):
        current_closest_difference, current_closest_length = find_length_and_difference_for_closest_rectangle_num(width)
        if current_closest_difference < closest_difference:
            closest_difference = current_closest_difference
            closest_difference_length = current_closest_length
            closest_difference_width = width
    print(f"Difference: {closest_difference}, Width: {closest_difference_width} Length: {closest_difference_length} "
          f"Grid Area: {closest_difference_width * closest_difference_length}")
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
