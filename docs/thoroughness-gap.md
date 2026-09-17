# What the Zinny session does, and where it came from

Source: week 2 video, "The Generated Assets" segment (11:15–12:43), Zinny Studio
building brand assets for The Bread Standard.

The session looks thorough because of eight specific behaviours, not because the
model is better. Each one is mechanical and copyable.

| # | Behaviour | Evidence in the video |
|---|---|---|
| 1 | Palette is sampled from the user's file, not chosen | "The palette is now sampled, not chosen. Paper `#FEEFE0`, Peach `#F4C99F`, Terracotta `#CE5B20`, Cream `#E8CAA6`, Ink `#2E2C20`. Every one measured off your file." |
| 2 | Measurement changes a prior decision, and it says so | Earlier terracotta `#B4551E` "scraped 4.5:1"; the sampled `#CE5B20` measures 3.58:1 and fails, so it is demoted to fill and display only |
| 3 | Options, not a single output | Three variants generated per prompt; four font specimens rendered side by side |
| 4 | Judged at real render size | The 48px grid: "at the size it actually renders, the middle one holds the face" |
| 5 | Rendering is confirmed, not assumed | "Young Serif confirmed as the actually-rendered family, not a fallback" |
| 6 | Verified against real crops, with a saved proof | Safe area checked at all three YouTube crops, proof at `assets/banner-safe-area-proof.png` |
| 7 | Incidental findings are written into the guide | Centring tracked-out caps needs a matching `text-indent`, "now written into the style guide so it doesn't get lost" |
| 8 | Cost and open work are stated every turn | "Total spend: 4 credits of 3,898"; a standing **Still open** section with a 2-credit estimate |

## The pattern underneath

Generate → measure under real conditions → let the measurement overrule the
plan → write the finding down → say what it cost and what is left.

The expensive-looking part is step two. It is the cheap part: rendering a PNG at
48px and looking at it takes one command.

## Status in this repo

Rules 1–9 in `CLAUDE.md` encode the eight behaviours above, and the
`brand-asset` skill sequences them for asset production.

Two of the checks are executable:

- `scripts/sample_palette.py` — behaviours 1 and 2. Quantises a reference image,
  reports each colour with its coverage and source coordinate, computes WCAG
  contrast against the background and prints the pass/fail verdict per entry.
- `scripts/render_sizes.py` — behaviour 4. Builds the comparison grid at real
  render sizes, with the circular crop a profile image actually gets.

Not yet written: the safe-area proof for banners (behaviour 6) and the font
specimen sheet with fallback detection (behaviour 5). Both are needed before a
banner can be produced to this standard.
