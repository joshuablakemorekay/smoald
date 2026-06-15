# v2 — Merge it in, keep everything as it is

```
I really like these from the Figma design, especially the consistency with
colours: Red, Yellow and Orange. The ecosystem is very good. Can we merge this
into current https://smoald.com/ while keeping everything for https://smoald.com/
as it is?
```

## Context

The decisive round. Screenshots pinned down exactly what to adopt: the **tri-colour pillar system** (Build = orange, Learn = yellow, Shop = red) and the interactive **"Ecosystem"** node graph. The "keep everything as it is" instruction set the constraint — restyle and add, don't remove.

## What changed after this round

- Built the merge as a **`index-preview.html`** first so the live site stayed untouched until approval.
- Applied the tri-colour system across hero, cards, and ecosystem.
- Replaced the old static architecture map with the interactive Ecosystem, carrying its content into hover detail panels.
- Blended the hero: kept founder framing, borrowed the Build · Learn · Shop rhythm.
- After approval, promoted to live and deployed via `wrangler pages deploy` (this repo does **not** auto-deploy on git push).
