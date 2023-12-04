class Character:
    def __init__(self, hp, st, mc, dx):
        self.health_points = hp
        self.magic = mc
        self.strength = st
        self.dexterity = dx


class Warrior(Character):
    pass


class NoviceWarrior(Warrior):
    pass


class IntermediateWarrior(Warrior):
    pass


class AdvancedWarrior(Warrior):
    pass


class Mage(Character):
    pass


class NoviceMage(Warrior):
    pass


class IntermediateMage(Warrior):
    pass


class AdvancedMage(Warrior):
    pass


class Rogue(Character):
    pass


class NoviceRogue(Warrior):
    pass


class IntermediateRogue(Warrior):
    pass


class AdvancedRogue(Warrior):
    pass
