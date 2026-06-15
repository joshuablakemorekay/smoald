# Merge a Figma Design Into the Live Homepage

> **Category:** code-generation
> **Model used:** Claude Opus 4.8 (Claude Code)
> **Project area:** SMOALD.com brand-house website — homepage redesign
> **Status:** production
> **Last updated:** 2026-06-15

## What this prompt does

Takes a Figma "Make" design the user liked and merges its strongest ideas — a tri-colour pillar system and an interactive "Ecosystem" visual — into the *existing* smoald.com homepage, without rebuilding from scratch and without losing the copy, sections, and founder framing that already worked.

## The prompt

```
I really like these from the Figma design, especially the consistency with
colours: Red, Yellow and Orange. The ecosystem is very good. Can we merge this
into current https://smoald.com/ while keeping everything for https://smoald.com/
as it is?
```

## Inputs

- A **Figma Make design** shared as screenshots (hero, an interactive "Ecosystem" node graph, and three product cards) plus the project's `package.json` (a React/Vite/Tailwind export).
- The **existing homepage** (`index.html`) — a hand-written, single-file static page with a dark `#0E1116` theme, orange `#FF6A3D` accent, and "three doors" (AI / Learn / Store), an architecture map, a founder section, and contact.
- Later in the session, the **real logo art** (3D cloud + globe `SM◍ALD` wordmark) supplied as screenshots, to replace a code-built placeholder.

## Expected output

A redesigned-but-familiar homepage that:
- Adopts the **tri-colour system** — Build = orange `#FF6A3D`, Learn = yellow `#FFB23D`, Shop = red `#F04438` — across hero, cards, and the ecosystem
- Adds an **interactive "Ecosystem"** section (hover a node → coloured glow + orbiting dots + detail panel) that **replaces** the old static architecture map, carrying its content over
- **Keeps** the founder framing, all existing card copy, every sub-page link, and honest "coming soon" states
- Stays a **single static file with no build step** — not the heavy React export
- Ships only after a **preview-before-deploy** check, since this repo goes live via `wrangler`, not on git push

## Related files

- Reasoning: [`REASONING.md`](./REASONING.md)
- Evaluation rubric: [`rubric.yaml`](./rubric.yaml)
- Version history: [`versions/`](./versions/)
