#!/usr/bin/env python3
"""Sample a palette from a reference image and contrast-check it.

Colours come out of the file, measured, with the coordinate they were taken
from — so a palette entry can always be traced back to its source.

    python3 scripts/sample_palette.py reference.png [--colours 5]
"""
import argparse
import sys
from collections import Counter

from PIL import Image


def hexof(rgb):
    return "#{:02X}{:02X}{:02X}".format(*rgb)


def relative_luminance(rgb):
    """WCAG 2.1 relative luminance."""
    channels = []
    for c in rgb:
        c = c / 255
        channels.append(c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4)
    r, g, b = channels
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def contrast_ratio(fg, bg):
    l1, l2 = relative_luminance(fg), relative_luminance(bg)
    lighter, darker = max(l1, l2), min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def sample(path, n_colours):
    img = Image.open(path).convert("RGB")
    quantised = img.quantize(colors=n_colours, method=Image.Quantize.MEDIANCUT)
    palette = quantised.getpalette()
    indexed = quantised.load()
    width, height = quantised.size

    counts = Counter()
    first_seen = {}
    for y in range(height):
        for x in range(width):
            i = indexed[x, y]
            counts[i] += 1
            first_seen.setdefault(i, (x, y))

    entries = []
    for index, count in counts.most_common():
        rgb = tuple(palette[index * 3 : index * 3 + 3])
        entries.append(
            {
                "rgb": rgb,
                "hex": hexof(rgb),
                "coverage": count / (width * height),
                "at": first_seen[index],
            }
        )
    return entries


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("image")
    ap.add_argument("--colours", type=int, default=5, help="palette size (default 5)")
    args = ap.parse_args()

    entries = sample(args.image, args.colours)
    paper = entries[0]  # most coverage is the background in practice
    ink = min(entries, key=lambda e: relative_luminance(e["rgb"]))

    print(f"Sampled from {args.image}\n")
    print(f"{'HEX':<9} {'COVERAGE':>9}  {'AT':<14} {'VS PAPER':>9}  VERDICT")
    for e in entries:
        ratio = contrast_ratio(e["rgb"], paper["rgb"])
        if e is paper:
            verdict = "paper (background)"
        elif ratio >= 4.5:
            verdict = "passes 4.5:1 — body text ok"
        elif ratio >= 3.0:
            verdict = "FAILS 4.5:1 — fill and display only"
        else:
            verdict = "FAILS 3:1 — fill only, never text"
        at = "{},{}".format(*e["at"])
        print(f"{e['hex']:<9} {e['coverage']:>8.1%}  {at:<14} {ratio:>8.2f}:1  {verdict}")

    print(f"\nBody text colour: {ink['hex']} "
          f"({contrast_ratio(ink['rgb'], paper['rgb']):.2f}:1 against paper)")
    print("\nPaste these into brand/style-guide.md with the source filename.")


if __name__ == "__main__":
    sys.exit(main())
