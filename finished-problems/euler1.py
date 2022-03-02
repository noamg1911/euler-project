"""
FileName: Multiples of 3 and 5
Author: N.G 28.3.21
Purpose: Find the sum of all the multiples of 3 or 5 below 1000.
"""

LIMIT = 1000
FIRST_DIVISOR = 3
SECOND_DIVISOR = 5


def main():
    print(sum([num for num in range(LIMIT)
               if num % FIRST_DIVISOR == 0 or num % SECOND_DIVISOR == 0]))


if __name__ == "__main__":
    main()
