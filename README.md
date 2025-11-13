# Merge Tactics Calculator — Input Guide
The program generates all valid teams in Clash Royale Merge Tactics, taking the following into account:
- Troops already in the team
- Excluded troops
- Trait dummies
- Trait requirements

It then scores each team based on active traits and displays the top results.

---

### Input Types
NOTE: Using prefixes for strings in the input is supported.

| Input Type | Syntax | Example | Meaning |
|-------------|---------|----------|----------|
| Troop | lowercase | `archer` | Ensures the troop is in the team |
| Exclude troop | `!` + lowercase | `!archer` | Ensures the troop is **not** in the team |
| Trait | UPPERCASE | `CLAN` | Requires **2** of this trait |
| Trait with count | number + UPPERCASE | `4CLAN` | Requires the given number of this trait |
| Exclude trait | `!` + UPPERCASE | `!CLAN` | Prohibits **2** of this trait |
| Exclude trait with count | `!` + number + UPPERCASE | `!4CLAN` | Prohibits the given number of this trait |
| Trait dummy | UPPERCASE + `:` + UPPERCASE | `FIRE:UNDEAD` | Adds a trait dummy with both traits |
| Team size | number | `7` | Sets the team size (default 6) |
| Sort ascending by cost | `-ascending` | `-a` | Prioritizes lower-cost teams when scores are tied |
| Sort descending by cost | `-descending` | `-d` | Prioritizes higher-cost teams when scores are tied |
| Display count | `-` + number | `-10` | Sets how many top teams to display (default 10) |
| Brute force | `-bruteforce` | `-b` | Search all troop combinations instead of ones with common traits. |

### Example

```
barb !goldenknight FIRE:BRAWL 4NOBLE
```
- Ensures `barbarian` is in the team
- Excludes `goldenknight` from the team
- Adds a trait dummy with `FIRE` and `BRAWLER` traits
- Requires at least 4 `NOBLE` trait troops

### Scoring System

- **2 traits** → 2 points  
- **4 traits** → 5 points  
- **6 or more traits** → 10 points