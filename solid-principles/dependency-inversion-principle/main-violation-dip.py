from enum import Enum


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class Relationships:
    def __init__(self):
        self.relations = []

    def add_parent_and_child_relation(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.PARENT, parent)
        )


# Violation of dependency inversion principle as strongly dependent on Relationships.relations (storage type), depended on low level module directly
class Research:
    def __init__(self, relationships, parent):
        relations = relationships.relations
        for r in relations:
            if r[0].name == parent.name and r[1] == Relationship.PARENT:
                print(f'{parent.name} has a child called {r[2].name}')


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