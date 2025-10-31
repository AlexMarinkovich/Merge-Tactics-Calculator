from collections import Counter

from traits import Trait

class Troop:
    def __init__(self, cost: int, trait1: Trait, trait2: Trait, *names: str):
        self.cost = cost
        self.trait1 = trait1
        self.trait2 = trait2
        self.names = names

    def add_traits(self, trait_counter: Counter[Trait, int]):
        trait_counter[self.trait1] += 1
        trait_counter[self.trait2] += 1

    def subtract_traits(self, trait_counter: Counter[Trait, int]):
        trait_counter[self.trait1] -= 1
        trait_counter[self.trait2] -= 1
        if trait_counter[self.trait1] == 0: del trait_counter[self.trait1]
        if trait_counter[self.trait2] == 0: del trait_counter[self.trait2]

    def image_path(self) -> str:
        return f"images/troops/{self.names[0]}.webp"

    def __repr__(self):
        return f"{self.names[0]}"

ALL_TROOPS = {
    Troop(2,    Trait.CLAN,       Trait.BRAWLER,      "barbarian"),
    Troop(2,    Trait.CLAN,       Trait.RANGER,       "archer"),
    Troop(5,    Trait.CLAN,       Trait.AVENGER,      "archerqueen", "aq", "queen"),
    Troop(3,    Trait.CLAN,       Trait.JUGGERNAUT,   "valkyrie"),
    Troop(4,    Trait.ACE,        Trait.BRAWLER,      "megaknight"),
    Troop(3,    Trait.ACE,        Trait.BLASTER,      "executioner"),
    Troop(3,    Trait.ACE,        Trait.AVENGER,      "pekka"),
    Troop(4,    Trait.ACE,        Trait.ASSASSIN,     "bandit"),
    Troop(3,    Trait.ELECTRIC,   Trait.AVENGER,      "electrogiant", "egiant"),
    Troop(4,    Trait.ELECTRIC,   Trait.MAGE,         "electrowizard", "ewiz"),
    Troop(3,    Trait.UNDEAD,     Trait.BRAWLER,      "giantskeleton"),
    Troop(2,    Trait.UNDEAD,     Trait.RANGER,       "skeletondragons", "skellydragons"),
    Troop(4,    Trait.UNDEAD,     Trait.AVENGER,      "witch"),
    Troop(4,    Trait.UNDEAD,     Trait.ASSASSIN,     "royalghost"),
    Troop(5,    Trait.UNDEAD,     Trait.JUGGERNAUT,   "skeletonking", "skellyking"),
    Troop(3,    Trait.GOBLIN,     Trait.RANGER,       "dartgoblin"),
    Troop(2,    Trait.GOBLIN,     Trait.BLASTER,      "speargoblin"),
    Troop(2,    Trait.GOBLIN,     Trait.ASSASSIN,     "goblin"),
    Troop(4,    Trait.GOBLIN,     Trait.JUGGERNAUT,   "goblinmachine"),
    Troop(3,    Trait.NOBLE,      Trait.BRAWLER,      "prince"),
    Troop(4,    Trait.NOBLE,      Trait.RANGER,       "princess"),
    Troop(3,    Trait.NOBLE,      Trait.BLASTER,      "musketeer"),
    Troop(5,    Trait.NOBLE,      Trait.ASSASSIN,     "goldenknight"),
    Troop(2,    Trait.NOBLE,      Trait.JUGGERNAUT,   "knight"),
    Troop(4,    Trait.FIRE,       Trait.BLASTER,      "babydragon"),
    Troop(2,    Trait.FIRE,       Trait.MAGE,         "wizard")
}