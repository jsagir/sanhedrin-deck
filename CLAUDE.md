# Sanhedrin Educational Experience — Pitch Deck

## Project Overview
Investor pitch deck for the Sanhedrin Educational Experience at the Museum of Tolerance Jerusalem (MOTJ). Single-page HTML presentation with 18 slides, AI-generated isometric hero images, and MOTJ brand compliance.

**Live URL:** https://sanhedrin-deck.onrender.com
**Repo:** https://github.com/jsagir/sanhedrin-deck
**Auto-deploy:** Push to `master` triggers Render deploy.

## Repository Structure

```
sanhedrin-deck/
  index.html              # Main deck (all 18 slides, inline CSS/JS)
  CLAUDE.md               # This file
  assets/
    logos/                 # MOTJ brand logos
      motj-logo-horizontal.png
      motj-logo-icon.png
  slides/
    slide-01/hero.png     # Title/Hero — Sanhedrin arena
    slide-02/hero.png     # The Problem — polarization
    slide-03/hero.png     # Puzzle Metaphor
    slide-04/hero.png     # Value Proposition
    slide-05/hero.png     # Visitor Journey
    slide-06/hero.png     # Role-Based Architecture
    slide-07/hero.png     # Sample Session (AV dilemma)
    slide-08/hero.png     # Dilemma Library (bonus asset)
    slide-09/hero.png     # Experience Modes (split diorama)
    slide-10/hero.png     # Physical Space
    slide-11/hero.png     # Proof of Concept (Rambam)
    slide-12/hero.png     # Solved vs Ahead (70/30)
    slide-13/hero.png     # Competitive Advantage
    slide-14/hero.png     # EdTech Platform
    slide-15/hero.png     # Roadmap & Milestones
    slide-16/hero.png     # Business Case
    slide-17/hero.png     # The Team
    slide-18/hero.png     # Closing/CTA
  docs/
    motj-brand/           # MOTJ brand guide (reference only, not deployed)
  generate_images.py      # Script to regenerate images via Gemini API
```

## MOTJ Brand Guidelines

### Colors (CSS Variables in :root)
| Variable | Hex | MOTJ Reference |
|----------|-----|----------------|
| `--bg-deep` | `#003057` | PMS 540 — Primary navy |
| `--gold-primary` | `#BDD6E6` | PMS 544 — Light blue accent |
| `--teal` | `#776E64` | PMS 404 — Warm taupe |
| `--text-primary` | `#f0f4f7` | White on dark |

### Fonts
- **Display/Body:** Montserrat (Google Fonts proxy for Gotham Medium/Book)
- **Mono:** JetBrains Mono (labels, technical text)
- **Hebrew:** Almoni Neue DL 4.0 AAA (brand spec, not loaded in web)
- **Arabic:** Markazi Text (brand spec, not loaded in web)

### Logo Usage
- Horizontal logo on slide 1 (white-inverted via CSS filter)
- Icon logo in bottom nav bar (white-inverted)
- Source PNGs: `assets/logos/`
- SVGs available in `docs/motj-brand/` for print

## Slide Structure (4 Acts)

### ACT 1 — THE HOOK (Slides 1-4)
1. Title/Hero — first impression, core premise
2. The Problem — polarization urgency
3. Puzzle Metaphor — cognitive twist (dispute = puzzle)
4. Value Proposition — "Learn to argue in 30 min"

### ACT 2 — THE EXPERIENCE (Slides 5-9)
5. Visitor Journey — 6-step end-to-end flow
6. Architecture — Role-Based (Persona vs Role separation)
7. Sample Session — Goring Ox / AV dilemma with Rambam, Golda, Hillel
8. Experience Modes — Culture of Disagreement vs Debate Mode
9. Physical Space — circular amphitheater concept

### ACT 3 — WHY IT WORKS (Slides 10-13)
10. Proof of Concept — Rambam exhibit validation
11. Solved vs Ahead — 70/30 progress, A2A mitigation
12. Competitive Advantage — matrix vs chatbots/museums/debate AI
13. EdTech Platform — museum + schools + online pyramid

### ACT 4 — THE ASK (Slides 14-18)
14. Roadmap — 4 phases (POC → Demo → Prototype → Launch)
15. Business Case — revenue streams + Research Hub
16. The Team — Tech + Strategy + Knowledge + Missing Piece
17. Closing/CTA — "Give us the green light"
18. Appendix — 13 Thinking Modes, architecture, personas

## Image Generation
Images use "Premium Museum-Tech & Architectural Minimalism" aesthetic:
- **Perspective:** High-end 3D top-down isometric, strictly grid-aligned
- **Background:** Always "isolated on a pure white background for easy cutout"
- **Materials:** Warm walnut wood (history), brushed aluminum, frosted glass/glassmorphism (technology)
- **Characters:** Semi-translucent architectural scale figures (no cartoonish avatars)
- **Lighting:** Premium corporate studio lighting, soft ambient occlusion, crisp shadows, cyan/amber data accents
- **Model:** `gemini-2.5-flash-image` via Google Generative AI API
- **Script:** `generate_images.py` (requires GEMINI_API_KEY env var)
- To regenerate: `python3 generate_images.py`

## Presentation Design Rules
- 16:9 widescreen aspect ratio (viewport-based, adapts naturally)
- Titles: 56px (36-44pt equivalent)
- Body text: 24px minimum (24pt+ rule)
- Sans-serif fonts (Montserrat as Gotham proxy)
- Rule of 6: max 6 elements per slide
- High contrast: light text on dark navy, or dark on cream

## Working with This Deck

### Adding/editing a slide
1. Edit the `<section class="slide">` block in `index.html`
2. Place new images in `slides/slide-NN/`
3. Reference as `slides/slide-NN/filename.png`

### Regenerating a single image
Edit the prompt in `generate_images.py` and run for that slide only, or use the nanobanana MCP tool directly.

### Deploy
```bash
git add -A && git commit -m "update: description" && git push
```
Render auto-deploys on push to master.

## Navigation
- Arrow keys (left/right) or swipe
- `F` key for fullscreen
- Home/End for first/last slide
- Bottom bar: prev/next/fullscreen buttons

## State Tracking (MANDATORY)
**After every work session**, update `STATE.md` with:
1. What was done (add a new dated section)
2. Why it was done (context/reasoning)
3. What's next (update backlog)
4. Any new decisions (add to decisions table)

This is non-negotiable. STATE.md is the project memory.

## Style Rules (MANDATORY)

1. **NO em-dashes** - Never use "—" anywhere. Use ":", "-", ".", or "," instead.
2. **NO emojis** - Never use emoji characters. Use inline SVG icons instead.
3. **Professional tone** - This is an investor pitch deck for a world-class museum. Every element must look polished and institutional.
4. **MOTJ Brand compliance** - All colors must use the 3 MOTJ Pantone values (see STYLE_GUIDE.md). No off-brand colors.
5. **SVG icons only** - All icons must be inline SVG with `stroke="currentColor"`. No emoji, no icon fonts.
6. **API keys LOCAL ONLY** - For image generation, read GEMINI_API_KEY from `.env` file (gitignored). NEVER hardcode API keys in code or commit them to the repo.
7. **Narration MP3 sync** - When slides are added, removed, or reordered, the narration MP3s in `audio/narration/slide-NN.mp3` MUST be regenerated or renumbered to match. Run `generate_narration.py` after any slide structure change. Update narration scripts in that file to match new slide content.
