"""
FileName: Integer right triangles
Author: N.G 9.4.21
Purpose: Find the value of p ≤ 1000 for which the number of solutions
is maximised (explained in Q)
"""

import time

MAX_VALUE = 10 ** 3


def main():
    start = time.time()
    max_solutions = {}
    for a_side in range(1, MAX_VALUE // 3 + 1):
        for b_side in range(a_side, MAX_VALUE // 2):
            c_side = int((a_side ** 2 + b_side ** 2) ** 0.5)
            if a_side + b_side + c_side < MAX_VALUE + 1 and \
                    a_side ** 2 + b_side ** 2 == c_side ** 2:
                perimeter = a_side + b_side + c_side
                if perimeter not in max_solutions:
                    max_solutions[perimeter] = 0
                max_solutions[perimeter] += 1
    print(max(max_solutions, key=max_solutions.get))
    print(time.time() - start)


if __name__ == "__main__":
    main()
