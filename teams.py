from troops import Troop
from traits import Trait

class Team:
    __slots__ = ('troops', 'trait_dummy', 'traits', 'score', 'cost', 'meta_ranking')

    TWO_TRAIT_SCORE = 2
    FOUR_TRAIT_SCORE = 5
    SIX_TRAIT_SCORE = 10

    score_map = [0, 0, TWO_TRAIT_SCORE, TWO_TRAIT_SCORE, FOUR_TRAIT_SCORE, FOUR_TRAIT_SCORE, SIX_TRAIT_SCORE]

    def __init__(self, troops: list[Troop], trait_dummy: Troop | None):
        traits = [0] * len(Trait)
        cost = 0
        meta_ranking = 0

        for troop in troops:
            cost += troop.cost
            meta_ranking += troop.meta_ranking
            traits[troop.trait1] += 1
            traits[troop.trait2] += 1

        if trait_dummy:
            traits[trait_dummy.trait1] += 1
            traits[trait_dummy.trait2] += 1

        score = 0
        for count in traits:
            score += Team.score_map[count]
        
        self.troops: list[Troop] = troops
        self.trait_dummy: Troop = trait_dummy
        self.traits: list[int] = traits
        self.score: int = score 
        self.cost: int = cost
        self.meta_ranking: int = meta_ranking