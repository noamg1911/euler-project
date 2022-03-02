"""
FileName: Digit fifth powers
Author: N.G 2.4.21
Purpose: Find the sum of all the numbers that can be written as the sum of fifth powers of their digits
"""

import time
POWER = 5
# one-liner! print(sum([x for x in range(2, 9 ** POWER * (POWER + 1)) if sum(int(i) ** POWER for i in str(x)) == x]))


def main():
    start = time.time()
    max_num = 9 ** POWER * (POWER + 1)
    max_num = int(str(max_num)[0]) ** 5 + 9 ** POWER * (len(str(max_num)) - 1)
    print(sum([x for x in range(2, max_num) if sum(int(i) ** POWER for i in str(x)) == x]))
    print(time.time() - start)


if __name__ == "__main__":
    main()
