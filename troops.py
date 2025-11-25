from traits import Trait

class Troop():
    all_troops = set()
    instance_count = 0

    def __init__(self, cost: int, trait1: Trait, trait2: Trait, name: str, *aliases: str):
        self.cost = cost
        self.trait1 = trait1
        self.trait2 = trait2
        self.name = name
        self.all_names = (name,) + aliases
        self.meta_ranking = Troop.instance_count
        self.image = f"images/troops/{name}.webp"
        if name == "traitdummy": return
        Troop.all_troops.add(self)
        Troop.instance_count += 1
    
    def __repr__(self) -> str:
        return self.name

# Order the following troops from most useful to least useful
Troop(5,    Trait.CLAN,         Trait.RANGER,       "archerqueen", "aq", "queen")
Troop(4,    Trait.UNDEAD,       Trait.SUPERSTAR,    "witch")
Troop(5,    Trait.ACE,          Trait.SUPERSTAR,    "monk")
Troop(3,    Trait.ACE,          Trait.BLASTER,      "executioner")
Troop(2,    Trait.CLAN,         Trait.BRAWLER,      "barbarian")
Troop(3,    Trait.CLAN,         Trait.BRUTALIST,    "valkyrie")
Troop(2,    Trait.CLAN,         Trait.BLASTER,      "wizard")
Troop(3,    Trait.GIANT,        Trait.SUPERSTAR,    "electrogiant", "egiant")
Troop(3,    Trait.NOBLE,        Trait.SUPERSTAR,    "musketeer")
Troop(4,    Trait.ACE,          Trait.BRAWLER,      "megaknight")
Troop(3,    Trait.PEKKA,        Trait.BRAWLER,      "pekka")
Troop(5,    Trait.UNDEAD,       Trait.BRUTALIST,    "skeletonking", "skellyking")
Troop(3,    Trait.GOBLIN,       Trait.RANGER,       "dartgoblin")
Troop(2,    Trait.GOBLIN,       Trait.BLASTER,      "speargoblin")
Troop(2,    Trait.GOBLIN,       Trait.ASSASSIN,     "goblin")
Troop(4,    Trait.GOBLIN,       Trait.BRUTALIST,    "goblinmachine", "gmachine", "machine")
Troop(3,    Trait.NOBLE,        Trait.BRAWLER,      "prince")
Troop(5,    Trait.NOBLE,        Trait.ASSASSIN,     "goldenknight")
Troop(2,    Trait.PEKKA,        Trait.BRUTALIST,    "minipekka")
Troop(4,    Trait.NOBLE,        Trait.BLASTER,      "princess")
Troop(2,    Trait.GIANT,        Trait.RANGER,       "royalgiant", "rg")
Troop(2,    Trait.UNDEAD,       Trait.RANGER,       "skeletondragons", "skellydragons")
Troop(4,    Trait.ACE,          Trait.ASSASSIN,     "bandit")
Troop(4,    Trait.UNDEAD,       Trait.ASSASSIN,     "royalghost", "ghost")