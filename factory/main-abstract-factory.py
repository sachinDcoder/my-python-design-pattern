from enum import Enum
from abc import ABC


class HotDrink(ABC):
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print(f'The tea is delicious')


class Coffee(HotDrink):
    def consume(self):
        print(f'The coffee is delicious')


class HotDrinkFactory(ABC):
    def prepare(self, amount):
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Put in tea bag, boil water, pour {amount}ml, enjoy!')
        return Tea()


class CoffeeFactory(HotDrinkFactory):
    def prepare(self, amount):
        print(f'Grind beans, boil water, pour {amount}ml, enjoy!')
        return Coffee()


class HotDrinkMachine:
    class AvailableDrink(Enum):
        COFFEE = 1
        TEA = 2

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                name = d.name[0] + d.name[1:].lower()
                factory_name = name + "Factory"
                factory_instance = eval(factory_name)
                self.factories.append((name, factory_instance))

    def make_drink(self):
        print(f'Here are the available options: ')
        for f in self.factories:
            print(f[0])

        inp = input(f'Please pick drink 0-{len(self.factories)-1}: ')
        idx = int(inp)
        inp = input(f'Specify amount: ')
        amount = int(inp)
        return self.factories[idx][1]().prepare(amount)


def make_drink(type):
    if type == 'Tea':
        return TeaFactory().prepare(200)
    elif type == 'Coffee':
        return CoffeeFactory().prepare(50)
    else:
        return None


def class_factory():
    hdm = HotDrinkMachine()
    drink = hdm.make_drink()
    drink.consume()


def func_factory():
    drink_type = input('What kind of drink you like to have? Tea/Coffee : ')
    drink = make_drink(drink_type)
    drink.consume()


def main():
    func_factory()
    class_factory()


if __name__ == "__main__":
    main()
