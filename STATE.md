# Sanhedrin Deck - Project State

## Current Status
**Last updated:** 2026-03-13 (Session 20)
**Phase:** 22 main slides (3 team slides) + 8 appendix (A-F, P, Q). 12 sages with voices. Deployed and live.
**Live URL:** https://sanhedrin-deck.onrender.com
**Repo:** https://github.com/jsagir/sanhedrin-deck (auto-deploy on push to master)

## What To Do Next (Pick Up Here)

### Immediate
1. **Slide 15 (Business Case)** - placeholder for Yoni to customize per donor
2. **Wire up CTA buttons** - "Approve Phase 1 POC" and "View Tech Architecture" still have no targets

### Content Refinement
- [ ] Confirm or remove unverified claims (Yazdani Studio, 100K visitors)
- [ ] Update "View Tech Architecture" link to point to Appendix A or a separate doc
- [ ] Review all slide copy with Daniel (both EN and HE)
- [ ] Daniel has a WhatsApp POC doc (written in LaTeX, ~1 year old) - integrate into Phase 1 narrative

### Design Polish
- [ ] PDF export for leave-behind
- [ ] Speaker notes mode

## Current Deck Structure (20 + 5 Appendix)

### ACT 1: THE HOOK (Slides 1-7)
| # | Title | Layout | Image |
|---|-------|--------|-------|
| 1 | Title/Hero - "Disagree Better. Discover Together." | Hero full-bleed | slide-01/hero.png |
| 2 | The Problem - Discourse is broken | Editorial split (img right) | slide-02/hero.png |
| 3 | Team: Core MOTJ Team (Daniel Muller, Jonathan Sagir, Marla Supnick, Sharon Jacobson) | Statement + 4-col grid | (headshot placeholders) |
| 3B | Team: Bar-Ilan Academic Partner (Jonathan Schler, Alex Tal) | Statement + 2-col grid | (headshot placeholders) |
| 3C | Team: Advisory (Micha Goodman, Miri Dayan) | Statement + 2-col grid | (headshot placeholders) |
| 4 | The Cognitive Twist - Dispute as Dynamic Puzzle | Editorial split (img left) | slide-03/hero.png |
| 5 | Value Prop - "Learn to argue in 30 min" + INPUT/ENGINE/OUTPUT | Statement | (no image) |
| 6 | Sage Showcase - 12 sages in 4-col carousel (Abraham, Maimonides, Spinoza, Herzl, Golda, Einstein, Anne Frank, Houdini, Moses, Freud + 2 more) | Statement + carousel | (Jewish Lives covers) |
| 7 | Visitor Journey - 6-step, 25-min loop (pre-selected dilemmas) | Statement + 2x3 cards | (no image) |

### ACT 2: THE EXPERIENCE (Slides 8-12)
| # | Title | Layout | Image |
|---|-------|--------|-------|
| 8 | Architecture - 3 Personas x Roles visual with Sanhedrin terminology | Statement + 3-column grid | (Jewish Lives images) |
| 9 | Sample Session - The Goring Ox | Editorial split (img left) | slide-07/hero.png |
| 10 | Two Configurations - Machloket vs Debate | Statement + 2 cards | (no image) |
| 11 | Physical Space - 12 kiosks, Yazdani Studio | Hero full-bleed | slide-10/hero.png |

### ACT 3: WHY IT WORKS (Slides 12-15)
| # | Title | Layout | Image |
|---|-------|--------|-------|
| 12 | POC - Rambam exhibit validated | Editorial split (img right) | slide-11/hero.png |
| 13 | Risk - 70% Solved, 30% Ahead (A2A2H). 80 characters. | Statement + giant typography | (no image) |
| 14 | Competitive - Chatbot vs Sanhedrin only | Statement + editorial table | (no image) |
| 15 | EdTech - Debate Gym (Museum/Schools/Home) | Editorial split (img right) | slide-14/hero.png |

### ACT 4: THE ASK (Slides 16-20)
| # | Title | Layout | Image |
|---|-------|--------|-------|
| 16 | Roadmap - 4 phases (POC/Demo/Prototype/Deploy) | Statement + timeline cards | (no image) |
| 17 | Business Case - Placeholder for Yoni | Editorial split (img left) | slide-16/hero.png |
| 18 | CTA - "Give us the green light" | Hero full-bleed | slide-18/hero.png |

### APPENDIX (A1-A5)
| # | Title | Content |
|---|-------|---------|
| A1 | Technical Architecture | Kong, PostgreSQL, Vector DB, A2A2H Protocol, Orchestrator Logic |
| A2 | 13 Thinking Modes | Full list + System Role Mapping (Nasi, Av Beit Din, Devil's Advocate) |
| A3 | Dilemma Scenarios | 13 pre-built scenarios (Goring Ox, Lashon Hara, NFT Chametz, etc.) |
| A4 | Visitor Personas | Daniel the Seeker, Sarah the Balanced, Avi the Skeptic, Noa the Teacher |
| A5 | The Sage Library | All 80 Jewish Lives figures with hover overlays showing Sanhedrin roles |

## What Changed in Latest Sessions

### Session 20 (2026-03-13) - HE Scatter Fix, Dashboard Tour, Sage Hover Fix
- **HE scatter plot SVG axis labels**: Bumped font-size from 7 to 10 (axis labels) and 6 to 9 (inner labels: ideal zone, start, now) to match EN. Also aligned x position of rotated label
- **Puzzle click-to-place verified**: Code reviewed - e.currentTarget usage correct, 75% hit area working, fly animation with cubic ease-out, both mouse and touch support via touchend
- **Appendix F dashboard onboarding tour**: 9-step guided walkthrough of all dashboard widgets (sentiment, radar, scatter, video, sages, roles, visitors, heatmap, schedule). GUIDE button added to both EN and HE headers. Reuses existing tour overlay infrastructure. Scroll-into-view for heatmap/schedule steps
- **Sage card hover fix (Appendix E)**: Moved overflow-y:auto from .sage-grid to new .sage-grid-scroll wrapper. Grid itself now overflow:visible so hover transforms (scale 1.03 + translateY) are no longer clipped. Both EN and HE grids wrapped
- IDs added to all EN dashboard widgets for tour targeting: dash-sentiment, dash-radar, dash-scatter, dash-video, dash-sages, dash-roles, dash-visitors, dash-heatmap, dash-schedule

### Session 19 (2026-03-13) - Dashboard Typography Scale, Proportions Rebalance, Video Controls
- **Dashboard grid rebalanced**: Changed from `260px 1fr 260px` (~20/60/20) to `1fr 1.2fr 1fr` (~30/40/30). Side panels now wide enough for legible data tiles
- **Full typography scale applied** (12px minimum rule, WCAG-compliant):
  - Section headers: 10px -> 13px mono + letter-spacing: 1px (technical look without being invisible)
  - Sentiment percentages: 18px -> **24px bold** (the data pops)
  - Sentiment labels: 13px -> 15px
  - Hero numbers (L'Shem Shamayim / Visitors): 36-38px -> **40px bold**
  - Sage names: 14px -> 15px, status badges: 10px -> 12px
  - Role names: 13px -> 15px, assignees: 11px -> 13px
  - Heatmap minute numbers: 7px -> 11px, row labels: 10px -> 13px, annotations: 9px -> 12px
  - Heatmap legend: 8px -> 12px, cell height: 18px -> 22px
  - Schedule times: 10px -> 12px, schedule names: 11px -> 13-15px
  - Radar/scatter axis labels: SVG font-size 7-9 -> 10-12 bold
  - Video overlay LIVE badge: 9px -> 12px, cam label: 9px -> 12px
  - Scatter subtitle: 9px -> 13px
- **Video player fixed**: Replaced 16:8 cropped aspect ratio with proper **16:9** (object-fit: contain). Native browser controls now fully visible (play, pause, timeline, volume)
- **Video overlay redesign**: Replaced text buttons ("INJECT CONTEXT", "FLAG") with **SVG icon buttons** (plus icon + flag icon) with tooltips. Cleaner control-room aesthetic, no legibility issue
- **Hebrew dashboard full-bleed fix**: Changed `max-width: 1200px; margin: 0 auto` to `max-width: 100%; margin: 0; padding: 16px 28px 40px` (matches English)
- **Dashboard scroll fix**: Added `slide--appendix` class to Appendix F section, changed layout-statement from `height: 100%` to `height: auto; justify-content: flex-start`. Session schedule no longer cut off at bottom
- All changes applied to both EN and HE dashboards

### Session 18 (2026-03-13) - Jigsaw Bezier, Control Room Dashboard, Behavioral Analytics
- **Slide 4 jigsaw pieces**: Replaced arc-based tabs with bezier curve neck+bulb jigsaw profile. Per-piece tab directions (in/out) that interlock with neighbors. Outer edges flat. Piece size reduced to 0.82x for breathing room. Labels enlarged (18% of piece width, weight 800). Hit area doubled (30% margin)
- **Appendix P/Q text alignment fix**: Added `text-align: left` to `.sow-doc` - was inheriting `text-align: center` from `.slide` parent
- **Appendix F: Experience Control Room dashboard** - complete redesign from simple video+timetable to live facilitator intelligence dashboard:
  - 3-column layout: metrics | video | metrics
  - Header: "Experience Control Room" with pulsing green SESSION LIVE indicator
  - Left panel: Sentiment Analysis bars (constructive 72%, adversarial 18%, neutral 10%)
  - **Sanhedrin Rules Radar Chart**: 5-axis spider web (Premise, Logic, Humility, Grounding, Curiosity) showing L'Shem Shamayim Index as a pentagon shape (82/100)
  - **Polarization vs Empathy Scatter Plot**: Journey trail from high-polarization/low-empathy start to bottom-right ideal zone
  - Right panel: Sages at Play (Rambam speaking, Spinoza analyzing, Einstein listening, Golda standby), Roles at Play (Nasi, Ipcha Mistabra, Shakla V'Tarya, Av Beit Din), Visitors (8/12 active)
  - **Discourse Rhythm Heatmap**: Full-width 25-minute timeline, 5 rows (Human 1, AI Rambam, Human 2, AI Spinoza, System). Color-coded: blue=curiosity, orange=friction, gold=synthesis, red=violation. Annotations show ad-hominem flag, disengagement warning, convergence zone
  - Video frame: widescreen 16:8 aspect ratio, crops top/bottom (hides NotebookLM logo), preserves full width. Cyan corner accents
  - Compact horizontal session schedule at bottom
  - Full bilingual EN/HE
- **dashPulse CSS animation** added for live status indicator

### Session 17 (2026-03-13) - Interactive Puzzle, Dark Mode Fixes, Video Appendix, Animation Index Fix
- **Slide 4 (Cognitive Twist): Interactive drag-and-snap jigsaw puzzle**
  - 4 jigsaw pieces: Arguments (matte green), Facts (matte orange), Empathy (matte red), Sentiment (matte purple)
  - Pieces float scattered, user drags them to dashed ghost targets
  - Snap-to-place with cyan spark burst, checkmark on placed pieces
  - **Gradient merge**: placed pieces blend colors toward neighbors (islands merging into shared lake)
  - **Venn center**: glowing intersection appears as pieces connect, "Shared Discourse" label when all 4 placed
  - Auto-resets after 5 seconds. Mouse + touch. Bilingual EN/HE labels
  - **STILL NEEDS WORK**: jigsaw tab shape may still look too tile-like. Tabs are arc-based with 22% size. May need bezier curves or more pronounced interlocking shape in next session
- **Dark mode contrast fix**: All `background: var(--navy); color: #fff` hardcoded to `#003057`. In dark mode `--navy` flips to light blue making white text unreadable. Fixed: ENGINE box, 6 persona cards, View Full Library buttons, narration btn, back btn, tour btn, sage play btn
- **Canvas animation indices fixed**: All were wrong since team slides were inserted at position 3. Polarization [1] correct, puzzle [5], role network [9], arena [12]
- **Appendix F: Explainer Video** with daily session timetable
  - Video: `video/explainer.mp4` (AI Sages & The Art of Disagreement, 33MB)
  - 8 dilemma scenarios scheduled 09:00-16:30, rotates daily, 25-min sessions
  - Video frame: navy border crops bottom-right to hide NotebookLM logo naturally via offset margins
  - Quick nav updated, onboarding tour count updated to 8 appendices
  - Bilingual EN/HE

### Session 16 (2026-03-13) - Narration, Onboarding, Polarization Anim, Value Prop Redesign
- **22 narration MP3s generated** via ElevenLabs (Daniel voice, eleven_multilingual_v2)
- **New audio path**: `audio/narration/slide-NN.mp3` (was `slides/slide-NN/narration.mp3`)
- **Narration scripts rewritten** from scratch for new 22-slide structure
- **Content aligned with Daniel meeting transcript**: CTO title, Miri Dayan as Lt. Col. Ret./School of Civic Discourse principal, WhatsApp-based POC, Maimonides Pavilion co-leadership, 6-phase roadmap with April RFP
- **index.html updated**: narration audio path changed, appendix slide guard added (no narration on appendix slides)
- **generate_narration.py rewritten**: new 22-slide narration texts, outputs to audio/narration/, uses elevenlabs SDK
- **RESOLVED**: "Narration MP3s need complete redo" from Session 15
- **Onboarding tour**: 8-step first-visit highlight walkthrough of all UI components (progress bar, counter, acts, quick nav, language, dark mode, arrows, narration). Auto-starts, skippable, saved to localStorage.
- **CLAUDE.md rule #7**: narration MP3 sync required on any slide structure change
- **Slide 2 (The Problem)**: "polarized society" bolded in EN+HE. Live canvas animation: 40 particles splitting into red/blue camps, central crack line, broken bridge lines, same-side network connections. Starts/stops on slide transition.
- **Slide 5 (Value Prop) full redesign** per Daniel's feedback:
  - Headline changed: "Discourse Training" (was "Learn to disagree better in 30 minutes")
  - Label: "What This Is" (was "Key Value Proposition")
  - Flow diagram with SVG arrows: INPUT -> ENGINE -> OUTPUT
  - ENGINE box visually dominant (dark navy, shadow, larger), labeled "Multi-Agent Deliberation"
  - INPUT/OUTPUT boxes light with border (clear hierarchy, 3-4 words each)
  - 3 sage portraits (Rambam, Einstein, Golda) inside ENGINE box
  - Removed generic "AI-powered immersive space" phrasing
  - slide-07.mp3 narration regenerated to match
- **Navigation fix**: duplicate showSlide wrapper was causing infinite recursion. Merged polarization into slideAnimations registry.

### Session 15 (2026-03-13) - Tech Slides, Appendices P/Q, Back Button
- **Two new tech slides** (11: AI & Context Engineering, 12: Debate & Discourse Framework) with drill-down links to Appendix A/B
- **Appendix P** (Program Scope) and **Appendix Q** (POC Definition) added as SoW-style documents with sticky TOC
- **Roadmap** revamped: 6 phases, RFP moved to April, hyperlinks from cards to appendices
- **Floating "Back to Slide" button** on all appendix slides for presentation flow
- **RTL alignment fix** for Hebrew appendix content
- **Daniel & Jonathan bios** updated with Maimonides Pavilion leadership
- **All slides renumbered** (22 main + 7 appendix)
- **DONE**: Narration MP3s regenerated in Session 16

### Session 14 (2026-03-13) - Team Slides + Sage Carousel + Spinoza
- **Team slide moved** from position 16 to position 3 per Daniel's feedback
- **Team expanded to 3 slides** with 8 members across 3 sections:
  - Slide 3: Core MOTJ Team (Daniel Muller PhD, Jonathan Sagir MBA, Marla Supnick, Sharon Jacobson)
  - Slide 3B: Bar-Ilan Academic Partner (Jonathan Schler PhD, Alex Tal PhD)
  - Slide 3C: Advisory Team (Micha Goodman PhD, Miri Dayan Lt. Col. Ret.)
- Each team member has 80px circular headshot placeholder, full unabridged bio text
- **Spinoza added** as 12th sage (between Maimonides and Herzl) with ElevenLabs "Roger" voice
- **Sage carousel** on Slide 5: 4-col grid with prev/next navigation and dot indicators (replaces single-row scroll)
- **Sage card CSS fixes**: overlay stacking (removed position:relative), play button underline bleed-through (z-index stacking context)
- **Deck audit** against March 12 revision guide: 12/18 items done, 3 partial, 3 not done
- All slides renumbered after Team insertion (old 3->4, 4->5, etc.)
- Bilingual EN/HE for all new content

### Session 13 (2026-03-12) - Sage Voices + Canvas Animations
- **ElevenLabs voice clips** for 9 sages: Abraham, Maimonides, Herzl, Golda Meir, Einstein, Anne Frank, Houdini, Moses, Freud
- Each sage has a unique ElevenLabs voice with custom stability/similarity settings
- Einstein uses "Bill" voice (Feynman restricted to Reader App)
- **Slide 5 expanded** from 6 to 9 sage cards (added Houdini, Moses, Freud)
- **Slide 5 hover redesign**: cards scale to 1.5x on hover showing overlay with role title, description, quote, and play button
- **Play button** on each card triggers sage voice clip (audio/sages/*.mp3)
- **Audio system integration**: sage voice, slide narration, and slide transitions all stop competing audio
- **Slide 6 canvas animation**: "Dynamic Role Assignment Network" with 3 persona nodes, 9 role nodes, edges that migrate between personas every 4 seconds
- **Slide 9 canvas animation**: "Living Arena" with 12 kiosk nodes in a circle, central pulsing hub, 25 drifting participant dots, spark effects
- **Animation lifecycle**: canvas animations start/stop on slide transitions (not always-on)
- Grid widened from 1100px to 1400px for 9 cards, gap reduced to 12px
- Both EN and HE versions updated with full Hebrew overlays

### Session 12 (2026-03-12) - Full 80-Sage Library
- **Appendix E expanded** from 24 to all 80 Jewish Lives figures
- All 80 sages have real book cover images from Jewish Lives Squarespace CDN
- Each sage has: cover image, EN+HE name, thinking mode badge, hover overlay with role title, description, signature quote
- 9 domains: Antiquity (9), Philosophy/Religion (12), Law/Politics (16), Literary Arts (13), Arts/Culture (9), Entertainment (13), Business (1), Rogues (2), Science (4)
- **"View Full Library" button** added to Slide 5 (EN + HE) linking to Appendix E via goToSageLibrary() JS function
- Sage Library appendix section given id="sage-library" for targeting
- Pending: visitor journey dilemma scheduling concept (from user feedback)

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
| 12 | 2026-03-12 | Full 80-sage library: expanded Appendix E from 24 to 80 Jewish Lives figures with real cover images, added navigation button from Slide 5 |
| 13 | 2026-03-12 | Sage voices (ElevenLabs, 9 sages), Slide 5 hover+play redesign, canvas animations for Slides 6+9 |
| 14 | 2026-03-13 | Team moved to slide 3, split into 3 slides (8 members), Spinoza added as 12th sage, sage carousel with navigation, CSS fixes |
| 15-19 | 2026-03-13 | Tech slides, appendices P/Q, narration, onboarding tour, sage voices, dashboard, typography scale |
| 20 | 2026-03-13 | HE scatter fix, dashboard tour (9 steps), sage hover fix, puzzle verification |

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
| All 80 sages with real images | No placeholders - every sage uses actual Jewish Lives (Yale UP) cover art from Squarespace CDN |
| Slide 5 links to full library | "View Full Library" button navigates from preview (9 sages) to complete Appendix E (80 sages) |
| ElevenLabs for sage voices | Each sage gets a unique voice matching their character; Einstein uses Bill (Feynman restricted) |
| Canvas animations lifecycle | Start/stop tied to slide transitions to avoid running 3 animation loops simultaneously |
| Team slides at position 3 | Daniel requested team near beginning of deck, not end |
| 3 separate team slides | 8 members across Core/Academic/Advisory sections too dense for 1 slide |
| Spinoza as 12th sage | Surprising pick, fits philosophy/ethics theme. Roger voice (non-popular) |
| Sage carousel (4-col paginated) | Replaced single horizontal row; cleaner for 12 cards with room to grow |

## File Quick Reference
- `index.html` - the deck (22 main + 7 appendix, bilingual EN/HE, dark/light mode)
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
