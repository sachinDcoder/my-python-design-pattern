
class Monostate:
    __shared_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__shared_state
        return obj


class CFO(Monostate):

    def __init__(self):
        self.name = ''
        self.money_manged = 0

    def __str__(self):
        return f'{self.name} manages ₹{self.money_manged}'


def main():
    cfo1 = CFO()
    cfo1.name = "Sachin"
    cfo1.money_manged = 10
    print(cfo1)

    cfo2 = CFO()
    cfo1.name = "Raja"
    cfo1.money_manged = 77
    print(cfo1)
    print(cfo2)

    cfo2.money_manged = 99
    print(cfo1)
    print(cfo2)


if __name__ == "__main__":
    main()
