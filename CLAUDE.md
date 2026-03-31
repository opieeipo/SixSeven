# SixSeven

A 2D Mario-style platformer built with Flask and vanilla JavaScript Canvas. The player is a farmer who shoots carrots at enemies while navigating platforms to reach a goal.

## Tech Stack

- **Backend**: Python / Flask (serves a single HTML page)
- **Frontend**: Vanilla JavaScript with HTML5 Canvas (no frameworks, no build step)
- **Sprites**: 16x16 pixel-art grids defined as color-index arrays, scaled 4x to 64x64 on screen
- **Port**: 6578 (not 5000, macOS AirPlay uses 5000)
- **Deployment**: GitHub Pages (auto-deploys on push to main)

## Project Structure

```
app.py                          # Flask server, auto-opens browser on launch
templates/index.html            # Entire game: rendering, physics, input, sprites
run.sh                          # macOS/Linux launcher (creates venv, installs deps, starts)
run.bat                         # Windows launcher
requirements.txt                # Flask dependency
CLAUDE.md                       # This file — project context for Claude
README.md                       # Public-facing docs (MUST be updated when game features change)
.github/workflows/claude.yml    # @claude GitHub Actions trigger
.github/workflows/deploy.yml    # Auto-deploy to GitHub Pages on push to main
```

## Architecture

Everything lives in `templates/index.html` — there are no separate JS files, asset files, or CSS files. The game loop, sprite definitions, physics, input handling, and rendering are all in one `<script>` block.

### Key systems in index.html

- **Sprite data**: 16x16 arrays of single-char color variables (e.g., `b` = hat color). Each variable is a `const` holding a hex color string. `_` = transparent/null.
- **Sprite renderer**: `drawSprite(sprite, x, y, scale)` iterates the grid and draws scaled `fillRect` calls.
- **Game loop**: `requestAnimationFrame` driving `update()` and `draw()`.
- **Player**: Arrow keys for movement/jump, Space to shoot. Has gravity, jump velocity, ground/platform collision.
- **Camera**: Follows player horizontally, clamped to level bounds. Player stays at ~W/3 from left edge.
- **Platforms**: Array of `{x, top, w}` objects with full collision (land on top, bump head, side block).
- **Enemies**: Multiple types with different behaviors:
  - **Bunny**: Stationary, 1 HP, 10 pts
  - **Tortoise**: Slow tracking, 2 HP (has health bar), 20 pts
  - **Fox**: Fast charge when player is close, 1 HP, 15 pts
  - **Crow**: Flying, sine-wave movement, 1 HP, 15 pts
- **Difficulty scaling**: Early level = bunnies only, mid-level adds tortoises/foxes, late level adds crows. Speed multipliers increase with distance.
- **Particles**: Poof effects on enemy kill, dust on landing, score popups.
- **Background**: Parallax clouds, twinkling stars, scrolling grass/flowers/bushes.
- **Level**: Fixed width (6400px) with a goal marker. Reaching the goal wins the level.
- **Progress bar**: Shows player position relative to goal at top of screen.

## Code Conventions

- No external JS libraries or CSS frameworks
- Pixel art sprites defined inline as 2D arrays
- All game code in a single HTML file
- Keep the retro pixel-art aesthetic (Press Start 2P font, dark sky, garden theme)
- Canvas coordinates: world-space for game objects, screen-space for UI/particles
- High score persisted via `localStorage`

## Running

```bash
./run.sh          # or: python app.py
```

Opens browser automatically at http://localhost:6578

## When Making Changes

- Test that the game loads and Space starts it
- Verify sprites render correctly (no missing color variables)
- Check that collision detection still works after changing sprite/hitbox sizes
- Keep sprite definitions as 16x16 grids scaled by `S` (currently 4)
- If adding new sprites, define color variables as standalone `const` values (not object properties) so sprite arrays can reference them directly
- World-space vs screen-space: game objects use world X (offset by `cameraX` for rendering), particles and UI use screen coordinates
- **Always update README.md** when adding new game features, enemies, mechanics, or controls
