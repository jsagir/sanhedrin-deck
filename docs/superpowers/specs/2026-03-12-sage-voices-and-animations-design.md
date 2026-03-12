# Sage Voices + Slide Animations - Design Spec

**Date:** 2026-03-12
**Project:** Sanhedrin Deck (Session 13)
**Status:** Approved

## Overview

Three features for the Sanhedrin pitch deck:

1. **Sage Voice Clips** - Pre-generated ElevenLabs TTS MP3s for 9 sages on Slide 5. Each sage introduces themselves in character.
2. **Slide 5 Card Redesign** - Expand from 6 to 9 cards in a single row. Cards enlarge on hover with a play button for audio.
3. **Canvas Animations** - Two new animations for Slide 6 (Role-Based Architecture) and Slide 9 (Physical Space).

---

## Feature 1: Sage Voice Generation (ElevenLabs)

### Approach
Pre-generate 9 MP3 files using the ElevenLabs TTS API. Each sage has a unique voice, a ~15-20 second script in first person, covering: who they are, what they bring to the Sanhedrin, and their signature line. Files are committed as static assets (~150-300KB each, ~2MB total).

### Voice Mapping

| Sage | Voice | Voice ID | Thinking Mode | Stability | Similarity |
|------|-------|----------|---------------|-----------|------------|
| Abraham | Brian (Deep, Resonant) | nPczCjzI2devNBz1zQrb | #1 DISRUPTION | 0.7 | 0.8 |
| Maimonides | Rama (Wise, Philosophical) | VXFdnKU6k5XRvwf2xfEY | #10 SOLUTION | 0.75 | 0.8 |
| Herzl | Daniel (Steady Broadcaster) | onwK4e9ZLuTAKqWW03F9 | #7 GENERATIVE | 0.6 | 0.75 |
| Golda Meir | Jeanette (Audiobook, Mature) | RILOU7YmBhvwJGDGjNmP | #13 COLLECTIVE | 0.65 | 0.8 |
| Einstein | Richard Feynman (Raw Genius) | iUqvz0lkQxPhaAG37J5I | #8 IMAGINATIVE | 0.4 | 0.7 |
| Anne Frank | Jessica (Playful, Bright, Young) | cgSgspJ2msm6clMCkdW9 | #3 NARRATIVE | 0.35 | 0.75 |
| Houdini | Callum (Husky Trickster) | N2lVS1w4EtoT3dr4eOWO | #1 DISRUPTION | 0.4 | 0.7 |
| Moses | Adam (Dominant, Firm) | pNInz6obpgDQGcFmaJgB | #10 SOLUTION | 0.8 | 0.85 |
| Freud | George (Warm Storyteller) | JBFqnCBsd6RMkjVDRZzb | #5 INTERPRETIVE | 0.6 | 0.8 |

### Scripts (first person, in character)

**Abraham** (Brian - Deep, Resonant):
"I am Abraham. I was chosen because I broke my father's idols before I built anything of my own. In this council, I challenge every inherited assumption. I force you to question what you take for granted. So tell me: what if everything your fathers taught you is wrong?"

**Maimonides** (Rama - Wise, Philosophical):
"I am Maimonides. I unified Aristotelian logic with Torah law, and I bring that same rigor here. In the Sanhedrin, I classify, I systematize, I cut through confusion to find the underlying structure. There are exactly four categories, and here they are."

**Herzl** (Daniel - Steady Broadcaster):
"I am Herzl. They called me a dreamer, but I built a state from a pamphlet. In this council, I generate radical new possibilities when others see only deadlock. If you will it, it is no dream."

**Golda Meir** (Jeanette - Mature):
"I am Golda. I speak for collective fate, not personal interest. In every deliberation, I ask: what does this mean for our people? Not for me, not for you, for all of us. We have no one else."

**Einstein** (Richard Feynman - Raw Genius):
"I am Einstein. I propose thought experiments that reframe the entire discussion. I take your fixed assumptions and I ask: what if they are wrong? What if the very thing you are certain of is the thing preventing you from seeing clearly? Imagine everything you assume is wrong."

**Anne Frank** (Jessica - Playful, Bright):
"I am Anne Frank. I remind the council that grand principles are lived in small daily moments. I do not argue from theory. I testify from experience. I still believe people are good. But let me tell you what I saw."

**Houdini** (Callum - Husky Trickster):
"I am Houdini. No cage can hold a determined mind, and no framework is as solid as it appears. My role in the Sanhedrin is to find the hidden exit, the trick door, the constraint everyone else accepts. What the eyes see and the ears hear, the mind believes."

**Moses** (Adam - Dominant, Firm):
"I am Moses. I did not choose this role. I was chosen. In this council, I translate values into actionable statutes. I cut through abstraction to ask: what is the law? That is the principle. Now here is the statute."

**Freud** (George - Warm Storyteller):
"I am Sigmund Freud. What you think you believe is not what drives you. My role in this council is to expose hidden motivations, the fears beneath the arguments, the desires behind the positions. Before you insist on your reasons, let us examine your resistance."

### File Structure
```
audio/sages/
  abraham.mp3
  maimonides.mp3
  herzl.mp3
  golda-meir.mp3
  einstein.mp3
  anne-frank.mp3
  houdini.mp3
  moses.mp3
  freud.mp3
```

### Generation Script
Python script (`generate_sage_voices.py`) that:
1. Reads ELEVENLABS_API_KEY from `.env`
2. Iterates over the 9 sage configs (voice_id, script text, stability, similarity_boost)
3. Calls ElevenLabs TTS API (`/v1/text-to-speech/{voice_id}`)
4. Saves MP3 to `audio/sages/{sage-name}.mp3`
5. Uses `eleven_multilingual_v2` model for natural delivery
6. Skips generation if MP3 already exists and is non-empty (resume-safe)
7. Handles rate limits (429) with exponential backoff (1s, 2s, 4s, max 3 retries)
8. Validates response is audio/mpeg before writing

---

## Feature 2: Slide 5 Card Redesign

### Current State
- 6 sage cards in a `repeat(6, 1fr)` grid with `max-width: 1100px`
- Cards have: cover image, name, thinking mode badge
- No hover overlay (unlike Appendix E cards)
- No audio playback
- "View Full Library" button at bottom

### Target State
- **9 cards** in a single row: `repeat(9, 1fr)` with `max-width: 1400px` (widened from 1100px to accommodate 9 cards at ~140px each)
- Cards are smaller at rest (narrower to fit 9)
- **Hover behavior**: Card scales up significantly (`transform: scale(1.5)`) with elevated shadow and `z-index: 20`
- **Hover overlay**: Shows role title, description, signature quote (same data as Appendix E cards)
- **Play button**: Circular speaker icon at bottom of overlay, appears on hover
- **Playing state**: Button pulses (reuses existing `narrationPulse` keyframes), subtle blue glow ring around card border while audio plays
- **Audio**: Clicking play loads `audio/sages/{name}.mp3` via HTML5 Audio API
- **"View Full Library" button**: Retained below the grid

### Audio System Integration
Global rule: **only one audio stream at a time.**
- `playSageVoice()` calls `stopNarration()` first (stops any slide narration)
- `playNarration()` calls `stopSageVoice()` first (stops any sage audio)
- Shared globals: `sageAudio`, `isSagePlaying`, `activeSageCard`

### New Sages to Add (3)
| Sage | Image Source | Mode Badge | Role Title | Description | Quote |
|------|-------------|------------|------------|-------------|-------|
| Houdini | `https://static1.squarespace.com/static/57abd1268419c28d7981b5cd/t/5e54182e7bcf434aa9c1d312/1582569521607/JL_NewReleases_Houdini_Facebook.jpg?format=500w` | #1 DISRUPTION | The Escape Artist | No cage can hold a determined mind. Every constraint is an invitation to find the hidden exit. | "What the eyes see and the ears hear, the mind believes" |
| Moses | `https://static1.squarespace.com/static/57abd1268419c28d7981b5cd/5851a83fb8a79b5cd9df2528/58584185e58c623d6c961256/1770319874617/Moses.jpg?format=500w` | #10 SOLUTION | The Lawgiver | Translates values into actionable statutes. Cuts through abstraction to ask: what is the law? | "That is the principle; now here is the statute" |
| Sigmund Freud | `https://static1.squarespace.com/static/57abd1268419c28d7981b5cd/5851a83fb8a79b5cd9df2528/5852c1eef7e0ab7cf8248cd3/1770911668899/Freud.jpg?format=500w` | #5 INTERPRETIVE | The Unconscious Explorer | What you think you believe is not what drives you. Forces the council to examine their hidden motivations. | "Before you insist on your reasons, let us examine your resistance" |

### Card HTML (Slide 5 variant with audio)
Each card gets a `data-sage` attribute and a play button:
```html
<div class="sage-card sage-card-voice" data-sage="abraham" data-audio="audio/sages/abraham.mp3">
  <img class="sage-cover" src="..." alt="Abraham" loading="lazy">
  <div class="sage-info">
    <div class="sage-name">Abraham</div>
    <div class="sage-mode-badge">#1 DISRUPTION</div>
  </div>
  <div class="sage-overlay">
    <div class="sage-role-title">The Idol-Smasher</div>
    <div class="sage-role-desc">Challenges every inherited assumption...</div>
    <div class="sage-sig">"What if everything your fathers taught you is wrong?"</div>
    <button class="sage-play-btn" onclick="event.stopPropagation(); playSageVoice(this)" title="Hear this sage">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/>
        <path d="M15.54 8.46a5 5 0 0 1 0 7.07"/>
      </svg>
    </button>
  </div>
</div>
```

### CSS Changes
```css
/* Slide 5 voice cards */
.sage-card-voice {
  transition: transform 0.3s, box-shadow 0.3s;
}
.sage-card-voice:hover {
  transform: scale(1.5);
  z-index: 20;
  box-shadow: var(--card-hover-shadow), 0 0 0 2px var(--blue);
}
.sage-card-voice.playing {
  box-shadow: 0 0 0 3px var(--blue), 0 0 20px rgba(189,214,230,0.4);
}

/* Play button */
.sage-play-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  border: 1.5px solid rgba(189,214,230,0.4);
  background: rgba(0,48,87,0.6);
  color: #fff;
  cursor: pointer;
  margin: 8px auto 0;
  transition: background 0.2s;
}
.sage-play-btn:hover {
  background: rgba(0,48,87,0.9);
}
.sage-play-btn.playing {
  animation: narrationPulse 2s ease-in-out infinite;
  background: var(--navy);
}
```

### JS: `playSageVoice(btn)`
1. Call `stopNarration()` to stop any slide narration
2. If same sage is already playing, stop and return (toggle behavior)
3. Stop any other sage audio (`stopSageVoice()`)
4. Get `data-audio` path from closest `.sage-card-voice`
5. Create `new Audio(path)` and play
6. Add `.playing` class to button and card
7. On audio end or error, remove `.playing` classes

### Hebrew Cards
Mirror the EN cards. Play button triggers the same English audio. No Hebrew voice generation for now. Play button is visible on HE cards with no change.

### Touch Device Note
This is a desktop/laptop presentation deck. Touch hover behavior is acceptable as-is (tap triggers hover state, second tap or tap-away dismisses).

---

## Feature 3: Canvas Animations

### Animation Lifecycle
All canvas animations (including existing Slide 1 network) should only run when their slide is active. Add to the `showSlide()` function: start animation for the current slide, stop animations for all other slides. Each animation IIFE exposes `start()` and `stop()` functions on a shared `slideAnimations` object keyed by slide index.

### Slide 6 - "Dynamic Role Assignment Network"

**Note:** This is Slide 6 in current deck (Role-Based Architecture, lines ~1100-1267 in index.html).

**Concept:** Canvas layer behind the 3-column persona grid showing animated connections between personas and roles. Visualizes the core concept that personas are stable identities but roles are dynamically assigned.

**Implementation:**
- `<canvas class="role-network" id="roleNetwork">` (EN) and `id="roleNetworkHe"` (HE) positioned absolutely behind the grid content
- 3 persona nodes at top (proportional positions: 16.7%, 50%, 83.3% of canvas width)
- 9 role nodes below (3 per column, evenly spaced vertically)
- Animated edges connect persona nodes to role nodes
- **Key animation**: Edges periodically detach and reattach to different personas, showing role reassignment
- Edge color: MOTJ light blue (`rgba(189,214,230,alpha)`) with alpha fade based on "connection strength"
- Persona nodes: Larger circles (r=6), slightly brighter
- Role nodes: Smaller circles (r=3)
- Animation cycle: Every ~4 seconds, one random edge "migrates" from one persona to another (fade out old, fade in new)
- Background: Semi-transparent so grid content remains readable

**CSS:**
```css
.role-network {
  position: absolute;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  opacity: 0.6;
}
```

### Slide 9 - "Living Arena"

**Note:** This is Slide 9 in current deck (Physical Space / Yazdani Studio, lines ~1382-1420 in index.html).

**Concept:** Canvas overlay on the hero image showing a top-down circular arena. 12 kiosk nodes in a ring with participant dots flowing between them and a central pulsing hub. Reinforces "everyone participates."

**Implementation:**
- `<canvas class="arena-network" id="arenaNetwork">` (EN) and `id="arenaNetworkHe"` (HE) positioned over hero image
- 12 kiosk nodes arranged in a circle (evenly spaced, radius = 35% of canvas min dimension)
- Central hub: larger pulsing circle (sinusoidal radius oscillation)
- Participant dots: 20-30 small dots that drift along paths between kiosks and center
- Connection arcs: Thin curved lines between adjacent and opposite kiosks, opacity pulses
- Occasional "spark" effect: a bright dot travels quickly from one kiosk to another (representing cross-dialogue)
- Colors: White/light blue (`rgba(189,214,230,alpha)`) to work over the dark hero scrim
- Central hub color: Slightly warmer, brighter pulse

**Z-index stack for Slide 9:**
```
hero-bg:       z-index: 0  (background image)
arena-network: z-index: 1  (canvas animation)
hero-scrim:    z-index: 2  (dark overlay for readability)
hero-content:  z-index: 3  (text, badges)
```

**CSS:**
```css
.arena-network {
  position: absolute;
  inset: 0;
  z-index: 1;
  pointer-events: none;
  opacity: 0.5;
}
```

### Shared Animation Patterns
Both animations follow the Slide 1 Deliberation Network pattern:
- IIFE wrapping the canvas logic
- `resize()` handler on window resize
- `requestAnimationFrame` loop with start/stop lifecycle
- Time-based animation (`Date.now() * 0.001`)
- MOTJ brand colors only

---

## Constraints

- Single HTML file (index.html) - all CSS/JS inline
- No em-dashes, no emojis, SVG icons only
- MOTJ brand colors (navy #003057, blue #BDD6E6, taupe #776E64)
- Montserrat font
- API key from `.env` only, never committed
- Audio files committed to repo as static assets
- Both EN and HE versions of slides updated

---

## File Changes Summary

| File | Change |
|------|--------|
| `generate_sage_voices.py` | NEW - ElevenLabs voice generation script |
| `audio/sages/*.mp3` | NEW - 9 pre-generated voice clips |
| `index.html` | EDIT - Slide 5 expanded to 9 cards with hover+play, Slide 6 canvas, Slide 9 canvas, new CSS, new JS, animation lifecycle |
| `STATE.md` | EDIT - Session 13 log |
