# Reasoning: Merge a Figma Design Into the Live Homepage

This document captures the thinking behind the prompt. It exists so a reader can understand not just *what* the prompt is, but *why* it ended up this way.

> **Note:** the user delegated review of this writeup ("trust your judgment, just write it"), so the reasoning below is synthesised from the session rather than dictated word-for-word. The facts (what shipped, what was protected) are verified against the build; the framing is the author's best read of intent.

## Goal

Give smoald.com a bolder, more branded homepage by adopting the parts of a Figma design the user loved — the **red / yellow / orange** colour system and the interactive **"Ecosystem"** visual — *without* throwing away the existing site. The brief was explicitly conservative: "merge this in… while keeping everything as it is."

## Iteration history

This evolved across three rounds in one conversation (see [`versions/`](./versions/)):

- **v1** — "I like this Figma design, can we use it?" Established that the Figma Make export was a heavy React/Vite/Tailwind app, and that the right move was to *rebuild the look* in the existing static site rather than adopt the framework.
- **v2** — "Merge this in while keeping everything as it is." Narrowed the scope to the three things that mattered: the tri-colour system, the interactive Ecosystem (replacing the old static map), and a blended hero — all delivered as a **preview file first**, then promoted to live only after approval.
- **v3** — "Can we add these to replace [the logos]?" Swapped the code-built `SM◍ALD` placeholder for the real 3D cloud + globe artwork. Because the supplied images were screenshots with a baked-in dark background, the background was removed programmatically (a brightness key in Pillow) to produce clean transparent PNGs.

## Failure modes the final version handles

- **Throwing the baby out with the bathwater** — a redesign can erase what already worked. This kept the founder framing, every card's copy, and all sub-pages untouched; only the *look* changed.
- **Framework bloat** — the Figma export pulled in dozens of React libraries. Rebuilding as one static file kept the site fast and consistent with the rest of smoald.com (no build step).
- **Deploying the wrong thing** — the redesign was shown as a `index-preview.html` first, and a memory note caught that this repo does **not** auto-deploy on git push (it needs `wrangler pages deploy`), preventing a false "it's live" claim.
- **A visible logo box** — the screenshot logos had a solid dark background. Rather than ship a faint rectangle, the background was knocked out to transparency and verified by compositing over the site's dark colour before asking for sign-off.

## Outcome

The redesigned homepage — tri-colour system, interactive Ecosystem, restyled cards — was deployed and **verified live on smoald.com**. The real-logo version was built and verified locally; deploying it was the next step.

## What I'd change next

Export the logo as a native transparent PNG from Figma for a pixel-perfect result (the programmatic knockout is good, but a clean source is better), and flip card status dots from "coming soon" to "live" as Store and Learn products ship.

## Tags

`code-generation` `content` `design-merge` `web-dev`
