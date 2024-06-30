from enum import Enum
from math import sin, cos


# It violates the open and closed principle as we add new CoordinateSystem
class CoordinateSystem(Enum):
    CARTESIAN = 1
    POLAR = 2


class Point:
    def __init__(self, a, b, system=CoordinateSystem.CARTESIAN):
        if system == CoordinateSystem.CARTESIAN:
            self.x = a
            self.y = b
        elif system == CoordinateSystem.POLAR:
            self.x = a * sin(b)
            self.y = b * cos(a)

    def __str__(self):
        return f'x: {self.x}, y: {self.y}'


def main():
    p1 = Point(2, 3)
    p2 = Point(2, 3, CoordinateSystem.POLAR)
    print(p1)
    print(p2)


if __name__ == "__main__":
    main()
