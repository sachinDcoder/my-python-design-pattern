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


class LineToPointAdapter:
    cache = {}

    def __init__(self, line):
        super().__init__()
        self.h = hash(line)
        if self.h in self.cache:
            return

        print(f'Generating Points for Line '
              f'[{line.start.x, line.start.y}] -> [{line.end.x, line.end.y}]')

        left = min(line.start.x, line.end.x)
        right = max(line.start.x, line.end.x)
        top = max(line.start.y, line.end.y)
        bottom = min(line.start.y, line.end.y)

        points = []

        if right - left == 0:
            for y in range(bottom, top + 1):
                points.append(Point(left, y))
        if top - bottom == 0:
            for x in range(left, right + 1):
                points.append(Point(x, top))

        self.cache[self.h] = points

    def __iter__(self):
        return iter(self.cache[self.h])


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
    draw(rectangles)


if __name__ == "__main__":
    main()

