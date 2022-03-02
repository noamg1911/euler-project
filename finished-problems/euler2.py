"""
FileName: Even Fibonacci numbers
Author: N.G 28.3.21
Purpose: By considering the terms in the Fibonacci sequence
whose values do not exceed four million, find the sum of the even-valued terms.
"""

LIMIT = 4000000


def main():
    curr_num = 1
    prev_num = 0
    even_sum = 0

    while curr_num < LIMIT:
        curr_num += prev_num
        prev_num = curr_num - prev_num
        even_sum += curr_num if curr_num % 2 == 0 else 0

    print(even_sum)


if __name__ == "__main__":
    main()
