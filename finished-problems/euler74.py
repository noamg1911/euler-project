"""
FileName: Digit factorial chains
Author: N.G 21.5.21
Purpose: Find how many digit factorial chains (explained in question),
         with a starting number below one million, contain exactly sixty
         non-repeating terms
"""

import time

LIMIT = pow(10, 6)
NUM_DIGITS = 10
NUM_REPETITIONS = 60


def get_digit_factorials() -> dict:
    """
    Gets the factorial of every digit
    :return: The dictionary of every digit and its factorial value
    """
    digit_factorials = {'0': 1}
    for digit in range(1, NUM_DIGITS):
        digit_factorials[str(digit)] = digit_factorials[str(digit - 1)] * digit
    return digit_factorials


def main():
    start = time.time()
    factorials = get_digit_factorials()
    known_chains = {1: 2}
    num_max_repetitions = 0

    for num in range(1, LIMIT):
        chain = [num]
        next_link = num

        while next_link not in known_chains and next_link not in chain[:-1]:
            string_link = str(next_link)
            next_link = 0
            for digit in string_link:
                next_link += factorials[digit]
            chain.append(next_link)

        num_chain = len(chain) - 1
        if next_link in known_chains:
            num_chain += known_chains[next_link]

        for link_index in range(1, len(chain) - 1):
            known_chains[chain[link_index]] = num_chain - link_index

        known_chains[num] = num_chain
        if known_chains[num] >= NUM_REPETITIONS:
            num_max_repetitions += 1

    print(num_max_repetitions)
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
