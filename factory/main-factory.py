from enum import Enum
from math import sin, cos


# It violates the open and closed principle as we add new CoordinateSystem
class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    def __init__(self, a, b):
        self.x = a
        self.y = b

    @staticmethod
    def new_cartesian_point(x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * sin(theta), theta * cos(rho))

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'


def main():
    cartesian_point1 = Point(2, 3)
    cartesian_point2 = Point.new_cartesian_point(2, 3)
    polar_point2 = Point.new_polar_point(2, 3)
    print(cartesian_point1)
    print(cartesian_point2)
    print(polar_point2)


if __name__ == "__main__":
    main()
