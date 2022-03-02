"""
FileName: XOR decryption
Author: N.G
Purpose: Find the sum of the ASCII values in the original (now decrypted) text
"""

import time
import string
from collections import Counter

MOST_COMMON_LETTER = ord(' ')
LEN_KEY = 3


def get_ascii_values_text(file_name: str) -> list:
    """
    Gets the numbers (ASCII values of encrypted text) of a text
    :param file_name: The name of the file to extract the numbers
    :return: A list of the numbers from the file
    """
    with open(file_name, 'r') as decrypted_file:
        ascii_values = decrypted_file.read().strip().split(',')
    return list(map(int, ascii_values))


def decrypt_text(text: list, key: list) -> tuple:
    """
    Decrypts a text with a given key
    :param text: The decrypted text
    :param key: The key (A list of the ASCII values of the keyword)
    :return: The decrypted text and the sum of its ASCII values
    """
    text_len = len(text)
    for letter in range(text_len):
        text[letter] = text[letter] ^ key[letter % LEN_KEY]
    return ''.join(list(map(chr, text))), sum(text)


def main():
    start = time.time()
    ascii_values = get_ascii_values_text('euler59_text.txt')
    letters_ascii = list(map(ord, string.ascii_lowercase))
    key = []

    for i in range(LEN_KEY):
        for letter in letters_ascii:
            curr_letters = []
            for text_letter in ascii_values[i::LEN_KEY]:
                curr_letters.append(text_letter ^ letter)
            if Counter(curr_letters).most_common()[0][0] == MOST_COMMON_LETTER:
                key.append(letter)
                break

    new_text, sum_ascii_text = decrypt_text(ascii_values, key)
    print(new_text)
    print(sum_ascii_text)
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
