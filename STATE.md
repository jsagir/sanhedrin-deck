# Sanhedrin Deck - Project State

## Current Status
**Last updated:** 2026-03-10
**Phase:** Editorial redesign complete. Bilingual EN/HE, dark/light mode, new images. Deployed and live.
**Live URL:** https://sanhedrin-deck.onrender.com
**Repo:** https://github.com/jsagir/sanhedrin-deck (auto-deploy on push to master)

## What To Do Next (Pick Up Here)

### Immediate
1. **Review the live deck** at https://sanhedrin-deck.onrender.com
2. **Wire up CTA buttons** - "Approve Phase 1 POC" and "View Tech Architecture" currently have no targets
3. **Review Hebrew translations** with Daniel and Doron for accuracy

### Content Refinement
- [ ] Confirm or remove unverified claims (Yazdani Studio, 71/68 figures, 100K visitors)
- [ ] Update "View Tech Architecture" link to point to Appendix A or a separate doc
- [ ] Review all slide copy with Daniel and Doron (both EN and HE)

### Design Polish
- [ ] PDF export for leave-behind
- [ ] Speaker notes mode
- [ ] Consider product mockups/UX screenshots alongside editorial photos

## Current Deck Structure (17 + 4 Appendix)

### ACT 1: THE HOOK (Slides 1-4)
| # | Title | Layout | Image |
|---|-------|--------|-------|
| 1 | Title/Hero - "Disagree Better. Discover Together." | Hero full-bleed | slide-01/hero.png |
| 2 | The Problem - Discourse is broken | Editorial split (img right) | slide-02/hero.png |
| 3 | The Cognitive Twist - Dispute as Dynamic Puzzle | Editorial split (img left) | slide-03/hero.png |
| 4 | Value Prop - "Learn to argue in 30 min" + INPUT/ENGINE/OUTPUT | Statement | (no image) |

### ACT 2: THE EXPERIENCE (Slides 5-9)
| # | Title | Layout | Image |
|---|-------|--------|-------|
| 5 | Visitor Journey - 6-step, 25-min loop | Statement + 2x3 cards | (no image) |
| 6 | Architecture - Role-Based, 13 Thinking Modes | Editorial split (img right) | slide-06/hero.png |
| 7 | Sample Session - The Goring Ox (Rambam/Shammai/Herzl) | Editorial split (img left) | slide-07/hero.png |
| 8 | Two Configurations - Machloket vs Debate | Statement + 2 cards | (no image) |
| 9 | Physical Space - 12 kiosks, Yazdani Studio | Hero full-bleed | slide-10/hero.png |

### ACT 3: WHY IT WORKS (Slides 10-13)
| # | Title | Layout | Image |
|---|-------|--------|-------|
| 10 | POC - Rambam exhibit validated | Editorial split (img right) | slide-11/hero.png |
| 11 | Risk - 70% Solved, 30% Ahead (A2A2H) | Statement + giant typography | (no image) |
| 12 | Competitive - Matrix vs chatbots/museums/debate AI | Statement + editorial table | (no image) |
| 13 | EdTech - Debate Gym (Museum/Schools/Home) | Editorial split (img right) | slide-14/hero.png |

### ACT 4: THE ASK (Slides 14-17)
| # | Title | Layout | Image |
|---|-------|--------|-------|
| 14 | Roadmap - 4 phases (POC/Demo/Prototype/Deploy) | Statement + timeline cards | (no image) |
| 15 | Business Case - Revenue + Research Hub | Editorial split (img left) | slide-16/hero.png |
| 16 | Team - Jonathan/Daniel/Doron + Missing Piece | Statement + 2x2 cards | (no image) |
| 17 | CTA - "Give us the green light" | Hero full-bleed | slide-18/hero.png |

### APPENDIX (A1-A4)
| # | Title | Content |
|---|-------|---------|
| A1 | Technical Architecture | Kong, PostgreSQL, Vector DB, A2A2H Protocol, Orchestrator Logic |
| A2 | 13 Thinking Modes | Full list + System Role Mapping (Nasi, Av Beit Din, Devil's Advocate) |
| A3 | Dilemma Scenarios | 13 pre-built scenarios (Goring Ox, Lashon Hara, NFT Chametz, etc.) |
| A4 | Visitor Personas | Daniel the Seeker, Sarah the Balanced, Avi the Skeptic, Noa the Teacher |

## What Changed in Latest Sessions (Sessions 9-10)

### Session 10 (2026-03-10)
- **Dark mode toggle** added back - sun/moon SVG button, saves to localStorage
- **Full Hebrew translations** - all 21 slides translated using meeting transcript terminology
- Hebrew key terms: "תרבות המחלוקת", "השור שנגח", "חדר כושר לדיבייט", "בית ספר לשיח אזרחי"

### Session 9 (2026-03-10)
- **Editorial/magazine redesign** - complete visual overhaul:
  - Light base (#F5F2EB warm off-white), navy as accent
  - 3 layout types: hero full-bleed, editorial split, statement
  - Bold typography (h1 88px, h2 60px, body 24px)
  - White cards with subtle shadows
- **11 new hero images** - editorial photography style via Gemini API (gemini-2.5-flash-image)
- **Hebrew toggle** restored (EN/HE button in nav bar)
- **"School of Civic Discourse"** - renamed from "School of Disagreement"

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
| 9 | 2026-03-10 | Editorial/magazine redesign, new images, Hebrew toggle |
| 10 | 2026-03-10 | Dark mode toggle, full Hebrew translations from transcripts |

## Key Decisions
| Decision | Why |
|----------|-----|
| Single HTML file | Simplicity, no build step, easy to share |
| Montserrat over Gotham | Gotham isn't on Google Fonts; closest match |
| Render static site | Free tier, auto-deploy from GitHub |
| Editorial/magazine design | Light, bold, full-bleed. For laptop reading, not projection |
| Bilingual EN/HE | Hebrew uses meeting transcript terminology for authenticity |
| Dark mode optional | Toggle in nav, defaults to light, saves preference |
| 17+4 appendix structure | Deep-dive content accessible but not in main narrative |
| 4-phase roadmap | POC/Demo/Prototype/Deploy with concrete timelines |
| No em-dashes, no emojis | Professional tone, SVG icons only |
| API key via env var | Previous keys leaked by being committed to git |
| Editorial photography | Warm, human, magazine-feel. Replaced isometric renders |

## File Quick Reference
- `index.html` - the deck (17 main + 4 appendix, bilingual EN/HE, dark/light mode)
- `CLAUDE.md` - project guide + mandatory style rules
- `STATE.md` - this file
- `generate_images.py` - image regeneration script (editorial prompts, gemini-2.5-flash-image)
- `assets/logos/` - MOTJ logos (PNG/SVG, color/white)
- `slides/slide-NN/hero.png` - 11 hero images (editorial photography style)
- `docs/motj-brand/` - brand guide reference
- `docs/plans/` - design docs and implementation plans
- `docs/sanhedrin-kickoff-transcript.md` - Meeting 1: kickoff, role-based architecture, two modes
- `docs/sanhedrin-meeting2-transcript.md` - Meeting 2: deck walkthrough, presentation strategy
- `docs/sanhedrin-meeting3-transcript.md` - Meeting 3: two-track ASK, debate expert, timeline
