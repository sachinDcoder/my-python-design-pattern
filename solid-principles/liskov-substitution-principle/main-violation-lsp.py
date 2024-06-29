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


# Violation of Liskov Substitution Principle
class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        _width = _height = value

    @Rectangle.height.setter
    def height(self, value):
        _width = _height = value


def use_it(rectangle):
    w = rectangle.width
    rectangle.height = 10  # unpleasant side effect, Violation of Liskov Substitution Principle
    expected_area = int(w * 10)
    print(f'Expected: {expected_area}, got {rectangle.area}')


def main():
    rectangle = Rectangle(2, 3)
    use_it(rectangle)

    square = Square(3)
    use_it(square)


if __name__ == "__main__":
    main()





