# SixSeven

A 2D side-scrolling platformer built with Phaser 3 and Flask. The player is a farmer who shoots carrots at enemies while navigating platforms across 6 themed levels, each ending with a boss fight.

## Tech Stack

- **Backend**: Python / Flask (serves a single HTML page)
- **Frontend**: Phaser 3.80.1 (loaded via CDN, no build step)
- **Sprites**: PNG spritesheet with Phaser JSON atlas, scaled 4x on screen
- **Port**: 6578 (not 5000, macOS AirPlay uses 5000)
- **Deployment**: GitHub Pages (auto-deploys on push to main)

## Project Structure

```
app.py                              # Flask server, auto-opens browser on launch
templates/index.html                # Entire game: Phaser scenes, physics, input, rendering
static/sprites/spritesheet.png      # Packed sprite PNG (19 sprites: characters, enemies, bosses, items)
static/sprites/phaser-atlas.json    # Phaser 3 texture atlas format
static/sprites/atlas.json           # Simple atlas (legacy/reference)
tools/export_sprites.py             # Pillow script to regenerate spritesheet from PNGs + new_sprites.py
tools/new_sprites.py                # Pixel art definitions for new sprites (jump, crouch, hearts, new bosses)
run.sh                              # macOS/Linux launcher (creates venv, installs deps, starts)
run.bat                             # Windows launcher
requirements.txt                    # Flask dependency
CLAUDE.md                           # This file
README.md                           # Public-facing docs (MUST be updated when game features change)
.github/workflows/claude.yml        # @claude GitHub Actions trigger
.github/workflows/deploy.yml        # Auto-deploy to GitHub Pages on push to main
```

## Architecture

The game uses Phaser 3 with Arcade Physics, loaded via CDN. All game code lives in `templates/index.html` in a single `<script>` block. No build step, no external JS files.

### Scenes

- **BootScene**: Loads spritesheet atlas. Transitions to MenuScene.
- **MenuScene**: Title screen, controls info, hi-score display. Space to start.
- **GameScene**: All gameplay for 6 levels with in-scene overlays for death/level complete/victory.

### Key Systems

- **Rendering**: Phaser 3 WebGL with `pixelArt: true` for crisp scaling
- **Physics**: Arcade Physics (gravity: 900). Player, enemies, and projectiles are physics sprites.
- **Sprites**: 19 sprites in `static/sprites/spritesheet.png` loaded as a Phaser atlas
- **Player**: 5 HP health system, directional facing (flipX), jump/crouch poses, invincibility frames on damage
- **Enemies**: 4 types (bunny, tortoise, fox, crow) with AI state machines and randomized behaviors
- **Bosses**: 6 bosses with weighted attack tables, enrage at 50% HP
- **Platforms**: Procedurally generated per level (~24 platforms)
- **Background**: Sky gradients, twinkling stars, parallax clouds, ground/grass/bushes via Phaser Graphics
- **Particles**: Phaser particle emitters for poof, dust, score popups, celebrations
- **UI**: Score, ammo, health hearts, progress bar, boss HUD (all fixed to camera)

### 6 Levels

| Level | Theme | Boss | Boss HP |
|-------|-------|------|---------|
| 1 | The Garden | Bunny King | 8 |
| 2 | Dark Forest | Stone Golem | 12 |
| 3 | Storm Sky | Storm Lord | 16 |
| 4 | Underground Caves | Cave Worm | 10 |
| 5 | Volcanic Peaks | Fire Drake | 14 |
| 6 | Enchanted Ruins | Ruin Knight | 18 |

### Enemy AI States

- **Bunny**: IDLE, HOP_TOWARD, HOP_AWAY
- **Tortoise**: PATROL, TRACK, SHELL_RETREAT, STOP_AND_GO
- **Fox**: PATROL, STALK, FEINT, ZIGZAG_CHARGE, LEAP
- **Crow**: SINE_PATROL, SWOOP_DIVE, CIRCLE

## Code Conventions

- Phaser 3 loaded via CDN (no npm/build step)
- All game code in a single HTML file
- Keep the retro pixel-art aesthetic (Press Start 2P font, dark sky themes)
- Sprites are 16x16 scaled 4x to 64px (bosses 24x24 scaled to 96px)
- High score persisted via `localStorage`

## Running

```bash
./run.sh          # or: python app.py
```

Opens browser automatically at http://localhost:6578

## When Making Changes

- Test that the game loads and Space starts it
- Verify sprites render correctly at proper scale
- Check collision with platforms and enemies
- To add new sprites: define in `tools/new_sprites.py`, run `py tools/export_sprites.py`, update atlas reference in game code
- Phaser handles world-space vs screen-space via camera; UI elements use `setScrollFactor(0)`
- **Always update README.md** when adding new game features, enemies, mechanics, or controls
