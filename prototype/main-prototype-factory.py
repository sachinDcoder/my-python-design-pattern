import copy


class Address:
    def __init__(self, street_address, suite, city):
        self.street_address = street_address
        self.suite = suite
        self.city = city

    def __str__(self):
        return f'{self.street_address}, Suite: #{self.suite}, {self.city}'


class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f'{self.name} works at {self.address}'


class EmployeeFactory:
    main_office_employee = Employee('', Address('Bridge Road Phase 1', 0, 'Bangalore'))
    aux_office_employee = Employee('', Address('Bridge Road Phase 2', 0, 'Bangalore'))

    @staticmethod
    def __new_employee(prototype, name, suite):
        new_employee = copy.deepcopy(prototype)
        new_employee.name = name
        new_employee.address.suite = suite
        return new_employee

    @staticmethod
    def new_main_office_employee(name, suite):
        return EmployeeFactory.__new_employee(EmployeeFactory.main_office_employee, name, suite)

    @staticmethod
    def new_aux_office_employee(name, suite):
        return EmployeeFactory.__new_employee(EmployeeFactory.aux_office_employee, name, suite)


def main():
    sachin = EmployeeFactory.new_main_office_employee('Sachin', '456')
    raja = EmployeeFactory.new_aux_office_employee('Raja', '987')

    print(sachin)
    print(raja)


if __name__ == "__main__":
    main()


