"""
FileName: Number spiral diagonals
Author: N.G 1.4.21
Purpose: Find the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way (in q)
"""

NUM_SIDES = 4
SPIRAL_SIZE = 1001


def main():
    total_sum = 1
    difference = 2
    curr_num = total_sum
    while difference != SPIRAL_SIZE + 1:
        for i in range(NUM_SIDES):
            curr_num += difference
            total_sum += curr_num
        difference += 2
    print(total_sum)


if __name__ == "__main__":
    main()
