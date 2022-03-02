"""
FileName: Path sum: four ways
Author: N.G 12.6.21
Purpose: Find the minimal path sum from the top left to the bottom right
         in the matrix (directions: up, down, left & right)
"""

import time
from euler81 import get_matrix, LEN_MATRIX


def main():
    start = time.time()
    matrix = get_matrix()
    a = 28433 * pow(2, 7830457) + 1
    print(str(a)[-10:])
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
