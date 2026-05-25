# Sanhedrin Deck — CHANGELOG

Tracks every change to the deck (`index.html` + slides/) over time. Functions as the **fallback record** so any edit can be reverse-engineered without git archeology. Each entry: date, change reference, files touched, before/after notes, deploy status.

---

## 2026-05-25 — Yoni session pivot (in progress)

**Source:** `~/MindrianRooms/motj-ecosystem/sub-rooms/sanhedrin/team-execution/2026-05-25-yoni-architecture-pivot/DECK-CHANGES.md` (20 changes across 5 waves) + temporal-awareness pass.

**Reference date:** 2026-05-25 as the "today" anchor for all timeline language.

### Wave 1A — Spelling sweep

| Item | Before | After | Status |
|---|---|---|---|
| Advisor name 1 | (none — Weisbot/Weisbrot not yet in deck) | Eli Weissbart | n/a (deck advisor list does not yet include Eli) |
| Advisor name 2 | (none — Pakhter not yet in deck) | Rabbi Ido Pachter | n/a (deck advisor list does not yet include Pachter) |
| Advisor name 3 | (none — Stern not yet in deck) | Prof. Yedidia Stern | n/a (deck advisor list does not yet include Stern) |

*Note: spelling sweep only applies to the brief / canon docs because none of these names are in the deck yet. They get ADDED in Wave 2 (C.9 advisory slide).*

### Wave 1B — POC slide (C.1)

**Lines affected:** ~2397 (EN), ~2427 (HE)

| Field | Before | After |
|---|---|---|
| POC method | "WhatsApp group to test live dynamics before building the UI" | "500K NIS POC at the Sanhedrin Space space. Two CGI sages + 2D periphery animation + live theatrical actors + focus-group kids. AI brain underneath. Three to four months." |
| Concept proven | AI dynamics only | AI dynamics AND drama-in-the-room (Yoni KPI added 25 May 2026) |

### Wave 1C — Roadmap POC card (C.2)

**Lines affected:** ~2643 (EN), ~2690 (HE)

| Field | Before | After |
|---|---|---|
| POC method | "WhatsApp group with 3 agents + 2 humans" | "Sanhedrin Space POC at 500K NIS. 2 CGI sages + periphery animation + actors + focus group. Goodman validates AI; Yoni signs off on drama." |
| Filing date | June 2026 | June 2026 (confirmed against expanded scope; flagged for re-confirmation) |

### Wave 1D — 70/30 Risk Split (C.3)

**Lines affected:** TBD (locate via "30%" or "A2A2H")

| Field | Before | After |
|---|---|---|
| 30% ahead | "Agent-to-Agent-to-Human (A2A2H) orchestration" — one question | Two open questions: (a) A2A2H orchestration. (b) Drama in the room — does the theatrical experience produce real tension, audience engagement, emotional stakes (Yoni KPI 25 May 2026). |

### Wave 1E — Hologram cleanup (C.17)

**Lines affected:** 2975, 3001, 3003, 3014, 3206, 3215, 3269, 3296, 3299, 3300 (per grep)

| Approach | Decision |
|---|---|
| Existing tech-supplier appendix has Path A (Hologram) + Path B (Non-Hologram) | Keep both paths AS REFERENCE (they remain valid technology options). Add a Yoni-decision banner at the top of the appendix noting that as of 25 May 2026, **Path B (Non-Hologram) is selected for the POC and for the working demo**. Path A is preserved for future donor or board questions about alternatives but is no longer the planning baseline. |

### Wave 1F — Budget / Ask reframe (C.5)

**Lines affected:** ~2710-2724 (Investment Required slide)

| Field | Before | After |
|---|---|---|
| Ask | Sanhedrin-only | Whole Social Lab — $25M not-to-exceed. Realistic line ~$15M. Internal split: Sanhedrin ~$7M build + ~$5M/yr ops + Immersive Wall + War Desk + rest. Sharon Jacobson presents in NYC. |

### Wave 1G — Drama as design principle (C.10)

Surfaces Yoni's design principle on existing Act 2 slides. Adds a callout to the AI & Context Engineering slide.

### Wave 1H — Temporal awareness pass

Updates the deck to be aware of 2026-05-25 as the "today" anchor. Every "this year," "this quarter," "next month" reference inspected and updated. Roadmap dates re-anchored against the new reference point.

| Element | Before | After |
|---|---|---|
| Roadmap "Pre-Kickoff (Now)" | Implicit March 2026 | Becomes "Pre-Kickoff (Mar 2026, complete)" |
| Roadmap "Kickoff Post-Passover" | Implicit April 2026 | Becomes "Kickoff (Apr 2026, complete)" |
| Roadmap "RFP Issued" | May 2026 | Becomes "RFP (May 2026, in progress)" |
| Roadmap "Federal Grant + POC" | Jun 2026 | Stays Jun 2026 (POC scope upgraded — see Wave 1B/1C) |
| Roadmap "Working Demo" | Sep-Nov 2026 | End-2026 to early-2027 (Daniel slip notes from 25 May) |
| Roadmap "Deployment" | Jun-Jul 2027 | Unchanged |

### Wave 2-3 — Pedagogy + appendices (NOT YET EXECUTED)

| # | Description | Status |
|---|---|---|
| C.4 | Architecture diagram replacement (two-layer AI) | Pending — needs SVG asset port from brief |
| C.6 | New "Audience IS the Sanhedrin" slide | Pending — flagged tentative pending Miri + Yagil sign-off |
| C.8 | Visitor journey slide upgrade | Pending — needs SVG port from brief |
| C.9 | Advisory slide additions (Weissbart, Stern, Pachter) | Pending — Wave 2 |
| C.11 | New "Hologram conversion" slide | Pending — Wave 2 |
| C.12 | Animation film callout | Pending — Wave 3 |
| C.13 | Appendix Q rewrite (POC Definition) | Pending — Wave 3 |
| C.14 | Advisor appendix (full bios) | Pending — Wave 3 |
| C.15 | Museum-side onboarding role appendix | Pending — Wave 3 |
| C.7 | CTA button (no change needed once C.13 lands) | Pending |
| C.18 | Acronym sweep verification | Pending — final pass |
| C.19 | Roadmap synchronization | Folded into Wave 1H |
| C.20 | STATE.md update | Pending — final pass |

### Deploy

| Wave | Commit | Pushed | Render redeploy |
|---|---|---|---|
| Wave 1 (this run) | TBD | Pending | Triggered automatically on push to master |

---

## Rollback procedure

If any Wave 1 change breaks the deck:
1. `cd ~/sanhedrin-deck`
2. `git log --oneline -10` to find the last known-good commit
3. `git revert <commit-hash>` (preferred — keeps history) OR `git reset --hard <commit-hash>` (destructive — only if revert produces conflicts)
4. `git push origin master` to redeploy the known-good version

The Wave 1 commits are intentionally small and labeled with the change reference (C.1, C.2, etc.) so rollback can be surgical.

---

## Prior history

The deck's pre-25-May history is captured in `assets/deck/sanhedrin-deck-STATE.md` and is not duplicated here. This CHANGELOG begins at 2026-05-25 (Yoni pivot) and tracks every change forward from that point.
