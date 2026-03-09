# Sanhedrin Deck - Project State

## Current Status
**Last updated:** 2026-03-09
**Phase:** Frontend rewrite done, cinematic image regeneration blocked on API key

## What Needs to Happen Next
1. **Get a fresh Gemini API key** from https://aistudio.google.com/apikey
2. **Set it as env var** (do NOT paste in chat or code):
   ```bash
   export GEMINI_API_KEY="your-key-here"
   ```
3. **Run the image generator:**
   ```bash
   cd ~/sanhedrin-deck && python3 generate_images.py
   ```
4. **Commit and push:**
   ```bash
   git add slides/ generate_images.py && git commit -m "update: Cinematic first-person hero images" && git push
   ```
5. **Review the deck** at https://sanhedrin-deck.onrender.com after deploy

## What We Did (Chronological)

### Session 1 - Initial Build
- Built 18-slide HTML presentation from structured deck outline
- Design system: "Ancient Authority Meets Digital Future" (dark cinematic)
- All CSS/JS inline in single index.html
- Custom CSS visuals for each slide

### Session 2 - Image Generation
- Fixed nanobanana MCP config (correct model: gemini-2.5-flash-image)
- Generated 18 hero images via direct Gemini API calls
- Style: "Sims 8" isometric, white backgrounds for cutout
- Integrated all images into HTML slides

### Session 3 - MOTJ Rebrand + Deploy
- Extracted MOTJ brand guide from zip
- Rebranded deck: navy #003057, light blue #BDD6E6, taupe #776E64, Montserrat font
- Added MOTJ logos, reorganized repo (per-slide folders)
- Created CLAUDE.md project guide
- Pushed to GitHub, deployed to Render

### Session 4 - Brand Compliance + Features
- Color fix, logo swap, full asset structure
- Dark/light mode, EN/HE bilingual, mobile responsive
- No em-dashes, no emojis (SVG icons only)
- Image sizing bumps

### Session 5 - Killer Presentation Redesign (2026-03-09)
- **Regenerated all 18 images** with premium architectural style (walnut wood, brushed aluminum, frosted glass, semi-translucent scale figures). All 18/18 succeeded.
- **Complete frontend rewrite** applying killer presentation rules:
  - 852 lines (down from 3000+), stripped 2850 lines of visual noise
  - Image-dominant layout (55% of slide via grid split)
  - One message per slide, 24px+ body text, 56px headlines
  - Killed all cards, tables, matrices, chat bubbles, loop diagrams, progress bars
  - Added slide-08 (Dilemma Library) which had an image but was missing from HTML
- **Fixed image scaling** to fill desktop viewport (80vh split, 55vh centered)
- **Received investor review** with structural feedback:
  - Deck is strong on Puzzle metaphor, EdTech play, and 70/30 honesty
  - Weakness: too many slides (18 vs 10-12), too abstract (isometric), needs UX shots
  - Suggestion: combine Architecture+Solved into "Under the Hood", move Physical Space to appendix
  - Need: demo button on Sample Session slide, less metaphor, more first-person UX visuals
- **New cinematic image prompts written** in generate_images.py:
  - Pivoted from "Top-Down Isometric" to "Cinematic First-Person, Shallow DOF"
  - All 18 prompts updated for photorealistic museum-tech feel
  - BLOCKED: both Gemini API keys flagged as leaked (committed to git)

## What's Next (Backlog)
- [ ] Generate cinematic images with fresh API key (env var, not hardcoded)
- [ ] Apply structural deck feedback (combine slides, reduce to 12-14)
- [ ] Add "Play Demo" button on Sample Session slide
- [ ] Add Hebrew/Arabic font support (Almoni Neue, Markazi Text)
- [ ] Review Hebrew translations with native speaker
- [ ] Consider speaker notes or PDF export

## Key Decisions
| Decision | Why |
|----------|-----|
| Single HTML file | Simplicity, no build step, easy to share |
| Montserrat over Gotham | Gotham isn't on Google Fonts; Montserrat is closest match |
| Render static site | Free tier, auto-deploy from GitHub, CDN |
| Per-slide folders | Scalable, each slide can hold multiple assets |
| No em-dashes ever | Professional tone, CLAUDE.md rule |
| No emojis, SVG only | Professional tone, inline SVG icons instead |
| en-content/he-content divs | Language toggle via CSS display, no JS DOM manipulation |
| Light theme: cream/stone | Warm institutional feel vs cold white |
| Cinematic over Isometric | Emotional connection, first-person immersion for investors |
| API key via env var | Previous keys leaked by being committed to git |

## File Quick Reference
- `index.html` - the deck (18 slides, inline CSS/JS, killer presentation layout)
- `CLAUDE.md` - project guide + mandatory style rules
- `STATE.md` - this file (session log + backlog)
- `generate_images.py` - image regeneration script (cinematic prompts, reads GEMINI_API_KEY env var)
- `assets/logos/` - official MOTJ logos (PNG/SVG, color/white)
- `docs/motj-brand/` - brand guide reference, STYLE_GUIDE.md
- `slides/slide-NN/hero.png` - per-slide hero images (18 total, currently architectural style)
