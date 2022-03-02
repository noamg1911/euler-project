"""
FileName: Smallest multiple
Author: N.G 28.3.21
Purpose: Find the smallest positive number that is evenly divisible by all of the numbers from 1 to 20
"""

import time
MAX_NUM = 20


def main():
    start = time.time()
    smallest_multiple = 1
    for num in (range(2, MAX_NUM + 1)):
        for possible_divisor in range(1, 21):
            if (smallest_multiple * possible_divisor) % num == 0:
                smallest_multiple *= possible_divisor
                break
    print(smallest_multiple, time.time() - start)


if __name__ == "__main__":
    main()
