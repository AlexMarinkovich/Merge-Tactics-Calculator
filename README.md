# Merge Tactics Calculator — Input Guide
The program generates all valid compositions, taking your input into account:  
- Troops already in the team
- Excluded troops
- Trait dummies  
- Trait requirements (including counts)  

It then scores each composition based on active traits and displays the top results.

---

### Input Types

| Input Type | Syntax | Example | Meaning |
|------------|--------|---------|--------|
| Troop | lowercase | `archer` | Ensures the troop is in the team |
| Exclude troop | `!` + lowercase | `!archer` | Ensures the troop is **not** in the team |
| Trait | UPPERCASE | `CLAN` | Requires **2** of this trait |
| Trait with count | UPPERCASE + number | `CLAN4` | Requires the given number of this trait |
| Trait dummy | `TD:` + TRAIT1 + `:` + TRAIT2 | `TD:FIRE:UNDEAD` | Adds a trait dummy with both traits |

### Example

```
!goldenknight archer TD:FIRE:BRAWLER NOBLE
```
- Excludes `goldenknight` from the team
- Ensures `archer` is in the team
- Adds a trait dummy with `FIRE` and `BRAWLER` traits
- Requires at least 4 `NOBLE` trait troops

### Scoring System

- **2 traits** → 2 points  
- **4 traits** → 5 points  
- **6 or more traits** → 10 points