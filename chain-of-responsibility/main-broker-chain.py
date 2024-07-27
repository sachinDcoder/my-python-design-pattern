""""
1. Event Broker
2. Command Query Separation
3. Observer
"""
from enum import Enum
from abc import ABC


class Event(list):
    def __call__(self, *args, **kwargs):
        for item in self:
            item(*args, **kwargs)


class WhatToQuery(Enum):
    ATTACK = 1
    DEFENSE = 1


class Query:
    def __init__(self, creature_name, what_to_query, default_value):
        self.creature_name = creature_name
        self.what_to_query = what_to_query
        self.value = default_value  # Bidirectional


class Game:
    def __init__(self):
        self.queries = Event()

    def perform_query(self, sender, query):
        self.queries(sender, query)


class Creature:
    def __init__(self, game, name, attack, defense):
        self.game = game
        self.name = name
        self.initial_attack = attack
        self.initial_defense = defense

    @property
    def attack(self):
        query = Query(self.name, WhatToQuery.ATTACK, self.initial_attack)
        self.game.perform_query(self, query)
        return query.value

    @property
    def defense(self):
        query = Query(self.name, WhatToQuery.DEFENSE, self.initial_defense)
        self.game.perform_query(self, query)
        return query.value

    def __str__(self):
        return f'{self.name} ({self.attack}/{self.defense})'


class CreatureModifier(ABC):
    def __init__(self, game, creature):
        self.creature = creature
        self.game = game
        self.game.queries.append(self.handle)

    def handle(self, sender, query):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.game.queries.remove(self.handle)


class DoubleAttackModifier(CreatureModifier):
    def handle(self, sender, query):
        if sender.name == self.creature.name and query.what_to_query == WhatToQuery.ATTACK:
            query.value *= 2


class IncreaseDefenseModifier(CreatureModifier):
    def handle(self, sender, query):
        if sender.name == self.creature.name and query.what_to_query == WhatToQuery.DEFENSE:
            query.value += 3


def main():
    game = Game()
    goblin = Creature(game, "Goblin", 2, 2)
    print(goblin)

    with DoubleAttackModifier(game, goblin):
        print(goblin)
        with IncreaseDefenseModifier(game, goblin):
            print(goblin)

    print(goblin)


if __name__ == "__main__":
    main()


