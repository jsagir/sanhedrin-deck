# Sanhedrin Deck - Project State

## Current Status
**Last updated:** 2026-03-09
**Phase:** Final deck structure locked. English-only, 17+4 appendix. Deployed and live.
**Live URL:** https://sanhedrin-deck.onrender.com
**Repo:** https://github.com/jsagir/sanhedrin-deck (auto-deploy on push to master)

## What To Do Next (Pick Up Here)

### Immediate
1. **Review the live deck** at https://sanhedrin-deck.onrender.com
2. **Regenerate hero images** if desired (current images are isometric architectural style):
   - Get fresh Gemini API key from https://aistudio.google.com/apikey
   - `export GEMINI_API_KEY="your-key"` (do NOT commit)
   - `cd ~/sanhedrin-deck && python3 generate_images.py`
3. **Wire up CTA buttons** - "Approve Phase 1 POC" and "View Tech Architecture" currently have no targets

### Content Refinement
- [ ] Review all slide copy with Daniel and Doron
- [ ] Confirm or remove unverified claims (Yazdani Studio, 71/68 figures, 100K visitors)
- [ ] Add Hebrew version back if needed for Yoni presentation
- [ ] Update "View Tech Architecture" link to point to Appendix A or a separate doc

### Design Polish
- [ ] Generate new hero images matching the final slide content
- [ ] Consider replacing isometric images with product mockups/UX screenshots
- [ ] PDF export for leave-behind
- [ ] Speaker notes mode

## Current Deck Structure (17 + 4 Appendix)

### ACT 1: THE HOOK (Slides 1-4)
| # | Title | Layout | Image |
|---|-------|--------|-------|
| 1 | Title/Hero - "Disagree Better. Discover Together." | Centered | slide-01/hero.png |
| 2 | The Problem - Discourse is broken | Split | slide-02/hero.png |
| 3 | The Cognitive Twist - Dispute as Dynamic Puzzle | Split | slide-03/hero.png |
| 4 | Value Prop - "Learn to argue in 30 min" + INPUT/ENGINE/OUTPUT | Centered | (no image) |

### ACT 2: THE EXPERIENCE (Slides 5-9)
| # | Title | Layout | Image |
|---|-------|--------|-------|
| 5 | Visitor Journey - 6-step, 25-min loop | Split + step grid | slide-05/hero.png |
| 6 | Architecture - Role-Based, 13 Thinking Modes | Split | slide-06/hero.png |
| 7 | Sample Session - The Goring Ox (Rambam/Shammai/Herzl) | Split | slide-07/hero.png |
| 8 | Experience Modes - Machloket vs Debate | Centered + mode cards | (no image) |
| 9 | Physical Space - 12 kiosks, Yazdani Studio | Split | slide-10/hero.png |

### ACT 3: WHY IT WORKS (Slides 10-13)
| # | Title | Layout | Image |
|---|-------|--------|-------|
| 10 | POC - Rambam exhibit validated | Split + quote block | slide-11/hero.png |
| 11 | Risk - 70% Solved, 30% Ahead (A2A2H) | Split | slide-12/hero.png |
| 12 | Competitive - Matrix vs chatbots/museums/debate AI | Split-wide + table | slide-13/hero.png |
| 13 | EdTech - Debate Gym (Museum/Schools/Home) | Split | slide-14/hero.png |

### ACT 4: THE ASK (Slides 14-17)
| # | Title | Layout | Image |
|---|-------|--------|-------|
| 14 | Roadmap - 4 phases (POC/Demo/Prototype/Deploy) | Centered + phase cards | (no image) |
| 15 | Business Case - Revenue + Research Hub | Split | slide-16/hero.png |
| 16 | Team - Jonathan/Daniel/Doron + Missing Piece | Centered + team cards | (no image) |
| 17 | CTA - "Give us the green light" | Centered + quote | slide-18/hero.png |

### APPENDIX (A1-A4)
| # | Title | Content |
|---|-------|---------|
| A1 | Technical Architecture | Kong, PostgreSQL, Vector DB, A2A2H Protocol, Orchestrator Logic |
| A2 | 13 Thinking Modes | Full list + System Role Mapping (Nasi, Av Beit Din, Devil's Advocate) |
| A3 | Dilemma Scenarios | 13 pre-built scenarios (Goring Ox, Lashon Hara, NFT Chametz, etc.) |
| A4 | Visitor Personas | Daniel the Seeker, Sarah the Balanced, Avi the Skeptic, Noa the Teacher |

## What Changed in Latest Session (Session 8)

User manually revised the deck HTML with these changes:
- **Removed Hebrew/bilingual** - English-only deck (no more EN/HE toggle)
- **Removed language toggle buttons** from nav bar
- **Added INPUT/ENGINE/OUTPUT pillars** to value prop slide (slide 4)
- **Yazdani Studio** attribution restored on physical space slide
- **4-phase roadmap** (POC Now / Demo 3mo / Prototype 6mo / Deploy 12mo) replacing 3-year structure
- **CTA buttons changed:** "Approve Phase 1 POC" + "View Tech Architecture"
- **Revised 13 Thinking Modes** names (Flexible, Narrative-Visual, Active, Generative, Imaginative, Creative, Innovation-Focused, Entrepreneurial, Collective)
- **Enriched visitor personas** with ages, backgrounds, Noa the Teacher added
- **Copy refinements** throughout all slides
- **"Two Configurations"** instead of "Two Modes" on slide 8

## Session History

| Session | Date | Summary |
|---------|------|---------|
| 1 | 2026-03-09 | Initial 18-slide build, dark cinematic design |
| 2 | 2026-03-09 | Generated 18 hero images via Gemini API |
| 3 | 2026-03-09 | MOTJ rebrand, GitHub deploy, Render setup |
| 4 | 2026-03-09 | Brand compliance, dark/light mode, EN/HE toggle |
| 5 | 2026-03-09 | Killer presentation redesign, investor review feedback |
| 6 | 2026-03-09 | Isometric rebuild, content refresh from definitive outline |
| 7 | 2026-03-09 | Comprehensive rebuild (17+4), meeting transcripts filed |
| 8 | 2026-03-09 | User-revised deck: EN-only, refined content, 4-phase roadmap |

## Key Decisions
| Decision | Why |
|----------|-----|
| Single HTML file | Simplicity, no build step, easy to share |
| Montserrat over Gotham | Gotham isn't on Google Fonts; closest match |
| Render static site | Free tier, auto-deploy from GitHub |
| English-only (Session 8) | Primary audience is Yoni (internal), Hebrew can be added back later |
| 17+4 appendix structure | Deep-dive content accessible but not in main narrative |
| 4-phase roadmap | POC/Demo/Prototype/Deploy with concrete timelines |
| No em-dashes, no emojis | Professional tone, SVG icons only |
| API key via env var | Previous keys leaked by being committed to git |

## File Quick Reference
- `index.html` - the deck (17 main + 4 appendix, EN-only, inline CSS/JS)
- `CLAUDE.md` - project guide + mandatory style rules
- `STATE.md` - this file
- `generate_images.py` - image regeneration script (reads GEMINI_API_KEY from .env)
- `assets/logos/` - MOTJ logos (PNG/SVG, color/white)
- `slides/slide-NN/hero.png` - 18 hero images (isometric architectural style)
- `docs/motj-brand/` - brand guide reference
- `docs/sanhedrin-kickoff-transcript.md` - Meeting 1: kickoff, role-based architecture, two modes
- `docs/sanhedrin-meeting2-transcript.md` - Meeting 2: deck walkthrough, presentation strategy
- `docs/sanhedrin-meeting3-transcript.md` - Meeting 3: two-track ASK, debate expert, timeline
