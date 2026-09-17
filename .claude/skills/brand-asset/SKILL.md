---
name: brand-asset
description: Produce a channel brand asset — profile image, banner, thumbnail template, wordmark, watermark — to the repo's verification standard. Use when asked to create, regenerate or fix any visual identity asset, or when a reference image is supplied as the palette or style source.
---

# Brand asset production

Follow this in order. Do not skip the verification steps to save a turn; a
plausible-looking asset that fails at render size costs more than the check did.

## 1. Derive the palette from the reference

Sample it, do not eyeball it. Record hex, role and source coordinates in
`brand/style-guide.md`.

```bash
python3 scripts/sample_palette.py <reference.png>
```

Then run the contrast pass over the sampled values and demote anything failing
4.5:1 to fill/display-only. Say the ratio out loud in your reply.

## 2. Write the generation prompt against the crop

For anything that gets circular-cropped, the prompt must ask for generous empty
margin so the figure survives the crop. Name the composition explicitly: head
and shoulders, centred, square.

## 3. Generate three, not one

Use `generate_image_batch` where available. Three variants at the same prompt.

## 4. Judge at render size

```bash
python3 scripts/render_sizes.py <variant.png> --sizes 48,88,176
```

Build the comparison grid, look at it, and pick on evidence: which one holds the
face at 48px, which ones sit too high or too small. Save the grid to `assets/`.

## 5. Fix defects and re-test

Eyes, hands and text are the usual failures. If you fix one, re-run step 4 — the
fix is not verified until you have looked at the new render at size.

## 6. Verify fonts actually rendered

After any text render, confirm the intended family was used rather than a
fallback, and state it.

## 7. Prove the safe area

For banners, check all three YouTube crops (mobile, tablet, desktop) and write
the proof image to `assets/banner-safe-area-proof.png`.

## 8. Record and report

Append every decision to `brand/style-guide.md`. Close with spend to date and an
explicit "Still open" list with cost estimates.

## Asking the user

Only for genuine preference — which font, which variant, whether the watermark
is the mark or the character. Show rendered options, ask once, recommend one.
Anything you can measure, measure instead of asking.
