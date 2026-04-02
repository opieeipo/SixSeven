"""
Export sprite data to PNG files and a spritesheet.

Parses existing sprites from index.html and adds new sprites from new_sprites.py,
renders each as a PNG, packs them into a spritesheet, and outputs both a simple
atlas and a Phaser-format atlas.

Usage:
    pip install Pillow
    python tools/export_sprites.py

Output:
    static/sprites/<name>.png          -- individual sprite PNGs
    static/sprites/spritesheet.png     -- packed spritesheet
    static/sprites/atlas.json          -- simple {name: {x,y,w,h}} atlas
    static/sprites/phaser-atlas.json   -- Phaser 3 texture atlas format
"""

import json
import os
import re
import sys

from PIL import Image

# Paths
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(SCRIPT_DIR)
HTML_PATH = os.path.join(PROJECT_DIR, "templates", "index.html")
OUTPUT_DIR = os.path.join(PROJECT_DIR, "static", "sprites")


def parse_palette(html: str) -> dict:
    """Extract color variable declarations: const x = "#hex"; and const _ = null;"""
    palette = {"_": None}
    pattern = re.compile(
        r'const\s+([a-zA-Z_][a-zA-Z0-9_]*)\s*=\s*(?:"(#[0-9a-fA-F]{3,8})"|null)\s*;'
    )
    for match in pattern.finditer(html):
        name = match.group(1)
        color = match.group(2)
        palette[name] = color
    return palette


def parse_sprite_arrays(html: str) -> list:
    """Extract sprite array definitions from HTML."""
    sprites = []
    pattern = re.compile(
        r'const\s+((?:FARMER|BUNNY|TORTOISE|FOX|CROW|BOSS|CARROT)\w*)\s*=\s*\[(.*?)\];',
        re.DOTALL,
    )
    for match in pattern.finditer(html):
        name = match.group(1)
        body = match.group(2)
        rows = []
        row_pattern = re.compile(r'\[([^\]]*)\]')
        for row_match in row_pattern.finditer(body):
            row_content = row_match.group(1)
            cells = []
            for token in row_content.split(","):
                token = token.strip()
                if token:
                    cells.append(token)
            rows.append(cells)
        if rows:
            sprites.append((name, rows))
    return sprites


def hex_to_rgba(hex_str: str) -> tuple:
    """Convert hex color string to (r, g, b, 255) tuple."""
    h = hex_str.lstrip("#")
    if len(h) == 3:
        return (int(h[0]*2, 16), int(h[1]*2, 16), int(h[2]*2, 16), 255)
    elif len(h) == 6:
        return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), 255)
    return None


def render_sprite(name: str, rows: list, palette: dict) -> Image.Image:
    """Render a sprite array to a Pillow RGBA image at native pixel resolution."""
    height = len(rows)
    width = max(len(row) for row in rows) if rows else 0
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))

    for y, row in enumerate(rows):
        for x, token in enumerate(row):
            if token == "_" or token == "null" or token is None:
                continue
            color_hex = palette.get(token) if isinstance(token, str) else token
            if color_hex is None:
                continue
            rgba = hex_to_rgba(color_hex)
            if rgba:
                img.putpixel((x, y), rgba)

    return img


def render_new_sprite(name: str, grid: list) -> Image.Image:
    """Render a new sprite from a 2D array of hex color strings or None."""
    height = len(grid)
    width = max(len(row) for row in grid) if grid else 0
    img = Image.new("RGBA", (width, height), (0, 0, 0, 0))

    for y, row in enumerate(grid):
        for x, color in enumerate(row):
            if color is None:
                continue
            rgba = hex_to_rgba(color)
            if rgba:
                img.putpixel((x, y), rgba)

    return img


def build_spritesheet(sprite_images: list) -> tuple:
    """Pack sprite images into a single-row spritesheet."""
    CELL_SIZE = 24
    sheet_width = CELL_SIZE * len(sprite_images)
    sheet_height = CELL_SIZE

    sheet = Image.new("RGBA", (sheet_width, sheet_height), (0, 0, 0, 0))
    atlas = {}

    for i, (name, img) in enumerate(sprite_images):
        x_offset = i * CELL_SIZE
        sheet.paste(img, (x_offset, 0))
        atlas[name] = {
            "x": x_offset,
            "y": 0,
            "w": img.width,
            "h": img.height,
        }

    return sheet, atlas


def build_phaser_atlas(atlas: dict, sheet_width: int, sheet_height: int) -> dict:
    """Convert simple atlas to Phaser 3 texture atlas format."""
    frames = {}
    for name, data in atlas.items():
        frames[name] = {
            "frame": {"x": data["x"], "y": data["y"], "w": data["w"], "h": data["h"]},
            "rotated": False,
            "trimmed": False,
            "spriteSourceSize": {"x": 0, "y": 0, "w": data["w"], "h": data["h"]},
            "sourceSize": {"w": data["w"], "h": data["h"]},
        }
    return {
        "frames": frames,
        "meta": {
            "image": "spritesheet.png",
            "size": {"w": sheet_width, "h": sheet_height},
            "scale": "1",
        },
    }


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    # Define the canonical sprite order (original + new)
    SPRITE_ORDER = [
        "FARMER_SPRITE", "FARMER_WALK", "FARMER_JUMP", "FARMER_CROUCH",
        "BUNNY_SPRITE", "BUNNY_HOP",
        "TORTOISE_SPRITE", "FOX_SPRITE",
        "CROW_SPRITE", "CROW_FLAP",
        "BOSS_BUNNY_KING", "BOSS_GOLEM", "BOSS_STORM_CROW",
        "BOSS_CAVE_WORM", "BOSS_FIRE_DRAKE", "BOSS_RUIN_KNIGHT",
        "CARROT_SPRITE", "HEART", "HEART_EMPTY",
    ]

    # Generate new sprites from new_sprites.py definitions
    sys.path.insert(0, SCRIPT_DIR)
    from new_sprites import ALL_NEW_SPRITES
    print(f"Generating {len(ALL_NEW_SPRITES)} new sprites from definitions...")
    for name, grid in ALL_NEW_SPRITES.items():
        img = render_new_sprite(name, grid)
        individual_path = os.path.join(OUTPUT_DIR, f"{name}.png")
        img.save(individual_path)
        print(f"  Generated {name}: {img.width}x{img.height}")

    # Load all individual PNGs in canonical order
    sprite_images = []
    print(f"\nLoading {len(SPRITE_ORDER)} sprites for spritesheet:")
    for name in SPRITE_ORDER:
        png_path = os.path.join(OUTPUT_DIR, f"{name}.png")
        if not os.path.exists(png_path):
            print(f"  WARNING: {name}.png not found, skipping")
            continue
        img = Image.open(png_path).convert("RGBA")
        print(f"  {name}: {img.width}x{img.height}")
        sprite_images.append((name, img))

    # Build spritesheet
    sheet, atlas = build_spritesheet(sprite_images)
    sheet_path = os.path.join(OUTPUT_DIR, "spritesheet.png")
    sheet.save(sheet_path)
    print(f"\nSpritesheet: {sheet_path} ({sheet.width}x{sheet.height})")

    # Save simple atlas
    atlas_path = os.path.join(OUTPUT_DIR, "atlas.json")
    with open(atlas_path, "w", encoding="utf-8") as f:
        json.dump(atlas, f, indent=2)
    print(f"Atlas: {atlas_path}")

    # Save Phaser atlas
    phaser_atlas = build_phaser_atlas(atlas, sheet.width, sheet.height)
    phaser_path = os.path.join(OUTPUT_DIR, "phaser-atlas.json")
    with open(phaser_path, "w", encoding="utf-8") as f:
        json.dump(phaser_atlas, f, indent=2)
    print(f"Phaser atlas: {phaser_path}")

    print(f"\nDone! {len(sprite_images)} sprites exported successfully.")


if __name__ == "__main__":
    main()
