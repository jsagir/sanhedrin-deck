# Sanhedrin Deck — Project State

## Current Status
**Last updated:** 2026-03-09
**Phase:** Initial build complete, MOTJ rebrand applied, deployed to Render

## What We Did (Chronological)

### Session 1 — Initial Build
- Built 18-slide HTML presentation from structured deck outline
- Design system: "Ancient Authority Meets Digital Future" (dark cinematic)
- All CSS/JS inline in single `index.html`
- Custom CSS visuals for each slide (SVG puzzles, chat bubbles, timelines, etc.)

### Session 2 — Image Generation
- Fixed nanobanana MCP config (correct model: `gemini-2.5-flash-image`)
- Generated 18 hero images via direct Gemini API calls
- Style: "Sims 8" isometric, white backgrounds for cutout
- Integrated all images into HTML slides

### Session 3 — MOTJ Rebrand + Deploy
- Extracted MOTJ brand guide from zip (colors, fonts, logos)
- Rebranded deck: navy #003057, light blue #BDD6E6, taupe #776E64, Montserrat font
- Added MOTJ logos to slide 1 and nav bar
- Reorganized repo: per-slide folders (`slides/slide-NN/hero.png`)
- Created CLAUDE.md project guide
- Pushed to GitHub: https://github.com/jsagir/sanhedrin-deck
- Deployed to Render: https://sanhedrin-deck.onrender.com

## What's Next (Backlog)
- [ ] Review all 18 slides visually in browser — check MOTJ brand cohesion
- [ ] Fine-tune color balance (some hardcoded rgba values still reference old gold/teal)
- [ ] Add Hebrew/Arabic font support (Almoni Neue, Markazi Text) per brand guide
- [ ] Consider adding speaker notes or PDF export
- [ ] Populate slide folders with alt image versions or supplementary assets
- [ ] Clean up old CSS classes no longer needed (sanhedrin-circle, polarization-visual, etc.)

## Key Decisions
| Decision | Why |
|----------|-----|
| Single HTML file | Simplicity, no build step, easy to share |
| Montserrat over Gotham | Gotham isn't on Google Fonts; Montserrat is closest match |
| White background images | Easy cutout, works against any slide background |
| Gemini 2.5 Flash for images | Supports generateContent endpoint, stable, good quality |
| Render static site | Free tier, auto-deploy from GitHub, CDN |
| Per-slide folders | Scalable — each slide can hold multiple assets |

## File Quick Reference
- `index.html` — the deck (edit slides here)
- `CLAUDE.md` — project guide for AI assistants
- `STATE.md` — this file (session log + backlog)
- `generate_images.py` — image regeneration script
- `docs/motj-brand/` — brand guide reference (not deployed)
