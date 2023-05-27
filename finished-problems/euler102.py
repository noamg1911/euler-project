"""
See problem 102
"""

import time

TEXT_FILE = "text-files/euler102_text.txt"
MIN_COORDINATE = 0
MAX_COORDINATE = 1000


class Point:
    def __init__(self, coordinates: tuple):
        x, y = coordinates
        self.x = x
        self.y = y

    def __str__(self):
        return f"X: {self.x}, Y: {self.y}"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Side:
    def __init__(self, point_a: Point, point_b: Point):
        self.min_point, self.max_point = point_a, point_b
        if point_a.x > point_b.x:
            self.min_point, self.max_point = point_b, point_a
        try:
            self.slope = (self.max_point.y - self.min_point.y) / (self.max_point.x - self.min_point.x)
            self.b = self.min_point.y - self.min_point.x * self.slope
        except ZeroDivisionError:
            self.slope = "infinity"
            self.b = "Nope"


class Triangle:
    def __init__(self, points_coordinates: list):
        self.a, self.b, self.c = [Point(point) for point in points_coordinates]
        self.ab = Side(self.a, self.b)
        self.ac = Side(self.a, self.c)
        self.bc = Side(self.b, self.c)

    def __str__(self):
        return f"A: {self.a.x, self.a.y}, B: {self.b.x, self.b.y}, C: {self.c.x, self.c.y}\n"

    def is_origin_inside_triangle(self) -> bool:
        """
        Checks if the origin point (0,0) is inside the triangle. If it's inside, that means one of two things:
        1. the point itself is on one of the sides.
        2. there's only one(!) side that cuts the y-axis above the origin point.
        That's how I check if the origin point is inside the triangle.
        """
        sides = [self.ab, self.ac, self.bc]
        filtered_intersection_points = [side.b for side in sides
                                        if side.min_point.x <= MIN_COORDINATE <= side.max_point.x and side.b >= MIN_COORDINATE]
        return MIN_COORDINATE in filtered_intersection_points or len(filtered_intersection_points) == 1


def get_triangle_from_text_line(line: str) -> Triangle:
    """
    Takes a line of text with comma-separated numbers, and gets coordinates (and a triangle object) from them
    """
    split_line_to_numbers = [int(str_coordinate) for str_coordinate in line[:-1].split(',')]
    iter_line = iter(split_line_to_numbers)
    triangle_coordinates = [*zip(iter_line, iter_line)]
    return Triangle(triangle_coordinates)


def get_triangles_from_text_file() -> list:
    """
    Gets a text file with coordinates and converts them to triangle objects
    """
    with open(TEXT_FILE, 'r') as triangle_coordinates_file:
        triangles = [get_triangle_from_text_line(line) for line in triangle_coordinates_file]
    return triangles


def main():
    start = time.time()
    triangles = get_triangles_from_text_file()
    print(sum([triangle.is_origin_inside_triangle() for triangle in triangles]))
    print(f"Solution took {time.time() - start} seconds!")


if __name__ == "__main__":
    main()
