# Sanhedrin Deck - Project State

## Current Status
**Last updated:** 2026-03-09
**Phase:** Full feature deck - dark/light mode, EN/HE bilingual, mobile responsive, deployed

## What We Did (Chronological)

### Session 1 - Initial Build
- Built 18-slide HTML presentation from structured deck outline
- Design system: "Ancient Authority Meets Digital Future" (dark cinematic)
- All CSS/JS inline in single `index.html`
- Custom CSS visuals for each slide (SVG puzzles, chat bubbles, timelines, etc.)

### Session 2 - Image Generation
- Fixed nanobanana MCP config (correct model: `gemini-2.5-flash-image`)
- Generated 18 hero images via direct Gemini API calls
- Style: "Sims 8" isometric, white backgrounds for cutout
- Integrated all images into HTML slides

### Session 3 - MOTJ Rebrand + Deploy
- Extracted MOTJ brand guide from zip (colors, fonts, logos)
- Rebranded deck: navy #003057, light blue #BDD6E6, taupe #776E64, Montserrat font
- Added MOTJ logos to slide 1 and nav bar
- Reorganized repo: per-slide folders (`slides/slide-NN/hero.png`)
- Created CLAUDE.md project guide
- Pushed to GitHub: https://github.com/jsagir/sanhedrin-deck
- Deployed to Render: https://sanhedrin-deck.onrender.com

### Session 4 - Brand Compliance + Features (2026-03-09)
- **Color fix**: Replaced ~60 hardcoded rgba values (old gold/teal) with MOTJ brand palette
- **Logo swap**: Replaced CSS-filtered PNGs with official white SVGs (horizontal + icon)
- **Full asset structure**: 15 official logo files (PNG/SVG, color/white), brand reference images, STYLE_GUIDE.md
- **Dark/light mode**: Toggle knob (top-right), localStorage persistence, logo auto-swap
- **EN/HE bilingual**: Full Hebrew translation of all 18 slides, RTL layout support, language toggle
- **Mobile responsive**: 1024px tablet + 640px phone breakpoints, stacked layouts
- **No em-dashes**: Removed all 102 em-dashes, replaced with colons/periods/hyphens
- **No emojis**: Replaced all emoji with inline SVG icons (loop diagram, speakers, modes, revenue, team, nav)
- **Image sizing**: Bumped all images 150-200px larger (hero: 640px, float: 560px, center: 560px)
- **CLAUDE.md rules**: Added 5 mandatory style rules

## What's Next (Backlog)
- [ ] Visual review of all 18 slides in browser after size changes
- [ ] Images may need regeneration at higher resolution for larger display
- [ ] Clean up old CSS classes no longer needed (sanhedrin-circle, polarization-visual, etc.)
- [ ] Add Hebrew/Arabic font support (Almoni Neue, Markazi Text) per brand guide
- [ ] Consider speaker notes or PDF export
- [ ] Review Hebrew translations for accuracy with native speaker

## Key Decisions
| Decision | Why |
|----------|-----|
| Single HTML file | Simplicity, no build step, easy to share |
| Montserrat over Gotham | Gotham isn't on Google Fonts; Montserrat is closest match |
| White background images | Easy cutout, works against any slide background |
| Gemini 2.5 Flash for images | Supports generateContent endpoint, stable, good quality |
| Render static site | Free tier, auto-deploy from GitHub, CDN |
| Per-slide folders | Scalable, each slide can hold multiple assets |
| No em-dashes ever | Professional tone, CLAUDE.md rule |
| No emojis, SVG only | Professional tone, inline SVG icons instead |
| en-content/he-content divs | Language toggle via CSS display, no JS DOM manipulation |
| Light theme: cream/stone | Warm institutional feel vs cold white |

## File Quick Reference
- `index.html` - the deck (all 18 slides, inline CSS/JS)
- `CLAUDE.md` - project guide + mandatory style rules
- `STATE.md` - this file (session log + backlog)
- `generate_images.py` - image regeneration script
- `assets/logos/` - 15+ official MOTJ logos (PNG/SVG, color/white)
- `docs/motj-brand/` - brand guide reference, STYLE_GUIDE.md
- `slides/slide-NN/hero.png` - per-slide hero images (18 total)
