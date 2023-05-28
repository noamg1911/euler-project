"""
Roman Numerals
"""

import time

ROMAN_FILE = "text-files/euler89_roman.txt"
MAX_INT_NUMBER_LEN = 4
ROMAN_NUMBER_MAP = {
    "M": 1000,
    "D": 500,
    "C": 100,
    "L": 50,
    "X": 10,
    "V": 5,
    "I": 1
}


def get_roman_numerals() -> list:
    """
    Gets a list of Roman Numeral numbers from the given file
    """
    with open(ROMAN_FILE, 'r') as roman_file:
        roman_numbers = [number.rstrip() for number in roman_file]
    return roman_numbers


def roman_numeral_str_to_number(roman_number_string: str) -> int:
    """
    Turns a Roman numeral to its matching number (checks previous index to see if there was a substitution for 4,
    6 or 9, i.e. read IX as 9 instead of 11)
    """
    number = ROMAN_NUMBER_MAP[roman_number_string[0]]
    for index, letter in enumerate(roman_number_string[1:], start=1):
        curr_letter_val = ROMAN_NUMBER_MAP[letter]
        prev_letter_val = ROMAN_NUMBER_MAP[roman_number_string[index - 1]]
        number += curr_letter_val
        if curr_letter_val > prev_letter_val:
            number -= 2 * prev_letter_val
    return number


def number_to_len_of_minimal_roman_numeral(number: int) -> int:
    """
    Checks what's the minimal amount of characters needed for representing a number in Roman numeral form.
    Skips the first index because even 4 M's are MMMM (and not a short version like in other numbers).
    """
    digits = str(number)
    starting_digit = MAX_INT_NUMBER_LEN - len(str(number))
    minimal_len = 0
    for index, digit in enumerate(digits, start=starting_digit):
        num_digit = int(digit)
        if index == 0:
            minimal_len += num_digit
            continue
        if num_digit in [0, 1, 2, 3, 7]:
            minimal_len += num_digit % 4
        elif num_digit in [4, 6, 9]:
            minimal_len += 2
        elif num_digit == 5:
            minimal_len += 1
        elif num_digit == 8:
            minimal_len += 4
    return minimal_len


def main():
    start = time.time()
    numerals = get_roman_numerals()
    characters_saved = 0
    for numeral in numerals:
        file_roman_number_length = len(numeral)
        numeral_as_int = roman_numeral_str_to_number(numeral)
        minimal_roman_number_length = number_to_len_of_minimal_roman_numeral(numeral_as_int)
        characters_saved += file_roman_number_length - minimal_roman_number_length
    print(characters_saved)
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
