"""
FileName: 1000-digit Fibonacci number
Author: N.G 31.3.21
Purpose: Find the index of the first term in the Fibonacci sequence to contain 1000 digits
"""

import time
LIMIT = 10 ** 3


def main():
    start = time.time()
    curr_num = 1
    prev_num = 0
    curr_index = 1
    while len(str(curr_num)) < LIMIT:
        curr_num += prev_num
        prev_num = curr_num - prev_num
        curr_index += 1
    print(curr_index, time.time() - start)


if __name__ == "__main__":
    main()
