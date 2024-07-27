class Creature:
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense

    def __str__(self):
        return f'Name: {self.name}, Attack: {self.attack} Defense: {self.defense}'


class CreatureModifier:
    def __init__(self, creature):
        self.creature = creature
        self.next_modifier = None

    def add_modifier(self, modifier):
        if self.next_modifier:
            self.next_modifier.add_modifier(modifier)
        else:
            self.next_modifier = modifier

    def handle(self):
        if self.next_modifier:
            self.next_modifier.handle()


class NoBonusModifier(CreatureModifier):
    def handle(self):
        print(f'No Bonus for {self.creature.name}')  # No call to super().handle() which means it stops the chain


class DoubleAttackModifier(CreatureModifier):
    def handle(self):
        print(f'Doubling creature {self.creature.name}\'s Attack')
        self.creature.attack *= 2
        super().handle()


class IncreaseDefenseModifier(CreatureModifier):
    def handle(self):
        if self.creature.attack <= 2:
            print(f'Increasing creature {self.creature.name}\'s Defense')
            self.creature.defense *= 2
        super().handle()


if __name__ == "__main__":
    goblin = Creature('Goblin', 1, 1)
    print(goblin)

    root = CreatureModifier(goblin)

    root.add_modifier(NoBonusModifier(goblin))

    root.add_modifier(DoubleAttackModifier(goblin))
    root.add_modifier(IncreaseDefenseModifier(goblin))
    root.add_modifier(DoubleAttackModifier(goblin))

    root.handle()  # Applying modifiers
    print(goblin)





