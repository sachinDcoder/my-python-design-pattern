class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class PropertyObserver:
    def __init__(self):
        self.property_changed = Event()


class Person(PropertyObserver):
    def __init__(self, name, age=0):
        super().__init__()
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @property
    def can_vote(self):
        return self._age >= 18

    @age.setter
    def age(self, value):
        if self._age == value:
            return

        prev_can_vote = self.can_vote
        self._age = value
        self.property_changed('age', value)

        if prev_can_vote != self.can_vote:
            self.property_changed('can_vote', self.can_vote)


def main():
    def person_changed(name, value):
        if name == 'can_vote':
            print(f'Voting status changed to {value}')

    p = Person('Raja')
    p.property_changed.append(person_changed)

    for age in range(16, 22):
        print(f'Changing age to {age}')
        p.age = age


if __name__ == "__main__":
    main()

