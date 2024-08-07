from abc import ABC, abstractmethod


class Renderer(ABC):
    @abstractmethod
    def render_circle(self, radius):
        pass


class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing a circle of radius {radius}')


class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing pixels for a circle of radius {radius}')


class Shape:
    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self):
        pass

    def resize(self, factor):
        pass


class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

    def resize(self, factor):
        self.radius *= factor


def main():
    raster = RasterRenderer()
    vector = VectorRenderer()
    circle = Circle(vector, 5)
    circle.draw()
    circle.resize(10)
    circle.draw()

    circle = Circle(raster, 6)
    circle.draw()
    circle.resize(20)
    circle.draw()


if __name__ == "__main__":
    main()
