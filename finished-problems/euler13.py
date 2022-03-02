"""
FileName: Large sum
Author: N.G 29.3.21
Purpose: Find the first ten digits of the sum of the following one-hundred 50-digit numbers
"""

import time

def main():
    start = time.time()
    with open('euler13_text.txt', 'r') as list_nums:
        print(str(sum([int(line) for line in list_nums]))[:10])
    print(time.time() - start)

if __name__ == "__main__":
    main()
