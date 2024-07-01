from enum import Enum
from math import sin, cos


class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    def __init__(self, a, b):
        self.x = a
        self.y = b

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'

    class PointFactory:
        def new_cartesian_point(self, x, y):
            return Point(x, y)

        def new_polar_point(self, rho, theta):
            return Point(rho * sin(theta), theta * cos(rho))

    factory = PointFactory()


def main():
    cartesian_point1 = Point(2, 3)
    cartesian_point2 = Point.factory.new_cartesian_point(2, 3)
    polar_point2 = Point.factory.new_polar_point(2, 3)
    print(cartesian_point1)
    print(cartesian_point2)
    print(polar_point2)


if __name__ == "__main__":
    main()
