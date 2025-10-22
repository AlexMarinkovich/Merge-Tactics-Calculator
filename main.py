from traits import Trait as T
from prefix_tree import Trie
from collections import Counter

# Part 1: Defining Troops and building the Trie
class Troop:
    trie = Trie()

    def __init__(self, trait_1: T, trait_2: T, name: str | list[str]):
        self.trait_1 = trait_1
        self.trait_2 = trait_2

        self.names = name if isinstance(name, list) else [name]
        for n in self.names:
            Troop.trie.insert(n, self)  

    def add_traits(self, trait_counter: Counter[T, int]) -> None:
        trait_counter[self.trait_1] += 1
        trait_counter[self.trait_2] += 1

    def subtract_traits(self, trait_counter: Counter[T, int]) -> None:
        trait_counter[self.trait_1] -= 1
        trait_counter[self.trait_2] -= 1
        if trait_counter[self.trait_1] == 0: del trait_counter[self.trait_1]
        if trait_counter[self.trait_2] == 0: del trait_counter[self.trait_2]

    def __repr__(self):
        return f"{self.names[0]}"

all_troops = {
    Troop(T.CLAN,       T.BRAWLER,      "barbarian"),
    Troop(T.CLAN,       T.RANGER,       "archer"),
    Troop(T.CLAN,       T.AVENGER,      ["archerqueen", "aq"]),
    Troop(T.CLAN,       T.JUGGERNAUT,   "valkyrie"),
    Troop(T.ACE,        T.BRAWLER,      "megaknight"),
    Troop(T.ACE,        T.BLASTER,      "executioner"),
    Troop(T.ACE,        T.AVENGER,      "pekka"),
    Troop(T.ACE,        T.ASSASSIN,     "bandit"),
    Troop(T.ELECTRIC,   T.AVENGER,      "electrogiant"),
    Troop(T.ELECTRIC,   T.MAGE,         ["electrowizard", "ewiz"]),
    Troop(T.UNDEAD,     T.BRAWLER,      "giantskeleton"),
    Troop(T.UNDEAD,     T.RANGER,       ["skeletondragons", "skellydragons"]),
    Troop(T.UNDEAD,     T.AVENGER,      "witch"),
    Troop(T.UNDEAD,     T.ASSASSIN,     "royalghost"),
    Troop(T.UNDEAD,     T.JUGGERNAUT,   ["skeletonking", "sk"]),
    Troop(T.GOBLIN,     T.RANGER,       "dartgoblin"),
    Troop(T.GOBLIN,     T.BLASTER,      "speargoblin"),
    Troop(T.GOBLIN,     T.ASSASSIN,     "goblin"),
    Troop(T.GOBLIN,     T.JUGGERNAUT,   "goblinmachine"),
    Troop(T.NOBLE,      T.BRAWLER,      "prince"),
    Troop(T.NOBLE,      T.RANGER,       "princess"),
    Troop(T.NOBLE,      T.BLASTER,      "musketeer"),
    Troop(T.NOBLE,      T.ASSASSIN,     "goldenknight"),
    Troop(T.NOBLE,      T.JUGGERNAUT,   "knight"),
    Troop(T.FIRE,       T.BLASTER,      "babydragon"),
    Troop(T.FIRE,       T.MAGE,         "wizard")
}
current_troops: set[Troop] = set()
excluded_troops: set[Troop] = set()

T.trie = Trie()
for trait in T:
    T.trie.insert(trait.name.lower(), trait)

# Part 2: Getting the current composition by input
trait_counter = Counter()

for troop_name in input("Current troops: ").split(" "):
    if not troop_name.strip(): continue  # skip whitespace inputs

    # Handling trait dummies
    if len(troop_name) >= 3 and troop_name[:3] == "td:":
        for trait_name in troop_name[3:].split(","):
            trait = T.trie.search_with_fallback(trait_name)
            if not trait: raise ValueError(f"Trait '{trait_name}' not found")
            trait_counter[trait] += 1
        continue

    # Handling troop exclusions
    exclude = False
    if troop_name and troop_name[0] == "!":
        troop_name = troop_name[1:]
        exclude = True

    # Finding the troop using the Troop Trie
    troop = Troop.trie.search_with_fallback(troop_name)
    if troop in current_troops or troop in excluded_troops: raise ValueError(f"Troop '{troop_name}' is already included/excluded")  # prevent duplicates
    if not troop: raise ValueError(f"Troop '{troop_name}' not found")  # troop not found
    if exclude: excluded_troops.add(troop)
    else:
        current_troops.add(troop)
        troop.add_traits(trait_counter)

# Part 3: Define the scoring method for compositions
TWO_TRAIT_SCORE = 2
FOUR_TRAIT_SCORE = 5
SIX_TRAIT_SCORE = 10

def composition_score(trait_counter: Counter[T, int]) -> int:
    score = 0
    for count in trait_counter.values():
        if count == 2 or count == 3: score += TWO_TRAIT_SCORE
        if count == 4 or count == 5: score += FOUR_TRAIT_SCORE
        if count >= 6: score += SIX_TRAIT_SCORE
    return score

# Part 4: Backtracking to find all compositions
MAX_TROOPS = 6
potential_troops = list(all_troops - current_troops - excluded_troops)
current_troops = list(current_troops)
all_compositions = []

def backtrack(start: int):
    if len(current_troops) == MAX_TROOPS:
        all_compositions.append((composition_score(trait_counter), current_troops.copy(), trait_counter.copy()))
        return

    for i in range(start, len(potential_troops)):
        current_troops.append(potential_troops[i])
        potential_troops[i].add_traits(trait_counter)
        backtrack(i + 1)
        current_troops.pop()
        potential_troops[i].subtract_traits(trait_counter)

backtrack(0)
print(f"{len(all_compositions)} compositions found.")

# Part 5: Sorting and displaying the best compositions
best_compositions = sorted(all_compositions, key=lambda x: x[0], reverse=True)
print(*best_compositions[:10], sep="\n")