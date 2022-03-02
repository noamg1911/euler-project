"""
FileName: Path sum: two ways
Author: N.G 11.6.21
Purpose: Find the minimal path sum from the top left to the bottom right
         in the matrix (directions: down & right)
"""

import time

LEN_MATRIX = 80


def get_matrix():
    """
    Gets the matrix from the file
    :return: The matrix from the text file
    """
    matrix = []
    with open('euler81_text.txt', 'r') as matrix_file:
        for line in matrix_file:
            matrix.append(list(map(int, line.split(','))))
    return matrix


def change_matrix_boundaries(matrix: list):
    """
    Changes the boundaries (right and down) of the matrix
    according to minimal path rules
    :param matrix: The matrix of numbers
    """
    for line in range(LEN_MATRIX - 2, -1, -1):
        matrix[line][-1] += matrix[line + 1][-1]
        matrix[-1][line] += matrix[-1][line + 1]


def main():
    start = time.time()
    matrix = get_matrix()
    change_matrix_boundaries(matrix)
    for num in range(LEN_MATRIX - 2, -1, -1):
        for line in range(LEN_MATRIX - 2, -1, -1):
            matrix[line][num] += min(matrix[line][num + 1],
                                     matrix[line + 1][num])
    print(matrix[0][0])
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
