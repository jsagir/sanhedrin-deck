# Sanhedrin Deck - Project State

## Current Status
**Last updated:** 2026-03-12
**Phase:** Major revision from Daniel meeting transcript. 18 main + 5 appendix slides. Deployed and live.
**Live URL:** https://sanhedrin-deck.onrender.com
**Repo:** https://github.com/jsagir/sanhedrin-deck (auto-deploy on push to master)

## What To Do Next (Pick Up Here)

### Immediate
1. **Review the live deck** at https://sanhedrin-deck.onrender.com
2. **Sage card hover bug** - cards in Appendix E not scaling on hover due to overflow-y:auto on .sage-grid clipping transforms. May need CSS rework (margin-based effect instead of transform:scale)
3. **Slide 9 (Physical Space)** - reconsider screen usage: live sentiment analysis, argument structure visualization instead of just decorative characters
4. **Slide 15 (Business Case)** - placeholder for Yoni to customize per donor
5. **Team slide position** - Daniel suggested moving to beginning of deck (not yet done, pending decision)
6. **Wire up CTA buttons** - "Approve Phase 1 POC" and "View Tech Architecture" still have no targets

### Content Refinement
- [ ] Confirm or remove unverified claims (Yazdani Studio, 100K visitors)
- [ ] Update "View Tech Architecture" link to point to Appendix A or a separate doc
- [ ] Review all slide copy with Daniel (both EN and HE)
- [ ] Daniel has a WhatsApp POC doc (written in LaTeX, ~1 year old) - integrate into Phase 1 narrative

### Design Polish
- [ ] PDF export for leave-behind
- [ ] Speaker notes mode

## Current Deck Structure (18 + 5 Appendix)

### ACT 1: THE HOOK (Slides 1-5)
| # | Title | Layout | Image |
|---|-------|--------|-------|
| 1 | Title/Hero - "Disagree Better. Discover Together." | Hero full-bleed | slide-01/hero.png |
| 2 | The Problem - Discourse is broken | Editorial split (img right) | slide-02/hero.png |
| 3 | The Cognitive Twist - Dispute as Dynamic Puzzle | Editorial split (img left) | slide-03/hero.png |
| 4 | Value Prop - "Learn to argue in 30 min" + INPUT/ENGINE/OUTPUT | Statement | (no image) |
| 5 | **NEW** Sage Showcase - 6 Jewish Lives figures (Abraham, Rambam, Herzl, Golda, Einstein, Anne Frank) | Statement + 6 sage-cards | (Jewish Lives cover images) |

### ACT 2: THE EXPERIENCE (Slides 6-10)
| # | Title | Layout | Image |
|---|-------|--------|-------|
| 6 | Visitor Journey - 6-step, 25-min loop (pre-selected dilemmas) | Statement + 2x3 cards | (no image) |
| 7 | Architecture - 3 Personas x Roles visual (Spinoza/Golda/Rambam) with Sanhedrin terminology | Statement + 3-column grid | (Jewish Lives images) |
| 8 | Sample Session - The Goring Ox (Rambam/Shammai/Herzl) | Editorial split (img left) | slide-07/hero.png |
| 9 | Two Configurations - Machloket vs Debate | Statement + 2 cards | (no image) |
| 10 | Physical Space - 12 kiosks, Yazdani Studio | Hero full-bleed | slide-10/hero.png |

### ACT 3: WHY IT WORKS (Slides 11-14)
| # | Title | Layout | Image |
|---|-------|--------|-------|
| 11 | POC - Rambam exhibit validated. Quote: "Rambam is a monologue. Sanhedrin is a multi-agent dialogue." | Editorial split (img right) | slide-11/hero.png |
| 12 | Risk - 70% Solved, 30% Ahead (A2A2H). 80 characters. | Statement + giant typography | (no image) |
| 13 | Competitive - Simplified: Chatbot vs Sanhedrin only | Statement + editorial table | (no image) |
| 14 | EdTech - Debate Gym (Museum/Schools/Home) - optional/aspirational | Editorial split (img right) | slide-14/hero.png |

### ACT 4: THE ASK (Slides 15-18)
| # | Title | Layout | Image |
|---|-------|--------|-------|
| 15 | Roadmap - 4 phases (POC/Demo/Prototype/Deploy) | Statement + timeline cards | (no image) |
| 16 | Business Case - Placeholder for Yoni | Editorial split (img left) | slide-16/hero.png |
| 17 | Team - Jonathan/Daniel/Micha Goodman/Bar-Ilan | Statement + 2x2 cards | (no image) |
| 18 | CTA - "Give us the green light" | Hero full-bleed | slide-18/hero.png |

### APPENDIX (A1-A5)
| # | Title | Content |
|---|-------|---------|
| A1 | Technical Architecture | Kong, PostgreSQL, Vector DB, A2A2H Protocol, Orchestrator Logic |
| A2 | 13 Thinking Modes | Full list + System Role Mapping (Nasi, Av Beit Din, Devil's Advocate) |
| A3 | Dilemma Scenarios | 13 pre-built scenarios (Goring Ox, Lashon Hara, NFT Chametz, etc.) |
| A4 | Visitor Personas | Daniel the Seeker, Sarah the Balanced, Avi the Skeptic, Noa the Teacher |
| A5 | The Sage Library | 24 Jewish Lives figures with hover overlays showing Sanhedrin roles |

## What Changed in Latest Sessions (Sessions 9-11)

### Session 11 (2026-03-12) - Daniel Meeting Revision
Based on transcript of Jonathan-Daniel deck walkthrough meeting:
- **New slide 5** (Sage Showcase) - 6 Jewish Lives figures with cover images before Visitor Journey
- **Slide 4** - 71 to 80 figures, ENGINE block now says "Historical AI Sages"
- **Slide 5 (now 6)** - Dilemmas changed to pre-selected, added "supra-moral, non-political" note
- **Slide 6 (now 7)** - Complete rework: 3 personas (Spinoza, Golda Meir, Rambam) each showing 3 possible roles. Uses authentic Sanhedrin terminology (Ipcha Mistabra, Shakla V'Tarya, Praklit Satan, Av Beit Din, Amora, To'en, Mesnateiz Kolektivi)
- **Slide 10 (now 11)** - Quote simplified: "Rambam is a monologue. Sanhedrin is a multi-agent dialogue." Removed "sold in one slide" and "starting from scratch"
- **Slide 11 (now 12)** - 68 to 80 characters count
- **Slide 12 (now 13)** - Simplified from 4-column matrix to Chatbot vs Sanhedrin only. Framed as "Why not just use ChatGPT?"
- **Slide 16 (now 17)** - Team updated: removed Doron, added Micha Goodman + Bar-Ilan University
- **Sage card hover fix** - overflow-visible added to sage-grid (partial fix, may still clip)

### Session 10 (2026-03-10)
- **Dark mode toggle** added back - sun/moon SVG button, saves to localStorage
- **Full Hebrew translations** - all slides translated using meeting transcript terminology

### Session 9 (2026-03-10)
- **Editorial/magazine redesign** - complete visual overhaul
- **11 new hero images** - editorial photography style via Gemini API
- **Hebrew toggle** restored (EN/HE button in nav bar)

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
| 11 | 2026-03-12 | Daniel meeting revision: new sage slide, role terminology, simplified competitive, team update |

## Key Decisions
| Decision | Why |
|----------|-----|
| Single HTML file | Simplicity, no build step, easy to share |
| Montserrat over Gotham | Gotham isn't on Google Fonts; closest match |
| Render static site | Free tier, auto-deploy from GitHub |
| Editorial/magazine design | Light, bold, full-bleed. For laptop reading, not projection |
| Bilingual EN/HE | Hebrew uses meeting transcript terminology for authenticity |
| Dark mode optional | Toggle in nav, defaults to light, saves preference |
| 18+5 appendix structure | Deep-dive content accessible but not in main narrative |
| 4-phase roadmap | POC/Demo/Prototype/Deploy with concrete timelines |
| No em-dashes, no emojis | Professional tone, SVG icons only |
| API key via env var | Previous keys leaked by being committed to git |
| Editorial photography | Warm, human, magazine-feel. Replaced isometric renders |
| Jewish Lives (Yale UP) | Character library grounded in biographical scholarship, aligned with potential donor |
| Sanhedrin role terminology | Use authentic Hebrew terms (Ipcha Mistabra, Av Beit Din, etc.) in both EN and HE |
| Chatbot vs Sanhedrin only | Simplified competitive slide per Daniel feedback - drop Museum/Debate columns |
| Remove Doron from team | Per Daniel instruction. Team is now Jonathan, Daniel, Micha Goodman, Bar-Ilan |
| Dilemmas pre-selected | Not visitor-chosen. Supra-moral, non-political. Per meeting discussion |

## File Quick Reference
- `index.html` - the deck (18 main + 5 appendix, bilingual EN/HE, dark/light mode)
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
