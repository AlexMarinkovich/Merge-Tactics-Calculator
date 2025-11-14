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
Troop(3,    Trait.ACE,        Trait.BLASTER,      "executioner")
Troop(2,    Trait.CLAN,       Trait.BRAWLER,      "barbarian")
Troop(2,    Trait.CLAN,       Trait.RANGER,       "archer")
Troop(5,    Trait.CLAN,       Trait.AVENGER,      "archerqueen", "aq", "queen")
Troop(3,    Trait.CLAN,       Trait.JUGGERNAUT,   "valkyrie")
Troop(4,    Trait.ACE,        Trait.BRAWLER,      "megaknight")
Troop(3,    Trait.ACE,        Trait.AVENGER,      "pekka")
Troop(3,    Trait.UNDEAD,     Trait.BRAWLER,      "giantskeleton", "gskeleton")
Troop(4,    Trait.UNDEAD,     Trait.AVENGER,      "witch")
Troop(2,    Trait.NOBLE,      Trait.JUGGERNAUT,   "knight")
Troop(5,    Trait.UNDEAD,     Trait.JUGGERNAUT,   "skeletonking", "skellyking")
Troop(3,    Trait.GOBLIN,     Trait.RANGER,       "dartgoblin")
Troop(2,    Trait.GOBLIN,     Trait.BLASTER,      "speargoblin")
Troop(2,    Trait.GOBLIN,     Trait.ASSASSIN,     "goblin")
Troop(4,    Trait.GOBLIN,     Trait.JUGGERNAUT,   "goblinmachine", "gmachine", "machine")
Troop(3,    Trait.NOBLE,      Trait.BRAWLER,      "prince")
Troop(3,    Trait.NOBLE,      Trait.BLASTER,      "musketeer")
Troop(5,    Trait.NOBLE,      Trait.ASSASSIN,     "goldenknight")
Troop(4,    Trait.ACE,        Trait.ASSASSIN,     "bandit")
Troop(4,    Trait.FIRE,       Trait.BLASTER,      "babydragon")
Troop(2,    Trait.FIRE,       Trait.MAGE,         "wizard")
Troop(4,    Trait.ELECTRIC,   Trait.MAGE,         "electrowizard", "ewiz")
Troop(4,    Trait.NOBLE,      Trait.RANGER,       "princess")
Troop(4,    Trait.UNDEAD,     Trait.ASSASSIN,     "royalghost", "ghost")
Troop(3,    Trait.ELECTRIC,   Trait.AVENGER,      "electrogiant", "egiant")
Troop(2,    Trait.UNDEAD,     Trait.RANGER,       "skeletondragons", "skellydragons")