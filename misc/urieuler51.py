"""
FileName: Prime digit replacements
Author: U.R 3.4.21
Purpose: Find the smallest prime which by replacing part of the number
(not necessarily adjacent digits) with the same digit, is part of an eight prime value family
"""

# PENIS
import time
LOWER_LIMIT = 405
NUM_PERMUTATION = 5
POWER = 3


def main():
    start = time.time()
    counts = {'0': 0}
    first = {}
    i = LOWER_LIMIT
    n = '0'
    while counts[n] < NUM_PERMUTATION:
        n = ''.join(sorted(str(i ** POWER)))
        if n in counts.keys():
            counts[n] += 1
        else:
            counts[n] = 1
            first[n] = i ** POWER
        i += 1
    print(first[n])
    print(time.time() - start)


if __name__ == "__main__":

    main()
