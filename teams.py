from troops import Troop
from traits import Trait

class Team:
    __slots__ = ('troops', 'trait_dummy', 'traits', 'score', 'cost')

    TWO_TRAIT_SCORE = 2
    FOUR_TRAIT_SCORE = 5
    SIX_TRAIT_SCORE = 10

    score_map = [0, 0, TWO_TRAIT_SCORE, TWO_TRAIT_SCORE, FOUR_TRAIT_SCORE, FOUR_TRAIT_SCORE, SIX_TRAIT_SCORE]

    def __init__(self, troops: list[Troop], trait_dummy: Troop | None):
        self.troops: list[Troop] = troops
        self.trait_dummy: Troop = trait_dummy

        traits = [0] * len(Trait)
        for troop in self.troops:
            traits[troop.trait1] += 1
            traits[troop.trait2] += 1
        if trait_dummy:
            traits[trait_dummy.trait1] += 1
            traits[trait_dummy.trait2] += 1
        self.traits: list[int] = traits

        score = 0
        for count in self.traits:
            score += self.score_map[count]
        self.score: int = score 

        cost = 0
        for troop in self.troops:
            cost += troop.cost
        self.cost: int = cost