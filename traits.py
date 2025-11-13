from enum import IntEnum, auto

class Trait(IntEnum):
    CLAN = 0
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

    @property
    def image(self) -> str:
        return f"images/traits/{self.name.lower()}.webp"