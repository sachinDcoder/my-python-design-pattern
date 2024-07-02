class CEO:
    __shared_state = {
        "name": "Sachin",
        "age": 27
    }

    def __init__(self):
        self.__dict__ = self.__shared_state

    def __str__(self):
        return f'{self.__shared_state["name"]} is {self.__shared_state["age"]} years old'


def main():
    ceo1 = CEO()
    print(ceo1)
    ceo2 = CEO()
    print(ceo2)

    ceo2.age = 65
    print(ceo1)
    print(ceo2)


if __name__ == "__main__":
    main()
