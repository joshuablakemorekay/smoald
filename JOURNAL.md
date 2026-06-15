# Development Journal — SMOALD.com Hub
A chronological log of key developments, decisions and learnings throughout this project.

---

## 2026-06-15 — Built & shipped the SMOALD.com brand hub

**TL;DR:** Turned a brand-architecture idea into a live, 4-page "brand house" website on Cloudflare Pages with the `smoald.com` domain — then documented the prompts that built it.

**Type:** Milestone

**What I built or did**
A parent homepage with three "doors" (SMOALD AI, Learn, Store), a page per mini-hub, and a hub-and-spoke architecture map. Wired my portfolio in at `/ai/hire`. Deployed it and connected `smoald.com`.

**Why I did it this way**
A unified brand house makes me look like a founder running a company, not a freelancer for hire — and it scales as new products go live.

**How it works**
Static HTML matching my portfolio's design. Honest "coming soon" badges, relative links, a `/hire` redirect. Deployed with wrangler; domain via Cloudflare DNS (CNAMEs → `smoald.pages.dev`).

**How We Did It**
1) Built the 4-page hub from the brief → 2) added the full spokes + map → 3) brought the portfolio in and renamed the project to `smoald` → 4) renamed "Tech" → "AI" and restructured URLs → 5) deployed to Cloudflare Pages → 6) moved `smoald.com` to Cloudflare + added DNS → 7) archived the prompts with an eval harness.

**What I learned**
Domain setup has real gotchas: Pages custom domains need DNS records that the API won't auto-create, and a Pages-only token can't list accounts. Also fixed a Windows UTF-8 crash in the eval runner.

**References / Conversations**
This Claude Code session; repo `joshuablakemorekay/smoald`.

---

## 2026-06-15 — smoald.com verified live

**Type:** Milestone

**What I built or did**
Confirmed the custom domain is fully live: `https://smoald.com` returns HTTP 200 over HTTPS with a valid SSL certificate, both the apex and `www` are active on Cloudflare, and the domain resolves globally. The build → deploy → custom-domain chain is complete.

---

## 2026-06-15 — Redesigned the homepage from a Figma design

**TL;DR:** Merged a Figma design's red/yellow/orange colour system and an interactive "Ecosystem" into the live homepage — keeping everything that already worked — then added the real logo and archived the prompts.

**Type:** Feature

**What I built or did**
A three-colour pillar system (Build = orange, Learn = yellow, Shop = red), an interactive "Ecosystem" visual that replaced the old static map, restyled cards, and a blended hero. Later swapped my placeholder wordmark for the real cloud + globe logo.

**Why I did it this way**
I loved the Figma design but didn't want to lose my founder framing, copy, or sub-pages — so I merged the best ideas into the existing site instead of rebuilding from scratch.

**How it works**
Still one static HTML file, no build step. The logo screenshots had a dark background, so I removed it automatically with a small Python script to get clean transparent images.

**How We Did It**
1) Backed up the site → 2) reviewed the Figma screenshots → 3) built a preview so the live site stayed safe → 4) deployed the redesign → 5) added the real logo with its background removed → 6) archived the prompts with an eval harness.

**What I learned**
This repo doesn't auto-publish on a git push — it only goes live when I run the deploy command. Catching that stopped me calling it "live" too early.

**References / Conversations**
This Claude Code session; repo `joshuablakemorekay/smoald`.

---
