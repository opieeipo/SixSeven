# SixSeven

A simple 2D browser game built with Flask. Defend your garden by shooting carrots at invading bunnies — inspired by the Chrome dinosaur runner.

## How to Play

- **UP** — Jump
- **DOWN** — Fast fall
- **SPACE** — Shoot carrots

Bunnies scroll in from the right and get faster over time. Hit them with carrots for points, but don't let them touch you.

## Scoring

- +1 point passively for surviving
- +10 points per bunny hit
- High score saved locally in your browser

## Running

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

## Requirements

- Python 3.8+
- Flask 3.0+
