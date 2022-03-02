"""
FileName: Path sum: three ways
Author: N.G 11.6.21
Purpose: Find the minimal path sum from the left column to the right column
        in the matrix (directions: up, down & right)
"""

import time
from euler81 import get_matrix, LEN_MATRIX


def get_min_path(matrix: list, line: int, num: int) -> int:
    """
    Gets the minimal path for a specific item in the matrix
    :param matrix: The matrix itself
    :param line: The line index of the item in the matrix
    :param num: The number index of the line of the item in the matrix
    :return: The minimal path sum of the item
    """
    best_path = matrix[line][num + 1]

    curr_line = line + 1
    curr_path = 0
    while curr_path < best_path and curr_line <= LEN_MATRIX - 1:
        curr_path += matrix[curr_line][num]
        best_path = min(best_path, curr_path + matrix[curr_line][num + 1])
        curr_line += 1

    curr_line = line - 1
    curr_path = 0
    while curr_path < best_path and curr_line >= 0:
        curr_path += matrix[curr_line][num]
        best_path = min(best_path, curr_path + matrix[curr_line][num + 1])
        curr_line -= 1

    return best_path


def main():
    start = time.time()
    matrix = get_matrix()

    for num in range(LEN_MATRIX - 2, 0, -1):
        curr_column = []

        for line in range(LEN_MATRIX):
            curr_column.append(get_min_path(matrix, line, num))

        for line in range(LEN_MATRIX):
            matrix[line][num] += curr_column[line]

    print(min(sum(matrix[line][:2]) for line in range(LEN_MATRIX)))
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
