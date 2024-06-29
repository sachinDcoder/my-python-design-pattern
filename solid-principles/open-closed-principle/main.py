from enum import Enum
from abc import ABC, abstractmethod


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


class Quality(Enum):
    GOOD = 1
    AVERAGE = 2
    ROTTEN = 3


class Product:
    def __init__(self, name, color, size, quality):
        self.name = name
        self.color = color
        self.size = size
        self.quality = quality

    def __repr__(self):
        return f'Product(name={self.name}, color={self.color}, size={self.size}, quality={self.quality})'


# Breaking Open and Close Principle
class ProductFilter:
    def filter_by_color(self, products, color):
        return list(filter(lambda product: product.color == color, products))

    def filter_by_size(self, products, size):
        return list(filter(lambda product: product.size == size, products))

    def filter_by_size_and_color(self, products, size, color):
        return list(filter(lambda product: product.color == color and product.size == size, products))

    def filter_by_size_and_color_and_quality(self, products, size, color, quality):
        return list(filter(lambda product: product.color == color and product.size == size and product.quality == quality, products))

    def filter_by_size_or_quality(self, products, size, quality):
        return list(filter(lambda product: product.size == size or product.quality == quality, products))


def without_ocp(products):
    product_filter = ProductFilter()
    print(product_filter.filter_by_color(products, Color.GREEN))
    print(product_filter.filter_by_size(products, Size.SMALL))
    print(product_filter.filter_by_size_and_color(products, Size.SMALL, Color.GREEN))
    print(product_filter.filter_by_size_and_color_and_quality(products, Size.MEDIUM, Color.GREEN, Quality.GOOD))
    print(product_filter.filter_by_size_or_quality(products, Size.SMALL, Quality.ROTTEN))


# Using Open and Closed Principle, implementation by Specification
class Specification(ABC):
    @abstractmethod
    def is_satisfied(self, item):
        pass

    def __and__(self, other):
        return AndSpecification(self, other)

    def __or__(self, other):
        return OrSpecification(self, other)


class Filter:
    @abstractmethod
    def filter(self, items, spec):
        pass


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return self.color == item.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return self.size == item.size


class QualitySpecification(Specification):
    def __init__(self, quality):
        self.quality = quality

    def is_satisfied(self, item):
        return self.quality == item.quality


class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(spec.is_satisfied(item) for spec in self.args)


class OrSpecification(Specification):
    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return any(spec.is_satisfied(item) for spec in self.args)


class BetterFilter:
    def filter(self, items, spec):
        return [item for item in items if spec.is_satisfied(item)]


def ocp(products):
    better_filter = BetterFilter()
    green = ColorSpecification(Color.GREEN)
    print(better_filter.filter(products, green))

    small = SizeSpecification(Size.SMALL)
    print(better_filter.filter(products, small))

    small_green = green & small
    print(better_filter.filter(products, small_green))

    good = QualitySpecification(Quality.GOOD)
    medium = SizeSpecification(Size.MEDIUM)
    medium_green_good = medium & green & good
    print(better_filter.filter(products, medium_green_good))

    rotten = QualitySpecification(Quality.ROTTEN)
    rotten_or_small = rotten | small
    print(better_filter.filter(products, rotten_or_small))


def main():
    apple = Product("apple", Color.GREEN, Size.MEDIUM, Quality.GOOD)
    grapes = Product("grapes", Color.GREEN, Size.SMALL, Quality.GOOD)
    berry = Product("berry", Color.BLUE, Size.SMALL, Quality.GOOD)
    banana = Product("berry", Color.GREEN, Size.MEDIUM, Quality.ROTTEN)
    products = [apple, grapes, berry, banana]

    print("Breaking Open and Close Principle")
    without_ocp(products)

    print()

    print("After using Open and Closed Principle, implementation by Specification")
    ocp(products)


if __name__ == "__main__":
    main()
