"""
FileName: Largest palindrome product
Author: N.G 28.3.21
Purpose: Find the largest palindrome made from the product of two 3-digit numbers
"""
import time
UPPER_NUM = 999
LOWER_NUM = 100
UPPER_LIMIT = UPPER_NUM ** 2 - 2
LOWER_LIMIT = LOWER_NUM ** 2


def check_if_palindrome(string_num: str) -> bool:
    """
    checks if a number is a palindrome
    :param string_num: the string of the number to be checked
    :return: True if it is, False otherwise
    """
    return True if string_num == string_num[::-1] else False


def check_if_product_three_digit(num: int) -> bool:
    """
    checks if a number is a product of two three digit numbers
    :param num: the number to be checked
    :return: True if it is, False otherwise
    """
    for divisor in range(UPPER_NUM, LOWER_NUM, -1):
        if num % divisor == 0 and LOWER_NUM < (num / divisor) < UPPER_NUM:
            return True
    return False


def main():
    start = time.time()
    for num in range(UPPER_LIMIT, LOWER_LIMIT, -10):
        if str(num)[0] != str(num)[-1]:
            num -= 1
        if check_if_palindrome(str(num)) and check_if_product_three_digit(num):
            print(num)
            print(time.time() - start)
            break


if __name__ == "__main__":
    main()
