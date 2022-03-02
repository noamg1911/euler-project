"""
FileName: Coin sums
Author: N.G 2.4.31
Purpose: Find how many different ways can £2 be made using any number of coins
"""

import time
COIN_SUM = 200

# recursive solution (my original), 3.2 sec:


def check_combinations(coins: list, sum_to_get: int) -> int:
    combinations = 0
    curr_sum = 0
    while curr_sum <= sum_to_get:
        if curr_sum == sum_to_get:
            combinations += 1
        elif len(coins) > 1:
            combinations += check_combinations(coins[1:], sum_to_get - curr_sum)
        curr_sum += coins[0]
    return combinations


# quicker solution, 0 sec:
def main():
    start = time.time()
    coins = [1, 2, 5, 10, 20, 50, 100, 200]
    combinations = [1] + [0] * COIN_SUM
    for coin in coins:
        for curr_val in range(coin, COIN_SUM + 1):
            combinations[curr_val] += combinations[curr_val - coin]
    print(combinations[COIN_SUM])
    print(time.time() - start)


if __name__ == "__main__":
    main()
