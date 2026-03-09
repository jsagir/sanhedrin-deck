# Sanhedrin Deck - Project State

## Current Status
**Last updated:** 2026-03-09
**Phase:** Comprehensive deck rebuild complete (17+4 slides), ready for review

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
   git add slides/ generate_images.py index.html && git commit -m "update: Isometric museum-tech images and refined slide content" && git push
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

### Session 6 - Isometric Rebuild + Content Refresh (2026-03-09)
- **Switched image style** from Cinematic First-Person to "Premium Museum-Tech & Architectural Minimalism" isometric
  - All 18 prompts updated: 3D isometric, white background cutouts, walnut wood + brushed aluminum + frosted glass
  - Semi-translucent architectural scale figures, cyan/amber data accents, studio lighting
- **Updated all slide content** to match the definitive deck outline:
  - Slide 2: Added civic discourse simulator framing
  - Slide 3: Added 13 Talmudic Thinking Modes reference
  - Slide 5: Expanded to 6 explicit journey steps with descriptions
  - Slide 7: Added "Play Demo" button (links to sanhedrin-demo.onrender.com)
  - Slide 8: Added 25-minute session timeline blocks
  - Slide 9: Added audience descriptions (school groups, corporate)
  - Slide 10: Clarified spectators as active judges
  - Slide 11: Added Micha Goodman validation, monologue-to-dialogue evolution quote
  - Slide 12: Added A2A mitigation via WhatsApp POC
  - Slide 15: Added phase details (WhatsApp POC, 5 characters, physical mockup)
  - Slide 16: Added Research Hub as IP
  - Slide 17: Named team members (Daniel, Jonathan, Doron) + Debate Expert gap
  - Slide 18: Updated CTA to "Fund Phase 1, schedule deep-dive, green light"
- **Added CSS:** timeline-row/timeline-block for session flow, demo-btn style
- **Kept all 18 slides** (no consolidation per user decision)

### Session 7 - Comprehensive Deck Rebuild (2026-03-09)
- **Filed 3 meeting transcripts** to docs/ with structured key decision summaries
- **Complete deck rewrite** from enhanced comprehensive outline:
  - 17 main slides + 4 appendix slides (21 total, up from 18 flat)
  - New 4-act structure: Hook (4), Experience (5), Why It Works (4), The Ask (4)
  - Appendix: Technical Architecture, 13 Thinking Modes, 20 Dilemma Scenarios, Visitor Personas
  - Appendix slides navigable but shown as "A1/A4" not in main slide count
  - New tagline: "Disagree Better. Discover Together."
- **New slide content from outline:**
  - Slide 2: Expanded urgency with tribal identity defense, "muscles" framing, civic simulator gap
  - Slide 3: Puzzle metaphor with earn/lose pieces mechanic, Sherlock Holmes framing
  - Slide 4: Pure statement slide with core loop description
  - Slide 5: 6-step visitor journey with step cards (confidence levels, Gold Star concept, digital takeaway)
  - Slide 6: Architecture with Persona vs Role separation explained, fact-checking callout
  - Slide 7: Goring Ox with Shammai and Herzl added, Research Agent mention, Play Demo button
  - Slide 8: Two modes with Polarization Score and dialogue index concepts, audience targeting
  - Slide 9: Physical space with 12 kiosks, Sage Screens, spotlights, peripheral audience mechanics
  - Slide 11: A2A2H terminology (Agent-to-Agent-to-Human), WhatsApp POC mitigation
  - Slide 12: Competitive matrix (4-column comparison table vs chatbots/museums/debate AI)
  - Slide 14: 3-year roadmap (Learn/Scale/Innovate) replacing 4-phase structure
  - Slide 15: Research Hub elevated, potential academic partnerships (aspirational)
  - Slide 17: Dual CTA buttons (Get in Touch + Try the Demo)
- **Design improvements:**
  - Varied layouts: centered, split, split-wide, statement, comparison matrix
  - Larger typography: 64px h1, 56px h2, 28px tagline, 24px body
  - Team cards with dashed border for "Missing Piece"
  - Thinker chips, space feature pills, phase cards
  - All aspirational elements phrased carefully (not stated as facts)
- **All unconfirmed elements flagged as aspirational:**
  - Wheel of Sages, Polarization Score, Gold Star, university partnerships, visitor numbers

## What's Next (Backlog)
- [ ] Generate new/refined images with fresh API key
- [ ] Update demo button URL once demo is deployed
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
| 17+4 appendix structure | Deep-dive content accessible but not cluttering main narrative |
| 3-year roadmap (Learn/Scale/Innovate) | Clearer phasing than 4-phase POC/Demo/Prototype/Launch |
| Aspirational language for unconfirmed | Wheel of Sages, Polarization Score etc. not stated as facts |
| API key via env var | Previous keys leaked by being committed to git |

## File Quick Reference
- `index.html` - the deck (17 main + 4 appendix slides, inline CSS/JS)
- `CLAUDE.md` - project guide + mandatory style rules
- `STATE.md` - this file (session log + backlog)
- `generate_images.py` - image regeneration script (cinematic prompts, reads GEMINI_API_KEY env var)
- `assets/logos/` - official MOTJ logos (PNG/SVG, color/white)
- `docs/motj-brand/` - brand guide reference, STYLE_GUIDE.md
- `slides/slide-NN/hero.png` - per-slide hero images (18 total, currently architectural style)
