"""
FileName:  Odd elimination
Author: N.G 16.5.21
Purpose: Find S(10 ** 18) mod 987654321 (S equation explained in question)
"""

import time
import numpy as np
import matplotlib.pyplot as plt

MODULO_NUM = 987654321
MAX_NUM = pow(10, 18)


def reznic_test_penis(num):
    power_of_2 = 1
    top = num - (num % 2)
    bottom = 2
    from_top = False
    while top != bottom:
        power_of_2 *= 2
        from_top = not from_top
        if from_top:
            if (top - bottom) % (2 * power_of_2) == 0:
                bottom += power_of_2
            top -= power_of_2
        else:
            if (top - bottom) % (2 * power_of_2) == 0:
                top -= power_of_2
            bottom += power_of_2
    return top


def main():
    start = time.time()
    p_values = []
    s_values = []
    sum_p = 0
    for num in range(2, 1025, 1):
        sum_p += reznic_test_penis(num)
        p_values.append(reznic_test_penis(num))
        s_values.append(sum_p)
    print(sum_p + 1)


    np.savetxt('euler539sum.csv', np.array(s_values))
    #print({x: p_values.count(x) for x in set(p_values)})
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
