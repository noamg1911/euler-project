"""
Eulercoin
"""

import time

MULTIPLIED_NUM = 1504170115041707
MODULO_NUM = 4503599627370517


def main():
    start = time.time()
    coins = [MULTIPLIED_NUM]
    smallest_coin = MULTIPLIED_NUM
    current_num = 0
    current_multiplication_factor = 0
    max_multiplication_factor = current_multiplication_factor
    while True:
        current_num += MULTIPLIED_NUM
        current_multiplication_factor += 1
        current_modulo = current_num % MODULO_NUM
        if current_modulo < smallest_coin:
            coins.append(current_modulo)
            smallest_coin = current_modulo
            max_multiplication_factor = current_multiplication_factor
            print(current_multiplication_factor, coins)
        if current_multiplication_factor - max_multiplication_factor > MULTIPLIED_NUM:
            break
    print(sum(coins))
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
