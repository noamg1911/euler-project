"""
FileName: Counting Sundays
Author: N.G 29.3.21
Purpose: Find how many Sundays fell on the first of the month during the twentieth century
"""

import time
LENGTH_WEEK = 7
NUM_MONTHS = 12
NUM_YEARS = 100
FIRST_YEAR = 1901


def main():
    start = time.time()
    months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    curr_month = 1
    year = FIRST_YEAR
    sunday = 6
    num_sundays = 0
    while year < 2001:
        sunday += LENGTH_WEEK
        if sunday > months[curr_month]:
            sunday -= months[curr_month]
            if curr_month != NUM_MONTHS:
                curr_month += 1
            else:
                curr_month = 1
                year += 1
                months[2] -= 1 if year % 4 == 1 else 0
                months[2] += 1 if year % 4 == 0 else 0
            if sunday == 1 and year != FIRST_YEAR + NUM_YEARS:
                num_sundays += 1
    print(num_sundays, time.time() - start)


if __name__ == "__main__":
    main()
