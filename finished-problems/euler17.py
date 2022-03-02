"""
FileName: Number letter counts
Author: N.G 29.3.21
Purpose: Find how many letters would be used if all the numbers
from 1 to 1000 inclusive were written out in words
"""

LIMIT = 1000
LENGTH_HUNDRED = 7
LENGTH_AND = 3


def main():
    up_to_twenty = {1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3,
                    11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8}
    tens = {10: 3, 20: 6, 30: 6, 40: 5, 50: 5, 60: 5, 70: 7, 80: 6, 90: 6}
    total_sum = 0
    sum_hundred = 0
    for num in range(1, 100):
        if num < 20:
            sum_hundred += up_to_twenty[num]
        elif num % 10 == 0:
            sum_hundred += tens[num]
        else:
            sum_hundred += tens[num // 10 * 10]
            sum_hundred += up_to_twenty[num % 10]
    for num in range(1, 10):
        total_sum += up_to_twenty[num] + LENGTH_HUNDRED
        total_sum += sum_hundred + (LENGTH_HUNDRED + LENGTH_AND + up_to_twenty[num]) * 99
    total_sum += up_to_twenty[1] + len('thousand') + sum_hundred
    print(total_sum)


if __name__ == "__main__":
    main()
