# SixSeven

A 2D Mario-style platformer built with Flask and vanilla JavaScript Canvas. Play as a farmer defending your garden — shoot carrots at enemies across **3 distinct levels**, each ending with a powerful boss fight.

**Play it live:** [opieeipo.github.io/SixSeven](https://opieeipo.github.io/SixSeven)

## How to Play

- **LEFT / RIGHT** — Move
- **UP** — Jump
- **DOWN** — Fast fall (while airborne)
- **SPACE** — Shoot carrots

## Game Features

### 3 Levels with Boss Fights
Each level has a unique visual theme and ends with a boss you must defeat before reaching the goal.

| Level | Theme | Boss | Boss HP | Boss Attacks |
|-------|-------|------|---------|--------------|
| 1 | The Garden | **Bunny King** | 8 | Hops, fires carrot spreads |
| 2 | Dark Forest | **Stone Golem** | 12 | Ground slams, shockwaves, drops rocks |
| 3 | Storm Sky | **Storm Lord** | 16 | Dive bombs, lightning strikes |

- Boss health bar displayed at top of screen during fight
- "BOSS INCOMING!" warning when you enter boss range
- Bosses enter an **enraged phase** at 50% HP (faster attacks, more projectiles)

### Platformer Mechanics
- Jump on and between platforms with full collision (land on top, bump head, side block)
- Camera scrolls to follow the player through the level
- Progress bar shows how far you are from the goal

### Enemy Types
| Enemy | Behavior | HP | Points |
|-------|----------|-----|--------|
| Bunny | Stationary | 1 | 10 |
| Tortoise | Slow, tracks player | 2 | 20 |
| Fox | Fast, charges when close | 1 | 15 |
| Crow | Flies overhead, swoops in waves | 1 | 15 |
| Bunny King (boss) | Hops + carrot spray | 8 | 150 |
| Stone Golem (boss) | Ground slam + rocks | 12 | 200 |
| Storm Lord (boss) | Dive bomb + lightning | 16 | 250 |

Enemy density and speed increase with each level. Level 2 has more foxes and tortoises; Level 3 swarms with fast foxes and crows.

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
- **Frontend**: Vanilla JavaScript with HTML5 Canvas
- **Sprites**: 16x16 pixel-art grids scaled 4x to 64x64 on screen
- **Deployment**: GitHub Pages (auto-deploys on push to main)

## Contributing

This project uses `@claude` via GitHub Actions. Authorized contributors can file issues with `@claude` to have changes implemented automatically. See the [workflow](.github/workflows/claude.yml) for details.

## Requirements

- Python 3.8+
- Flask 3.0+
