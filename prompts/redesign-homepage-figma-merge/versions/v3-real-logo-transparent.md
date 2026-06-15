# v3 — Swap in the real logo

```
Can we add these to replace [the current nav + hero logos] or not?
```

## Context

The user supplied the real logo artwork — a 3D cloud + globe `SM◍ALD` wordmark — as **screenshots**, to replace the code-built placeholder used in v2. The catch: screenshots have a solid dark background baked in, so dropping them straight in would show a faint box over the hero's glow.

## What changed after this round

- Inspected the actual pixels: the nav logo's background (`#0E0D0B`) nearly matched the site; the hero logo's was slightly warmer and would show an edge.
- A first attempt used a CSS `mix-blend-mode` trick — the user reported it left a faint box / washed-out colours.
- Removed the background **programmatically** with Pillow (a brightness key: dark → transparent, bright art preserved, soft-ramped edges) to produce clean transparent PNGs.
- **Verified before sign-off** by compositing the transparent logos over the site's dark colour and inspecting the result — no box, art intact.
