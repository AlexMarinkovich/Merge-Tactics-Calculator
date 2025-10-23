from collections import Counter

from traits import Trait

class Troop:
    def __init__(self, trait_1: Trait, trait_2: Trait, name: str | list[str]):
        self.trait_1 = trait_1
        self.trait_2 = trait_2
        self.names = name if isinstance(name, list) else [name]

    def add_traits(self, trait_counter: Counter[Trait, int]):
        trait_counter[self.trait_1] += 1
        trait_counter[self.trait_2] += 1

    def subtract_traits(self, trait_counter: Counter[Trait, int]):
        trait_counter[self.trait_1] -= 1
        trait_counter[self.trait_2] -= 1
        if trait_counter[self.trait_1] == 0: del trait_counter[self.trait_1]
        if trait_counter[self.trait_2] == 0: del trait_counter[self.trait_2]

    def image_path(self) -> str:
        return f"images/troops/{self.names[0]}.webp"

    def __repr__(self):
        return f"{self.names[0]}"

ALL_TROOPS = {
    Troop(Trait.CLAN,       Trait.BRAWLER,      "barbarian"),
    Troop(Trait.CLAN,       Trait.RANGER,       "archer"),
    Troop(Trait.CLAN,       Trait.AVENGER,      ["archerqueen", "aq", "queen"]),
    Troop(Trait.CLAN,       Trait.JUGGERNAUT,   "valkyrie"),
    Troop(Trait.ACE,        Trait.BRAWLER,      "megaknight"),
    Troop(Trait.ACE,        Trait.BLASTER,      "executioner"),
    Troop(Trait.ACE,        Trait.AVENGER,      "pekka"),
    Troop(Trait.ACE,        Trait.ASSASSIN,     "bandit"),
    Troop(Trait.ELECTRIC,   Trait.AVENGER,      "electrogiant"),
    Troop(Trait.ELECTRIC,   Trait.MAGE,         ["electrowizard", "ewiz"]),
    Troop(Trait.UNDEAD,     Trait.BRAWLER,      "giantskeleton"),
    Troop(Trait.UNDEAD,     Trait.RANGER,       ["skeletondragons", "skellydragons"]),
    Troop(Trait.UNDEAD,     Trait.AVENGER,      "witch"),
    Troop(Trait.UNDEAD,     Trait.ASSASSIN,     "royalghost"),
    Troop(Trait.UNDEAD,     Trait.JUGGERNAUT,   ["skeletonking", "sk"]),
    Troop(Trait.GOBLIN,     Trait.RANGER,       "dartgoblin"),
    Troop(Trait.GOBLIN,     Trait.BLASTER,      "speargoblin"),
    Troop(Trait.GOBLIN,     Trait.ASSASSIN,     "goblin"),
    Troop(Trait.GOBLIN,     Trait.JUGGERNAUT,   "goblinmachine"),
    Troop(Trait.NOBLE,      Trait.BRAWLER,      "prince"),
    Troop(Trait.NOBLE,      Trait.RANGER,       "princess"),
    Troop(Trait.NOBLE,      Trait.BLASTER,      "musketeer"),
    Troop(Trait.NOBLE,      Trait.ASSASSIN,     "goldenknight"),
    Troop(Trait.NOBLE,      Trait.JUGGERNAUT,   "knight"),
    Troop(Trait.FIRE,       Trait.BLASTER,      "babydragon"),
    Troop(Trait.FIRE,       Trait.MAGE,         "wizard")
}