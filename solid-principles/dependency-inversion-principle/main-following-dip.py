from enum import Enum
from abc import ABC, abstractmethod


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipBrowser(ABC):
    @abstractmethod
    def find_all_children_of(self, name):
        pass


class Relationships(RelationshipBrowser):
    def __init__(self):
        self.relations = []

    def add_parent_and_child_relation(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.PARENT, parent)
        )

    def find_all_children_of(self, name):
        return filter(lambda relation: relation[0].name == name and relation[1] == Relationship.PARENT, self.relations)


class Research:
    def __init__(self, browser, person):
        for p in browser.find_all_children_of(person.name):
            print(f'{person.name} has a child called {p.name}')


def main():
    parent = Person('Virat')
    child1 = Person('Vamika')
    child2 = Person('Akaay')

    relationships = Relationships()
    relationships.add_parent_and_child_relation(parent, child1)
    relationships.add_parent_and_child_relation(parent, child2)

    Research(relationships, parent)


if __name__ == "__main__":
    main()