from enum import Enum

class Trait(Enum):
    CLAN = "CLAN"
    ACE = "ACE"
    ELECTRIC = "ELECTRIC"
    UNDEAD = "UNDEAD"
    GOBLIN = "GOBLIN"
    NOBLE = "NOBLE"
    FIRE = "FIRE"
    BRAWLER = "BRAWLER"
    RANGER = "RANGER"
    BLASTER = "BLASTER"
    AVENGER = "AVENGER"
    ASSASSIN = "ASSASSIN"
    JUGGERNAUT = "JUGGERNAUT"
    MAGE = "MAGE"

    def __repr__(self):
        return self.name

    def image_path(self) -> str:
        return f"images/traits/{self.name.lower()}.webp"