from enum import IntEnum, auto

class Trait(IntEnum):
    CLAN = 0
    ACE = auto()
    UNDEAD = auto()
    GOBLIN = auto()
    NOBLE = auto()
    BRAWLER = auto()
    RANGER = auto()
    BLASTER = auto()
    ASSASSIN = auto()
    BRUTALIST = auto()
    GIANT = auto()
    PEKKA = auto()
    SUPERSTAR = auto()

    @property
    def image(self) -> str:
        return f"images/traits/{self.name.lower()}.webp"