from enum import StrEnum, auto

class Trait(StrEnum):
    CLAN = auto()
    ACE = auto()
    ELECTRIC = auto()
    UNDEAD = auto()
    GOBLIN = auto()
    NOBLE = auto()
    FIRE = auto()
    BRAWLER = auto()
    RANGER = auto()
    BLASTER = auto()
    AVENGER = auto()
    ASSASSIN = auto()
    JUGGERNAUT = auto()
    MAGE = auto()

    def __repr__(self):
        return f"{self.name}"