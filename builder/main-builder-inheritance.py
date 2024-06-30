class Person:
    def __init__(self):
        self.name = None
        self.position = None
        self.dob = None

    def __str__(self):
        return f'{self.name} born on {self.dob} works as a {self.position}'

    @staticmethod
    def new():
        return PersonBuilder()


class PersonBuilder:
    def __init__(self):
        self.person = Person()

    def build(self):
        return self.person


class PersonInfoBuilder(PersonBuilder):
    def called(self, name):
        self.person.name = name
        return self


class PersonJobBuilder(PersonInfoBuilder):
    def works_as_a(self, position):
        self.person.position = position
        return self


class PersonDobBuilder(PersonJobBuilder):
    def born(self, dob):
        self.person.dob = dob
        return self


def main():
    person = PersonDobBuilder() \
        .called("Sachin") \
        .works_as_a("MTS-3") \
        .born("01/03/1997") \
        .build()

    print(person)


if __name__ == "__main__":
    main()
