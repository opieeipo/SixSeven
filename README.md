# SixSeven

A 2D Mario-style platformer built with Flask and vanilla JavaScript Canvas. Play as a farmer defending your garden — shoot carrots at bunnies, tortoises, foxes, and crows as you navigate platforms to reach the goal.

**Play it live:** [opieeipo.github.io/SixSeven](https://opieeipo.github.io/SixSeven)

## How to Play

- **LEFT / RIGHT** — Move
- **UP** — Jump
- **DOWN** — Fast fall (while airborne)
- **SPACE** — Shoot carrots

## Game Features

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

Enemies grow in strength and variety as you progress through the level. Early zones have bunnies only, mid-level mixes in tortoises and foxes, and the final stretch adds crows.

### Scoring
- +1 point passively for surviving
- Bonus points per enemy type (see table above)
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
