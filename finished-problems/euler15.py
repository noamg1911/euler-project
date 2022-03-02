"""
FileName: Lattice paths
Author: N.G 29.3.21
Purpose: Find ow many such routes are there through a 20×20 grid,
that can go only right and down, starting from the top left corner
"""

import math
GRID_SIZE = 20


def main():
    print(int(math.factorial(GRID_SIZE * 2) / math.factorial(GRID_SIZE) ** 2))


if __name__ == "__main__":
    main()
