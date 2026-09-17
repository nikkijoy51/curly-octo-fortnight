# Operating standard

This repo produces brand and channel assets. The bar is not "an asset was
produced" — it is "the asset was measured under the conditions it will actually
be used in, and the decisions behind it are written down."

Nine rules. They apply to every asset session.

## 1. Sample, never invent

Colours, proportions and style come from the reference file, measured, not
chosen by eye or from memory. Every palette entry ships with the hex value and
the file it was sampled from.

Wrong: "a warm terracotta, roughly #B4551E"
Right: "Terracotta #CE5B20, sampled from reference.png at (412, 880)"

## 2. Measure the thing you just claimed

A sampled palette changes what passes contrast. Re-run the check against the
measured values, not the ones you assumed. State the ratio and the verdict:

> Terracotta #CE5B20 measures 3.58:1 against paper. Fails 4.5:1. Fill and
> display only; body text uses ink #2E2C20.

## 3. Test at the size it renders at

A profile image is judged at 48px, not at 1024px. A banner is judged at all
three YouTube crops, not just desktop. Render the real size, look at it, and
save the proof image into `assets/` so the check is repeatable.

## 4. Generate options, then narrow with evidence

Three variants, not one. Compare them under rule 3, then say which survives and
why — "at the size it actually renders, the middle one holds the face." The
comparison grid is the artifact; keep it.

## 5. Confirm it rendered, don't assume it

A font that silently falls back looks fine and is wrong. After any render that
depends on an external font, asset or model, verify the output used what you
asked for. Say so explicitly: "Young Serif confirmed as the actually-rendered
family, not a fallback."

## 6. Ask binary questions with a recommendation

When a choice is genuinely the user's, show the rendered options side by side,
ask one question, and name your pick:

> Which font for the wordmark? All four are on one line and tracked out.
> B Young Serif (Recommended)

Do not ask about things you can verify yourself.

## 7. Write decisions into the guide, immediately

Anything discovered once gets written into `brand/style-guide.md` so the next
session inherits it instead of rediscovering it. This includes incidental
mechanics, e.g. centring tracked-out caps needs a matching `text-indent` or the
trailing letter-space pushes the line right.

## 8. Report cost and keep an open list

State spend as it accrues ("4 credits of 3,898"), and say when work is free.
End every session with what is still open and what it will cost:

> **Still open** — the thumbnail template shows zones, not her. Now that the
> character exists I can build a real worked example. Roughly 2 more credits.

## 9. Build scripts, not one-off calls

Anything done twice becomes a script in `scripts/`, committed. Font specimen
sheets, safe-area proofs and contrast checks are code, so the next run is
reproducible rather than remembered.

## Layout

    assets/           rendered outputs and proof images
    brand/            style-guide.md — the durable record of decisions
    scripts/          reproducible checks and generators
    docs/             analysis and reference
