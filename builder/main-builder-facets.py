class Person:
    def __init__(self, name=''):
        self.name = name

        # Address
        self.street_address = None
        self.postcode = None
        self.city = None

        # Company
        self.company_name = None
        self.profile = None
        self.earning = None

    def __str__(self):
        return f'Name: {self.name} \n' \
               f'Address: {self.street_address}, {self.postcode}, {self.city} \n' \
               f'Company: {self.company_name} as a {self.profile} earning {self.earning}'


class PersonBuilder:
    def __init__(self, person=Person()):
        self.person = person

    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

    @property
    def works(self):
        return PersonJobBuilder(self.person)

    def build(self):
        return self.person


class PersonJobBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, company):
        self.person.company_name = company
        return self

    def as_a(self, profile):
        self.person.profile = profile
        return self

    def earning(self, earning):
        self.person.earning = earning
        return self


class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, street_address):
        self.person.street_address = street_address
        return self

    def with_postcode(self, postcode):
        self.person.postcode = postcode
        return self

    def in_city(self, city):
        self.person.city = city
        return self


def main():
    person_builder = PersonBuilder(Person('Sachin')) \
                    .lives \
                        .at('Jp Nagar') \
                        .with_postcode('560786') \
                        .in_city('Bangalore') \
                    .works \
                        .at('Vmware') \
                        .as_a('MTS-3') \
                        .earning('100$') \
                    .build()

    print(person_builder)


if __name__ == "__main__":
    main()
