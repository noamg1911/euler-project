"""
FileName: Maximum path sum II (also works with I, euler 18)
Author: N.G 15.5.21
Purpose: Find the maximum total from top to bottom of the triangle
"""

import time


def get_triangle_rows() -> list:
    """
    Gets the rows of the triangle from the text file (explained in question)
    :return: The list of rows of numbers in the triangle
    """
    with open('euler67_text.txt', 'r') as triangle_file:
        triangle = [row.split() for row in triangle_file]
        for row in range(len(triangle)):
            triangle[row] = list(map(int, triangle[row]))
    return triangle


def main():
    start = time.time()
    triangle = get_triangle_rows()

    for line in range(len(triangle) - 2, -1, -1):
        for num in range(len(triangle[line])):
            triangle[line][num] += max(triangle[line + 1][num + 1],
                                       triangle[line + 1][num])
    print(triangle[0][0])
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
