class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(".", end="")


# ^^ you are given this

# vv you are working with this

class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Rectangle(list):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.append(Line(Point(x, y), Point(x + width, y)))
        self.append(Line(Point(x + width, y), Point(x + width, y + height)))
        self.append(Line(Point(x + width, y + height), Point(x, y + height)))
        self.append(Line(Point(x, y), Point(x, y + height)))


class LineToPointAdapter(list):
    count = 0

    def __init__(self, line):
        super().__init__()
        self.count += 1
        print(f'{self.count}: Generating Points for Line '
              f'[{line.start.x, line.start.y}] -> [{line.end.x, line.end.y}]')

        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = max(line.start.y, line.end.y)
        bottom = min(line.start.y, line.end.y)

        if right - left == 0:
            for y in range(top, bottom):
                self.append(Point(left, y))
        if top - bottom == 0:
            for x in range(left, right):
                self.append(Point(x, top))


def draw(rectangles):
    print("---- Drawing ------")
    for rc in rectangles:
        for line in rc:
            adapter = LineToPointAdapter(line)
            for point in adapter:
                point.draw()


def main():
    rectangles = [
        Rectangle(1, 1, 10, 10),
        Rectangle(3, 3, 6, 6),
    ]

    draw(rectangles)


if __name__ == "__main__":
    main()

