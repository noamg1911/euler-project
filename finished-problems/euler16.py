"""
FileName: Power digit sum
Author: N.G 29.3.21
Purpose: Find the sum of the digits of the number 2^1000
"""

BIG_NUM = 2 ** 1000


def main():
    print(sum([int(digit) for digit in str(BIG_NUM)]))


if __name__ == "__main__":
    main()
