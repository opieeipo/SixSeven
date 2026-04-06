# SixSeven

A 2D side-scrolling platformer built with Phaser 3 and Flask. Play as a farmer defending your garden -- shoot carrots at enemies across **6 distinct levels**, each ending with a powerful boss fight.

**Play it live:** [opieeipo.github.io/SixSeven](https://opieeipo.github.io/SixSeven)

## How to Play

- **LEFT / RIGHT** -- Move (character faces the direction you move)
- **UP** -- Jump
- **DOWN** -- Crouch (reduced hitbox, dodge projectiles)
- **SPACE** -- Shoot carrots (shoots in the direction you're facing)

## Game Features

### 6 Levels with Boss Fights
Each level has a unique visual theme and ends with a boss you must defeat before reaching the goal.

| Level | Theme | Boss | Boss HP | Boss Attacks |
|-------|-------|------|---------|--------------|
| 1 | The Garden | **Bunny King** | 8 | Carrot spreads, homing carrots, ground pound, summon minions, spiral shot |
| 2 | Dark Forest | **Stone Golem** | 12 | Shockwaves, rock rain, charge, ground crack, spinning rock shield, slow homing rocks |
| 3 | Storm Sky | **Storm Lord** | 16 | Lightning strikes, dive bombs, tornadoes, chain lightning, wind gusts, feather barrages, ball lightning |
| 4 | Underground Caves | **Cave Worm** | 10 | Emerge+snap, acid spit, acid spray arc, tail sweep, summon grubs |
| 5 | Volcanic Peaks | **Fire Drake** | 14 | Fireball spray, flame breath, dive+fire trail, wing buffet, meteor rain |
| 6 | Enchanted Ruins | **Ruin Knight** | 18 | Sword slash, shield charge, summon wolves, teleport+strike, magic orb barrage, spiral shot |

- Boss health bar displayed at top of screen during fight
- "BOSS INCOMING!" warning when you enter boss range
- Bosses enter an **enraged phase** at 50% HP (faster attacks, deadlier patterns)

### Player Health
- You have **5 HP** shown as hearts at the top of the screen
- Taking damage grants brief invincibility (flashing effect)
- Enemies have a chance to drop health pickups (hearts) when killed

### Platformer Mechanics
- Jump on and between platforms with full collision
- Crouch to reduce your hitbox and dodge attacks
- Shoot in both directions (left and right)
- Camera scrolls to follow the player through the level
- Progress bar shows how far you are from the goal

### Smart Enemy AI
| Enemy | Behaviors | HP | Points | Ammo Drop |
|-------|-----------|-----|--------|-----------|
| Bunny | Idle, hop toward, hop away, zigzag approach | 1 | 10 | +1 |
| Tortoise | Patrol, track player, shell retreat, stop-and-go, flank | 2 | 20 | +3 |
| Fox | Patrol, stalk, feint, zigzag charge, leap, ambush | 1 | 15 | +2 |
| Crow | Sine patrol, swoop dive (with weave), circle | 1 | 15 | +2 |

Enemies use randomized AI state machines so each encounter feels different. Difficulty scales across levels with faster speeds and more aggressive compositions.

### Ammo System
- You start each level with **30 carrots**
- Running out of ammo means you cannot shoot until you pick up drops
- Kill enemies to collect carrot pickups (bob on the ground where the enemy died)
- Ammo is capped at 99 and displayed in the HUD

### Scoring
- +1 point passively for surviving
- Bonus points per enemy and boss kill
- +100 points per level clear, +200 for final victory
- High score saved locally in your browser

## Running Locally

### macOS / Linux

```bash
./run.sh
```

### Windows

```cmd
run.bat
```

Both scripts create a virtual environment, install dependencies, and launch the game in your browser at `http://localhost:6578`.

### Manual

```bash
pip install -r requirements.txt
python app.py
```

## Tech Stack

- **Backend**: Python / Flask (serves a single HTML page, auto-opens browser)
- **Frontend**: Phaser 3.80.1 with Arcade Physics
- **Sprites**: PNG spritesheet with Phaser JSON atlas, scaled 4x on screen
- **Deployment**: GitHub Pages (auto-deploys on push to main)

## Contributing

This project uses `@claude` via GitHub Actions. Authorized contributors can file issues with `@claude` to have changes implemented automatically. See the [workflow](.github/workflows/claude.yml) for details.

## Requirements

- Python 3.8+
- Flask 3.0+
