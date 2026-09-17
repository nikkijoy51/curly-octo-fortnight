# Style guide

The durable record. Anything decided once is written here so the next session
inherits it instead of rediscovering it. Every entry names its source.

## Palette

Not yet sampled. Run `python3 scripts/sample_palette.py <reference>` against the
channel's reference image and paste the table here, including the source
filename and the coordinate each colour was taken from.

| Role | Hex | Sampled from | Contrast vs paper | Permitted use |
|------|-----|--------------|-------------------|---------------|
| _tbd_ | | | | |

## Type

Not yet chosen. Render specimens of the candidates with the real wordmark on one
line, compare, and record the winner here — plus confirmation that the family
actually rendered rather than falling back.

## Mechanics

Findings that are easy to lose and expensive to rediscover.

- **Centring tracked-out caps.** Letter-spacing adds a trailing space after the
  final character, which pushes a centred line visibly right. Apply a
  `text-indent` equal to the tracking value to cancel it.
- **Circular crops.** A profile image is cropped to a circle and displayed as
  small as 48px. Prompt for generous empty margin around the figure, and judge
  every candidate at 48px before choosing.

## Open

- Palette not yet sampled from a reference image.
- Wordmark font not chosen.
- Thumbnail template not built.
