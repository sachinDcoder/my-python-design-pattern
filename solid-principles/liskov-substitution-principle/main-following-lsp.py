class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def area(self):
        return self._width * self._height

    @property
    def width(self):
        return self._width

    @property
    def height(self):
        return self._height

    @width.setter
    def width(self, value):
        self._width = value

    @height.setter
    def height(self, value):
        self._height = value


# No longer a violation of LSP
class Square:
    def __init__(self, size):
        self._size = size

    @property
    def size(self):
        return self._size

    @property
    def area(self):
        return self._size * self._size

    @size.setter
    def size(self, value):
        _size = _height = value


def use_it(shape):
    if isinstance(shape, Rectangle):
        w = shape.width
        shape.height = 10  # No longer a violation of LSP
        expected_area = w * 10
        print(f'Expected: {expected_area}, got {shape.area}')
    elif isinstance(shape, Square):
        s = shape.size
        shape.size = 5 # Example of usage for Square
        expected_area = s * s
        print(f'Expected: {expected_area}, got {shape.area}')


def main():
    rectangle = Rectangle(2, 3)
    use_it(rectangle)

    square = Square(3)
    use_it(square)


if __name__ == "__main__":
    main()





