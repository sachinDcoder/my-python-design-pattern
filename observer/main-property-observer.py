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

    @age.setter
    def age(self, value):
        if self._age == value:
            return
        self._age = value
        self.property_changed('age', value)


class TrafficAuthority:
    def __init__(self, person):
        self.person = person
        person.property_changed.append(self.person_age_changed)

    def person_age_changed(self, name, age):
        if name == 'age':
            if age < 18:
                print(f'You are not allowed to drive.')
            else:
                print(f'You can drive now.')
                self.person.property_changed.remove(self.person_age_changed)


def main():
    p = Person('Raja')
    ta = TrafficAuthority(p)
    for age in range(15, 21):
        print(f'Setting age to {age}')
        p.age = age


if __name__ == "__main__":
    main()

