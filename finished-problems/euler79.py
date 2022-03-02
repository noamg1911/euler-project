"""
FileName: Passcode derivation
Author: N.G 3.6.21
Purpose: Find the shortest passcode by analyzing the successful login attempts
"""

import time
# Firstly (and easier) done by hand

LENGTH_ATTEMPT = 3


def get_successful_login_attempts() -> list:
    """
    Gets the list of all the login attempts
    :return: The list of all login attempts (without twins of logins)
    """
    login_attempts = set()
    with open("euler79_text.txt") as login_file:
        for attempt in login_file:
            login_attempts.add(attempt[:-1])
    return sorted(login_attempts)


def add_digits_to_code(code: list, login_attempt: str):
    """
    Adds digits that aren't in the current code to the code
    :param code: The current code
    :param login_attempt: The current login attempt to match
    """
    for digit in login_attempt:
        if digit not in code:
            code.append(digit)


def make_code_match_attempt(code: list, login_attempt: str):
    """
    Makes the code match the current attempt
    :param code: The current code
    :param login_attempt: The current login attempt to match
    """
    add_digits_to_code(code, login_attempt)
    curr_index = code.index(login_attempt[0])

    for digit in range(1, LENGTH_ATTEMPT):
        while code.index(login_attempt[digit]) <= curr_index:
            digit_index = code.index(login_attempt[digit - 1])
            code[digit_index], code[digit_index - 1] =\
                code[digit_index - 1], code[digit_index]
            curr_index = code.index(login_attempt[digit - 1])

        curr_index = code.index(login_attempt[digit])


def main():
    start = time.time()
    login_attempts = get_successful_login_attempts()
    possible_code = list(login_attempts[0])
    for attempt in login_attempts:
        make_code_match_attempt(possible_code, attempt)

    print(''.join(possible_code))
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
