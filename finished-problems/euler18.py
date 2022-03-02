"""
FileName: Maximum path sum I (also works with II, euler 67)
Author: N.G 29.3.21
Purpose: Find the maximum total from top to bottom of the triangle
"""


def main():
    with open('euler18_text.txt', 'r') as triangle_file:
        triangle = [row.split() for row in triangle_file]
        for row in range(len(triangle)):
            triangle[row] = list(map(int, triangle[row]))

    for line in range(len(triangle) - 2, -1, -1):
        for number in range(len(triangle[line])):
            if triangle[line + 1][number] < triangle[line + 1][number + 1]:
                triangle[line][number] += triangle[line + 1][number + 1]
            else:
                triangle[line][number] += triangle[line + 1][number]
    print(triangle[0][0])


if __name__ == "__main__":
    main()
