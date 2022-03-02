"""
FileName: Longest Collatz sequence
Author: N.G 29.3.21
Purpose: Find which starting number, under one million, produces the longest chain in the Collatz sequence
"""

import time

LIMIT = pow(10, 6)


def main():
    start = time.time()
    known_chains = {1: 1}
    for num in range(1, LIMIT, 2):
        number = num
        chain = 1
        while number != 1:
            if number not in known_chains:
                if number % 2 == 0:
                    number /= 2
                else:
                    number *= 3
                    number += 1
                chain += 1
            else:
                chain += known_chains[number]
                break
        known_chains[num] = chain

    print(max(known_chains, key=known_chains.get))
    print(time.time() - start)


if __name__ == "__main__":
    main()
