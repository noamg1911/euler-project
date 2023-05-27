"""
Square Digit Chains
"""

import time

WRONG_FINISH_NUM = 1
RIGHT_FINISH_NUM = 89
ACCEPTABLE_FINISHES = (WRONG_FINISH_NUM, RIGHT_FINISH_NUM)
LIMIT = 10 ** 7


def create_new_num(num: int) -> int:
    """
    Gets the next number in the chain (as specified in the question, next number is the sum of the squared digits of the number)
    """
    new_num = 0
    while num:
        new_num += (num % 10) ** 2
        num //= 10
    return new_num


def create_memory_map(max_chain_num: int) -> tuple:
    """
    For every limit (i.e. 10 million), all the second numbers in the chain of each starting number up to the specified limit
    will get to a specific maximum chain number (i.e. 567). So instead of mapping each number to its finished number,
    we create a map of just the possible chain numbers (1-567). Saves time and memory.
    """
    current_amount_ending_in_right_finish = 0
    num_endings_map = {}
    for num in range(1, max_chain_num + 1):
        new_num = num
        chain_nums = [new_num]
        finish_num = 0
        while not finish_num:
            new_num = create_new_num(new_num)
            chain_nums.append(new_num)
            finish_num = num_endings_map[new_num] if num_endings_map.get(new_num) else \
                new_num if new_num in ACCEPTABLE_FINISHES else 0
        chain_nums.pop()
        for chain_num in chain_nums:
            num_endings_map[chain_num] = finish_num
        current_amount_ending_in_right_finish += (finish_num == RIGHT_FINISH_NUM)
    return num_endings_map, current_amount_ending_in_right_finish


def main():
    start = time.time()
    max_chain_num = create_new_num(LIMIT - 1)
    memory_map, amount_ending_in_right_finish = create_memory_map(max_chain_num)
    for num in range(max_chain_num + 1, LIMIT + 1):
        new_num = create_new_num(num)
        num_ending_value = memory_map[new_num]
        amount_ending_in_right_finish += (num_ending_value == RIGHT_FINISH_NUM)
    print(amount_ending_in_right_finish)
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
