#!/usr/bin/env python3
"""Render candidates at the sizes they will actually be seen at.

A profile image is judged at 48px, not at 1024px. This builds a grid — one row
per candidate, one column per size — so the choice is made on evidence.

    python3 scripts/render_sizes.py a.png b.png c.png --sizes 48,88,176
    python3 scripts/render_sizes.py a.png --circle -o assets/size-test.png
"""
import argparse
import sys

from PIL import Image, ImageDraw

GUTTER = 24
BACKGROUND = (255, 255, 255)


def circle_crop(img):
    mask = Image.new("L", img.size, 0)
    ImageDraw.Draw(mask).ellipse((0, 0, img.size[0] - 1, img.size[1] - 1), fill=255)
    out = Image.new("RGBA", img.size, (0, 0, 0, 0))
    out.paste(img, (0, 0), mask)
    return out


def build(paths, sizes, circle):
    rows = []
    for path in paths:
        img = Image.open(path).convert("RGBA")
        side = min(img.size)
        left = (img.size[0] - side) // 2
        top = (img.size[1] - side) // 2
        img = img.crop((left, top, left + side, top + side))
        rendered = []
        for size in sizes:
            thumb = img.resize((size, size), Image.LANCZOS)
            rendered.append(circle_crop(thumb) if circle else thumb)
        rows.append(rendered)

    largest = max(sizes)
    width = GUTTER + len(sizes) * (largest + GUTTER)
    height = GUTTER + len(rows) * (largest + GUTTER)
    sheet = Image.new("RGB", (width, height), BACKGROUND)

    for r, row in enumerate(rows):
        for c, thumb in enumerate(row):
            cell_x = GUTTER + c * (largest + GUTTER)
            cell_y = GUTTER + r * (largest + GUTTER)
            # centre each thumbnail in its cell so sizes are visually comparable
            x = cell_x + (largest - thumb.size[0]) // 2
            y = cell_y + (largest - thumb.size[1]) // 2
            sheet.paste(thumb, (x, y), thumb)
    return sheet


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("images", nargs="+")
    ap.add_argument("--sizes", default="48,88,176",
                    help="comma-separated pixel sizes (default 48,88,176)")
    ap.add_argument("--circle", action="store_true",
                    help="apply the circular crop a profile image gets")
    ap.add_argument("-o", "--out", default="assets/size-test.png")
    args = ap.parse_args()

    sizes = [int(s) for s in args.sizes.split(",")]
    sheet = build(args.images, sizes, args.circle)
    sheet.save(args.out)
    print(f"Wrote {args.out} — {len(args.images)} candidate(s) at {sizes} px.")
    print("Look at it before choosing. The smallest column is the one that decides.")


if __name__ == "__main__":
    sys.exit(main())
