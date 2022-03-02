"""
FileName: Names scores
Author: N.G 30.3.21
Purpose: Find the total of all the name scores in the file
"""

ASCII_DIFFERENCE = 64


def main():
    with open('euler22_text.txt', 'r') as names:
        name_list = sorted(names.read().split(','))
    for name in range(len(name_list)):
        name_list[name] = sum([ord(letter) - ASCII_DIFFERENCE for letter in name_list[name][1:-1]]) * (name + 1)
    print(sum(name_list))


if __name__ == "__main__":
    main()
