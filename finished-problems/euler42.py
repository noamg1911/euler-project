"""
FileName: Coded triangle numbers
Author: N.G 10.4.21
Purpose: Find how many words in the file (downloaded) are triangle words
"""

import time
import string


def main():
    start = time.time()

    with open('euler42_text.txt', 'r') as word_file:
        words_str = word_file.read()
    word_list = words_str.split(',')

    uppercase_list = string.ascii_uppercase
    for word in range(len(word_list)):
        curr_score = 0
        for letter in word_list[word][1:-1]:
            curr_score += uppercase_list.index(letter) + 1
        word_list[word] = curr_score

    triangles = [1]
    biggest_score = max(word_list)
    while triangles[-1] < biggest_score:
        triangles.append(triangles[-1] + len(triangles) + 1)

    num_triangle = 0
    for score in word_list:
        if score in triangles:
            num_triangle += 1

    print(num_triangle)
    print(time.time() - start)


if __name__ == "__main__":
    main()
