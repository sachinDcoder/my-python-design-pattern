from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def __str__(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def resize(self, factor):
        self.radius *= factor

    def __str__(self):
        return f'A circle of radius {self.radius}'


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def __str__(self):
        return f'A square of side {self.side}'


class ColoredShape(Shape):
    def __init__(self, shape, color):
        if isinstance(shape, ColoredShape):
            raise ValueError('Cannot apply color twice')
        self.shape = shape
        self.color = color

    def __str__(self):
        return f'{self.shape} has the {self.color}'


class TransparentShape(Shape):
    def __init__(self, shape, transparency):
        self.shape = shape
        self.transparency = transparency

    def __str__(self):
        return f'{self.shape} has {self.transparency * 100}% transparency'


def main():
    circle = Circle(5)
    print(circle)

    red_circle = ColoredShape(circle, 'Red')
    print(red_circle)
    # Note: red_circle doesn't have resize like circle object

    half_transparent_red_circle = TransparentShape(red_circle, 0.5)
    print(half_transparent_red_circle)

    try:
        mixed_color = ColoredShape(ColoredShape(circle, 'Red'), 'Green')  # shouldn't be allowed
        print(mixed_color)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()

