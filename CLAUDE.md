# SixSeven

A 2D browser game built with Flask and vanilla JavaScript Canvas. The player is a farmer who shoots carrots at invading bunnies.

## Tech Stack

- **Backend**: Python / Flask (serves a single HTML page)
- **Frontend**: Vanilla JavaScript with HTML5 Canvas (no frameworks, no build step)
- **Sprites**: 16x16 pixel-art grids defined as color-index arrays, scaled 4x to 64x64 on screen
- **Port**: 6578 (not 5000, macOS AirPlay uses 5000)

## Project Structure

```
app.py                  # Flask server, auto-opens browser on launch
templates/index.html    # Entire game: rendering, physics, input, sprites
run.sh                  # macOS/Linux launcher (creates venv, installs deps, starts)
run.bat                 # Windows launcher
requirements.txt        # Flask dependency
```

## Architecture

Everything lives in `templates/index.html` — there are no separate JS files, asset files, or CSS files. The game loop, sprite definitions, physics, input handling, and rendering are all in one `<script>` block.

### Key systems in index.html

- **Sprite data**: 16x16 arrays of single-char color variables (e.g., `b` = hat color). Each variable is a `const` holding a hex color string. `_` = transparent/null.
- **Sprite renderer**: `drawSprite(sprite, x, y, scale)` iterates the grid and draws scaled `fillRect` calls.
- **Game loop**: `requestAnimationFrame` driving `update()` and `draw()`.
- **Player**: Arrow keys for movement/jump, Space to shoot. Has gravity, jump velocity, ground collision.
- **Enemies**: Bunnies spawn from the right, scroll left. Collision with carrots = kill + points. Collision with player = death.
- **Particles**: Poof effects on bunny kill, dust on landing, score popups.
- **Background**: Parallax clouds, twinkling stars, scrolling grass/flowers/bushes.

## Code Conventions

- No external JS libraries or CSS frameworks
- Pixel art sprites defined inline as 2D arrays
- All game code in a single HTML file
- Keep the retro pixel-art aesthetic (Press Start 2P font, dark sky, garden theme)
- Canvas coordinates use screen pixels directly (not a virtual resolution)
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
