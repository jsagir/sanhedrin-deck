# Sage Voices + Slide Animations Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add ElevenLabs-generated voice clips for 9 sages on Slide 5, redesign Slide 5 cards with hover+play, and add canvas animations to Slides 6 and 9.

**Architecture:** Three independent features in a single HTML file. Voice generation is a Python script (run once, produces static MP3s). Card redesign and animations are CSS/JS edits to index.html. Audio system integrates with existing narration infrastructure.

**Tech Stack:** Python 3 + ElevenLabs SDK, HTML5 Canvas, inline CSS/JS in index.html

**Spec:** `docs/superpowers/specs/2026-03-12-sage-voices-and-animations-design.md`

---

## Chunk 1: Voice Generation Script + Audio Files

### Task 1: Create the ElevenLabs voice generation script

**Files:**
- Create: `generate_sage_voices.py`
- Create: `audio/sages/` (directory)

- [ ] **Step 1: Create audio directory**

```bash
mkdir -p audio/sages
```

- [ ] **Step 2: Write the generation script**

Create `generate_sage_voices.py`:

```python
#!/usr/bin/env python3
"""Generate sage voice clips using ElevenLabs TTS API."""

import os
import time
from pathlib import Path
from dotenv import load_dotenv
from elevenlabs import ElevenLabs

load_dotenv()

client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

OUTPUT_DIR = Path("audio/sages")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

SAGES = [
    {
        "name": "abraham",
        "voice_id": "nPczCjzI2devNBz1zQrb",
        "stability": 0.7,
        "similarity_boost": 0.8,
        "text": "I am Abraham. I was chosen because I broke my father's idols before I built anything of my own. In this council, I challenge every inherited assumption. I force you to question what you take for granted. So tell me: what if everything your fathers taught you is wrong?"
    },
    {
        "name": "maimonides",
        "voice_id": "VXFdnKU6k5XRvwf2xfEY",
        "stability": 0.75,
        "similarity_boost": 0.8,
        "text": "I am Maimonides. I unified Aristotelian logic with Torah law, and I bring that same rigor here. In the Sanhedrin, I classify, I systematize, I cut through confusion to find the underlying structure. There are exactly four categories, and here they are."
    },
    {
        "name": "herzl",
        "voice_id": "onwK4e9ZLuTAKqWW03F9",
        "stability": 0.6,
        "similarity_boost": 0.75,
        "text": "I am Herzl. They called me a dreamer, but I built a state from a pamphlet. In this council, I generate radical new possibilities when others see only deadlock. If you will it, it is no dream."
    },
    {
        "name": "golda-meir",
        "voice_id": "RILOU7YmBhvwJGDGjNmP",
        "stability": 0.65,
        "similarity_boost": 0.8,
        "text": "I am Golda. I speak for collective fate, not personal interest. In every deliberation, I ask: what does this mean for our people? Not for me, not for you, for all of us. We have no one else."
    },
    {
        "name": "einstein",
        "voice_id": "iUqvz0lkQxPhaAG37J5I",
        "stability": 0.4,
        "similarity_boost": 0.7,
        "text": "I am Einstein. I propose thought experiments that reframe the entire discussion. I take your fixed assumptions and I ask: what if they are wrong? What if the very thing you are certain of is the thing preventing you from seeing clearly? Imagine everything you assume is wrong."
    },
    {
        "name": "anne-frank",
        "voice_id": "cgSgspJ2msm6clMCkdW9",
        "stability": 0.35,
        "similarity_boost": 0.75,
        "text": "I am Anne Frank. I remind the council that grand principles are lived in small daily moments. I do not argue from theory. I testify from experience. I still believe people are good. But let me tell you what I saw."
    },
    {
        "name": "houdini",
        "voice_id": "N2lVS1w4EtoT3dr4eOWO",
        "stability": 0.4,
        "similarity_boost": 0.7,
        "text": "I am Houdini. No cage can hold a determined mind, and no framework is as solid as it appears. My role in the Sanhedrin is to find the hidden exit, the trick door, the constraint everyone else accepts. What the eyes see and the ears hear, the mind believes."
    },
    {
        "name": "moses",
        "voice_id": "pNInz6obpgDQGcFmaJgB",
        "stability": 0.8,
        "similarity_boost": 0.85,
        "text": "I am Moses. I did not choose this role. I was chosen. In this council, I translate values into actionable statutes. I cut through abstraction to ask: what is the law? That is the principle. Now here is the statute."
    },
    {
        "name": "freud",
        "voice_id": "JBFqnCBsd6RMkjVDRZzb",
        "stability": 0.6,
        "similarity_boost": 0.8,
        "text": "I am Sigmund Freud. What you think you believe is not what drives you. My role in this council is to expose hidden motivations, the fears beneath the arguments, the desires behind the positions. Before you insist on your reasons, let us examine your resistance."
    },
]


def generate_voice(sage, max_retries=3):
    """Generate a single sage voice clip."""
    output_path = OUTPUT_DIR / f"{sage['name']}.mp3"

    # Skip if already generated
    if output_path.exists() and output_path.stat().st_size > 0:
        print(f"  SKIP {sage['name']} (already exists: {output_path.stat().st_size} bytes)")
        return True

    for attempt in range(max_retries):
        try:
            print(f"  Generating {sage['name']} (attempt {attempt + 1})...")
            audio_generator = client.text_to_speech.convert(
                voice_id=sage["voice_id"],
                text=sage["text"],
                model_id="eleven_multilingual_v2",
                voice_settings={
                    "stability": sage["stability"],
                    "similarity_boost": sage["similarity_boost"],
                },
            )

            # Write audio chunks to file
            with open(output_path, "wb") as f:
                for chunk in audio_generator:
                    f.write(chunk)

            size = output_path.stat().st_size
            if size < 1000:
                print(f"  WARNING: {sage['name']} file suspiciously small ({size} bytes)")
                output_path.unlink()
                continue

            print(f"  OK {sage['name']} ({size:,} bytes)")
            return True

        except Exception as e:
            error_msg = str(e)
            print(f"  ERROR {sage['name']}: {error_msg}")
            if "429" in error_msg or "rate" in error_msg.lower():
                wait = 2 ** (attempt + 1)
                print(f"  Rate limited, waiting {wait}s...")
                time.sleep(wait)
            elif attempt < max_retries - 1:
                time.sleep(1)

    print(f"  FAILED {sage['name']} after {max_retries} attempts")
    return False


def main():
    print(f"Generating {len(SAGES)} sage voice clips...")
    print(f"Output: {OUTPUT_DIR.resolve()}\n")

    success = 0
    failed = 0
    for sage in SAGES:
        if generate_voice(sage):
            success += 1
        else:
            failed += 1
        # Brief pause between API calls
        time.sleep(0.5)

    print(f"\nDone: {success} succeeded, {failed} failed")
    if failed:
        print("Re-run the script to retry failed generations.")


if __name__ == "__main__":
    main()
```

- [ ] **Step 3: Run the generation script**

```bash
cd /home/jsagi/sanhedrin-deck && python3 generate_sage_voices.py
```

Expected: 9 MP3 files created in `audio/sages/`, each ~150-300KB.

- [ ] **Step 4: Verify all 9 files exist and are reasonable size**

```bash
ls -la audio/sages/
```

Expected: 9 `.mp3` files, each 50KB-500KB.

- [ ] **Step 5: Commit voice generation script and audio files**

```bash
git add generate_sage_voices.py audio/sages/
git commit -m "feat: Add ElevenLabs sage voice clips for 9 sages"
```

---

## Chunk 2: Slide 5 Card Redesign (HTML + CSS)

### Task 2: Add CSS for voice-enabled sage cards

**Files:**
- Modify: `index.html` (CSS section, around line 440-510)

- [ ] **Step 1: Add sage-card-voice CSS rules**

Insert after the existing `.sage-overlay .sage-mode-overlay` rule block (around line 505) in the `<style>` section:

```css
/* === SLIDE 5 VOICE CARDS === */
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

- [ ] **Step 2: Commit CSS changes**

```bash
git add index.html
git commit -m "style: Add CSS for Slide 5 voice-enabled sage cards"
```

### Task 3: Replace Slide 5 EN cards (6 -> 9 with overlays and play buttons)

**Files:**
- Modify: `index.html` (Slide 5 EN section, lines 908-951)

- [ ] **Step 1: Replace the EN card grid**

Replace the existing grid div (line 908, `<div style="display: grid; grid-template-columns: repeat(6, 1fr)...`) through the closing `</div>` of the grid (line 951) with the new 9-card grid. The grid changes from `repeat(6, 1fr)` to `repeat(9, 1fr)` and `max-width: 1100px` to `max-width: 1400px`.

The old content to replace starts at line 908:
```html
      <div style="display: grid; grid-template-columns: repeat(6, 1fr); gap: 16px; max-width: 1100px; width: 100%;" class="reveal r3">
```
through to the closing `</div>` just before the `<p class="body-sm reveal r4"` line (line 952).

New content (9 cards with overlays and play buttons):
```html
      <div style="display: grid; grid-template-columns: repeat(9, 1fr); gap: 12px; max-width: 1400px; width: 100%;" class="reveal r3">
        <div class="sage-card sage-card-voice" data-sage="abraham" data-audio="audio/sages/abraham.mp3">
          <img class="sage-cover" src="https://static1.squarespace.com/static/57abd1268419c28d7981b5cd/t/6788010d96ece2161d573ed9/1736966413206/JL_NewReleases_Abraham_Facebook+%28002%29.jpg?format=500w" alt="Abraham" loading="lazy">
          <div class="sage-info">
            <div class="sage-name">Abraham</div>
            <div class="sage-mode-badge">#1 DISRUPTION</div>
          </div>
          <div class="sage-overlay">
            <div class="sage-role-title">The Idol-Smasher</div>
            <div class="sage-role-desc">Challenges every inherited assumption. Forces the council to question what they take for granted.</div>
            <div class="sage-sig">"What if everything your fathers taught you is wrong?"</div>
            <button class="sage-play-btn" onclick="event.stopPropagation(); playSageVoice(this)" title="Hear this sage">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
            </button>
          </div>
        </div>
        <div class="sage-card sage-card-voice" data-sage="maimonides" data-audio="audio/sages/maimonides.mp3">
          <img class="sage-cover" src="https://static1.squarespace.com/static/57abd1268419c28d7981b5cd/5851a83fb8a79b5cd9df2528/63eb944ebbaede1fe2a511f8/1770325601718/Maimonides.jpg?format=500w" alt="Maimonides" loading="lazy">
          <div class="sage-info">
            <div class="sage-name">Maimonides</div>
            <div class="sage-mode-badge">#10 SOLUTION</div>
          </div>
          <div class="sage-overlay">
            <div class="sage-role-title">The Supreme Systematizer</div>
            <div class="sage-role-desc">Unified Aristotelian logic with Torah law. Brings rigorous classification to every debate.</div>
            <div class="sage-sig">"There are exactly four categories, and here they are"</div>
            <button class="sage-play-btn" onclick="event.stopPropagation(); playSageVoice(this)" title="Hear this sage">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
            </button>
          </div>
        </div>
        <div class="sage-card sage-card-voice" data-sage="herzl" data-audio="audio/sages/herzl.mp3">
          <img class="sage-cover" src="https://static1.squarespace.com/static/57abd1268419c28d7981b5cd/t/5e3c33a90a26f25c6a297761/1581003693653/Herzl+Facebook.jpg?format=500w" alt="Herzl" loading="lazy">
          <div class="sage-info">
            <div class="sage-name">Herzl</div>
            <div class="sage-mode-badge">#7 GENERATIVE</div>
          </div>
          <div class="sage-overlay">
            <div class="sage-role-title">The Visionary</div>
            <div class="sage-role-desc">Generates radical new possibilities from nothing. Produces options when the council reaches deadlock.</div>
            <div class="sage-sig">"If you will it, it is no dream"</div>
            <button class="sage-play-btn" onclick="event.stopPropagation(); playSageVoice(this)" title="Hear this sage">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
            </button>
          </div>
        </div>
        <div class="sage-card sage-card-voice" data-sage="golda-meir" data-audio="audio/sages/golda-meir.mp3">
          <img class="sage-cover" src="https://static1.squarespace.com/static/57abd1268419c28d7981b5cd/t/64b01293bcde250ff58dca7e/1689260695538/JL_NewReleases_Meir_Facebook.jpg?format=500w" alt="Golda Meir" loading="lazy">
          <div class="sage-info">
            <div class="sage-name">Golda Meir</div>
            <div class="sage-mode-badge">#13 COLLECTIVE</div>
          </div>
          <div class="sage-overlay">
            <div class="sage-role-title">The Mother of the Nation</div>
            <div class="sage-role-desc">Speaks for collective fate, not personal interest. Frames every dilemma: what does this mean for our people?</div>
            <div class="sage-sig">"We have no one else"</div>
            <button class="sage-play-btn" onclick="event.stopPropagation(); playSageVoice(this)" title="Hear this sage">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
            </button>
          </div>
        </div>
        <div class="sage-card sage-card-voice" data-sage="einstein" data-audio="audio/sages/einstein.mp3">
          <img class="sage-cover" src="https://static1.squarespace.com/static/57abd1268419c28d7981b5cd/5851a83fb8a79b5cd9df2528/58ac325c9de4bb7fca0ba46d/1770324502345/Einstein.jpg?format=500w" alt="Einstein" loading="lazy">
          <div class="sage-info">
            <div class="sage-name">Einstein</div>
            <div class="sage-mode-badge">#8 IMAGINATIVE</div>
          </div>
          <div class="sage-overlay">
            <div class="sage-role-title">The Thought Experimenter</div>
            <div class="sage-role-desc">Proposes radical hypotheses that reframe the entire discussion. Takes fixed assumptions and asks: what if they are wrong?</div>
            <div class="sage-sig">"Imagine everything you assume is wrong"</div>
            <button class="sage-play-btn" onclick="event.stopPropagation(); playSageVoice(this)" title="Hear this sage">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
            </button>
          </div>
        </div>
        <div class="sage-card sage-card-voice" data-sage="anne-frank" data-audio="audio/sages/anne-frank.mp3">
          <img class="sage-cover" src="https://static1.squarespace.com/static/57abd1268419c28d7981b5cd/t/676eca6cfc91ce6c667540e6/1735314028002/JL_Podcast_FBBanner_Anne+Frank+%28002%29.jpg?format=500w" alt="Anne Frank" loading="lazy">
          <div class="sage-info">
            <div class="sage-name">Anne Frank</div>
            <div class="sage-mode-badge">#3 NARRATIVE</div>
          </div>
          <div class="sage-overlay">
            <div class="sage-role-title">The Witness of the Ordinary</div>
            <div class="sage-role-desc">Reminds the council that grand principles are lived in small daily moments. Testifies from experience, not theory.</div>
            <div class="sage-sig">"I still believe people are good. But let me tell you what I saw."</div>
            <button class="sage-play-btn" onclick="event.stopPropagation(); playSageVoice(this)" title="Hear this sage">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
            </button>
          </div>
        </div>
        <div class="sage-card sage-card-voice" data-sage="houdini" data-audio="audio/sages/houdini.mp3">
          <img class="sage-cover" src="https://static1.squarespace.com/static/57abd1268419c28d7981b5cd/t/5e54182e7bcf434aa9c1d312/1582569521607/JL_NewReleases_Houdini_Facebook.jpg?format=500w" alt="Houdini" loading="lazy">
          <div class="sage-info">
            <div class="sage-name">Houdini</div>
            <div class="sage-mode-badge">#1 DISRUPTION</div>
          </div>
          <div class="sage-overlay">
            <div class="sage-role-title">The Escape Artist</div>
            <div class="sage-role-desc">No cage can hold a determined mind. Every constraint is an invitation to find the hidden exit.</div>
            <div class="sage-sig">"What the eyes see and the ears hear, the mind believes"</div>
            <button class="sage-play-btn" onclick="event.stopPropagation(); playSageVoice(this)" title="Hear this sage">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
            </button>
          </div>
        </div>
        <div class="sage-card sage-card-voice" data-sage="moses" data-audio="audio/sages/moses.mp3">
          <img class="sage-cover" src="https://static1.squarespace.com/static/57abd1268419c28d7981b5cd/5851a83fb8a79b5cd9df2528/58584185e58c623d6c961256/1770319874617/Moses.jpg?format=500w" alt="Moses" loading="lazy">
          <div class="sage-info">
            <div class="sage-name">Moses</div>
            <div class="sage-mode-badge">#10 SOLUTION</div>
          </div>
          <div class="sage-overlay">
            <div class="sage-role-title">The Lawgiver</div>
            <div class="sage-role-desc">Translates values into actionable statutes. Cuts through abstraction to ask: what is the law?</div>
            <div class="sage-sig">"That is the principle; now here is the statute"</div>
            <button class="sage-play-btn" onclick="event.stopPropagation(); playSageVoice(this)" title="Hear this sage">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
            </button>
          </div>
        </div>
        <div class="sage-card sage-card-voice" data-sage="freud" data-audio="audio/sages/freud.mp3">
          <img class="sage-cover" src="https://static1.squarespace.com/static/57abd1268419c28d7981b5cd/5851a83fb8a79b5cd9df2528/5852c1eef7e0ab7cf8248cd3/1770911668899/Freud.jpg?format=500w" alt="Sigmund Freud" loading="lazy">
          <div class="sage-info">
            <div class="sage-name">Sigmund Freud</div>
            <div class="sage-mode-badge">#5 INTERPRETIVE</div>
          </div>
          <div class="sage-overlay">
            <div class="sage-role-title">The Unconscious Explorer</div>
            <div class="sage-role-desc">What you think you believe is not what drives you. Forces the council to examine their hidden motivations.</div>
            <div class="sage-sig">"Before you insist on your reasons, let us examine your resistance"</div>
            <button class="sage-play-btn" onclick="event.stopPropagation(); playSageVoice(this)" title="Hear this sage">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
            </button>
          </div>
        </div>
      </div>
```

- [ ] **Step 2: Commit EN card changes**

```bash
git add index.html
git commit -m "feat: Expand Slide 5 EN to 9 sage cards with overlays and play buttons"
```

### Task 4: Replace Slide 5 HE cards (6 -> 9 with overlays and play buttons)

**Files:**
- Modify: `index.html` (Slide 5 HE section, lines 964-1006)

- [ ] **Step 1: Replace the HE card grid**

Replace the existing HE grid div (line 964, `<div style="display: grid; grid-template-columns: repeat(6, 1fr)...`) through its closing `</div>` (line 1007) with:

```html
      <div style="display: grid; grid-template-columns: repeat(9, 1fr); gap: 12px; max-width: 1400px; width: 100%;" class="reveal r3">
        <div class="sage-card sage-card-voice" data-sage="abraham" data-audio="audio/sages/abraham.mp3">
          <img class="sage-cover" src="https://static1.squarespace.com/static/57abd1268419c28d7981b5cd/t/6788010d96ece2161d573ed9/1736966413206/JL_NewReleases_Abraham_Facebook+%28002%29.jpg?format=500w" alt="Abraham" loading="lazy">
          <div class="sage-info">
            <div class="sage-name">אברהם</div>
            <div class="sage-mode-badge">#1 חשיבה מפריעה</div>
          </div>
          <div class="sage-overlay">
            <div class="sage-role-title">שובר האלילים</div>
            <div class="sage-role-desc">מאתגר כל הנחה מקובלת. מכריח את המועצה לשאול מה הם מקבלים כמובן מאליו.</div>
            <div class="sage-sig">"ומה אם כל מה שאבותיכם לימדו אתכם שגוי?"</div>
            <button class="sage-play-btn" onclick="event.stopPropagation(); playSageVoice(this)" title="שמעו את החכם">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
            </button>
          </div>
        </div>
        <div class="sage-card sage-card-voice" data-sage="maimonides" data-audio="audio/sages/maimonides.mp3">
          <img class="sage-cover" src="https://static1.squarespace.com/static/57abd1268419c28d7981b5cd/5851a83fb8a79b5cd9df2528/63eb944ebbaede1fe2a511f8/1770325601718/Maimonides.jpg?format=500w" alt="Maimonides" loading="lazy">
          <div class="sage-info">
            <div class="sage-name">רמב"ם</div>
            <div class="sage-mode-badge">#10 חשיבה מוכוונת פתרון</div>
          </div>
          <div class="sage-overlay">
            <div class="sage-role-title">המסדר העליון</div>
            <div class="sage-role-desc">איחד לוגיקה אריסטוטלית עם הלכה. מביא סיווג קפדני לכל דיון.</div>
            <div class="sage-sig">"יש בדיוק ארבע קטגוריות, והנה הן"</div>
            <button class="sage-play-btn" onclick="event.stopPropagation(); playSageVoice(this)" title="שמעו את החכם">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
            </button>
          </div>
        </div>
        <div class="sage-card sage-card-voice" data-sage="herzl" data-audio="audio/sages/herzl.mp3">
          <img class="sage-cover" src="https://static1.squarespace.com/static/57abd1268419c28d7981b5cd/t/5e3c33a90a26f25c6a297761/1581003693653/Herzl+Facebook.jpg?format=500w" alt="Herzl" loading="lazy">
          <div class="sage-info">
            <div class="sage-name">הרצל</div>
            <div class="sage-mode-badge">#7 חשיבה גנרטיבית</div>
          </div>
          <div class="sage-overlay">
            <div class="sage-role-title">החוזה</div>
            <div class="sage-role-desc">מייצר אפשרויות רדיקליות מאין. מפיק פתרונות כשהמועצה מגיעה למבוי סתום.</div>
            <div class="sage-sig">"אם תרצו, אין זו אגדה"</div>
            <button class="sage-play-btn" onclick="event.stopPropagation(); playSageVoice(this)" title="שמעו את החכם">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
            </button>
          </div>
        </div>
        <div class="sage-card sage-card-voice" data-sage="golda-meir" data-audio="audio/sages/golda-meir.mp3">
          <img class="sage-cover" src="https://static1.squarespace.com/static/57abd1268419c28d7981b5cd/t/64b01293bcde250ff58dca7e/1689260695538/JL_NewReleases_Meir_Facebook.jpg?format=500w" alt="Golda Meir" loading="lazy">
          <div class="sage-info">
            <div class="sage-name">גולדה מאיר</div>
            <div class="sage-mode-badge">#13 חשיבה קולקטיבית</div>
          </div>
          <div class="sage-overlay">
            <div class="sage-role-title">אם האומה</div>
            <div class="sage-role-desc">מדברת בשם הגורל הקולקטיבי. בכל דילמה שואלת: מה זה אומר לעם שלנו?</div>
            <div class="sage-sig">"אין לנו אף אחד אחר"</div>
            <button class="sage-play-btn" onclick="event.stopPropagation(); playSageVoice(this)" title="שמעו את החכם">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
            </button>
          </div>
        </div>
        <div class="sage-card sage-card-voice" data-sage="einstein" data-audio="audio/sages/einstein.mp3">
          <img class="sage-cover" src="https://static1.squarespace.com/static/57abd1268419c28d7981b5cd/5851a83fb8a79b5cd9df2528/58ac325c9de4bb7fca0ba46d/1770324502345/Einstein.jpg?format=500w" alt="Einstein" loading="lazy">
          <div class="sage-info">
            <div class="sage-name">איינשטיין</div>
            <div class="sage-mode-badge">#8 חשיבה דמיונית</div>
          </div>
          <div class="sage-overlay">
            <div class="sage-role-title">ניסויי המחשבה</div>
            <div class="sage-role-desc">מציע השערות רדיקליות שממסגרות מחדש את כל הדיון. לוקח הנחות קבועות ושואל: ומה אם הן שגויות?</div>
            <div class="sage-sig">"דמיינו שכל מה שאתם מניחים שגוי"</div>
            <button class="sage-play-btn" onclick="event.stopPropagation(); playSageVoice(this)" title="שמעו את החכם">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
            </button>
          </div>
        </div>
        <div class="sage-card sage-card-voice" data-sage="anne-frank" data-audio="audio/sages/anne-frank.mp3">
          <img class="sage-cover" src="https://static1.squarespace.com/static/57abd1268419c28d7981b5cd/t/676eca6cfc91ce6c667540e6/1735314028002/JL_Podcast_FBBanner_Anne+Frank+%28002%29.jpg?format=500w" alt="Anne Frank" loading="lazy">
          <div class="sage-info">
            <div class="sage-name">אנה פרנק</div>
            <div class="sage-mode-badge">#3 חשיבה נרטיבית</div>
          </div>
          <div class="sage-overlay">
            <div class="sage-role-title">העדה של הרגיל</div>
            <div class="sage-role-desc">מזכירה למועצה שעקרונות גדולים חיים ברגעים קטנים יומיומיים. מעידה מניסיון, לא מתיאוריה.</div>
            <div class="sage-sig">"אני עדיין מאמינה שאנשים טובים. אבל תנו לי לספר מה ראיתי."</div>
            <button class="sage-play-btn" onclick="event.stopPropagation(); playSageVoice(this)" title="שמעו את החכם">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
            </button>
          </div>
        </div>
        <div class="sage-card sage-card-voice" data-sage="houdini" data-audio="audio/sages/houdini.mp3">
          <img class="sage-cover" src="https://static1.squarespace.com/static/57abd1268419c28d7981b5cd/t/5e54182e7bcf434aa9c1d312/1582569521607/JL_NewReleases_Houdini_Facebook.jpg?format=500w" alt="Houdini" loading="lazy">
          <div class="sage-info">
            <div class="sage-name">הודיני</div>
            <div class="sage-mode-badge">#1 חשיבה מפריעה</div>
          </div>
          <div class="sage-overlay">
            <div class="sage-role-title">אמן הבריחה</div>
            <div class="sage-role-desc">שום כלוב לא יכול להחזיק מוח נחוש. כל אילוץ הוא הזמנה למצוא את היציאה הנסתרת.</div>
            <div class="sage-sig">"מה שהעיניים רואות והאוזניים שומעות, המוח מאמין"</div>
            <button class="sage-play-btn" onclick="event.stopPropagation(); playSageVoice(this)" title="שמעו את החכם">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
            </button>
          </div>
        </div>
        <div class="sage-card sage-card-voice" data-sage="moses" data-audio="audio/sages/moses.mp3">
          <img class="sage-cover" src="https://static1.squarespace.com/static/57abd1268419c28d7981b5cd/5851a83fb8a79b5cd9df2528/58584185e58c623d6c961256/1770319874617/Moses.jpg?format=500w" alt="Moses" loading="lazy">
          <div class="sage-info">
            <div class="sage-name">משה</div>
            <div class="sage-mode-badge">#10 חשיבה מוכוונת פתרון</div>
          </div>
          <div class="sage-overlay">
            <div class="sage-role-title">המחוקק</div>
            <div class="sage-role-desc">מתרגם ערכים לחוקים ברי ביצוע. חותך דרך הפשטות ושואל: מה הדין?</div>
            <div class="sage-sig">"זה העיקרון; עכשיו הנה החוק"</div>
            <button class="sage-play-btn" onclick="event.stopPropagation(); playSageVoice(this)" title="שמעו את החכם">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
            </button>
          </div>
        </div>
        <div class="sage-card sage-card-voice" data-sage="freud" data-audio="audio/sages/freud.mp3">
          <img class="sage-cover" src="https://static1.squarespace.com/static/57abd1268419c28d7981b5cd/5851a83fb8a79b5cd9df2528/5852c1eef7e0ab7cf8248cd3/1770911668899/Freud.jpg?format=500w" alt="Sigmund Freud" loading="lazy">
          <div class="sage-info">
            <div class="sage-name">זיגמונד פרויד</div>
            <div class="sage-mode-badge">#5 חשיבה פרשנית</div>
          </div>
          <div class="sage-overlay">
            <div class="sage-role-title">חוקר התת-מודע</div>
            <div class="sage-role-desc">מה שאתם חושבים שאתם מאמינים לא מה שמניע אתכם. מכריח את המועצה לבחון את המוטיבציות הנסתרות.</div>
            <div class="sage-sig">"לפני שתתעקשו על הסיבות שלכם, בואו נבחן את ההתנגדות"</div>
            <button class="sage-play-btn" onclick="event.stopPropagation(); playSageVoice(this)" title="שמעו את החכם">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
            </button>
          </div>
        </div>
      </div>
```

- [ ] **Step 2: Commit HE card changes**

```bash
git add index.html
git commit -m "feat: Expand Slide 5 HE to 9 sage cards with overlays and play buttons"
```

### Task 5: Add sage voice playback JavaScript

**Files:**
- Modify: `index.html` (JS section, insert before the `// === DELIBERATION NETWORK` block at line 3467)

- [ ] **Step 1: Add sage voice JS after the narration system (after line 3465)**

Insert this block between the narration system and the deliberation network:

```javascript
// === SAGE VOICE PLAYBACK ===
var sageAudio = null;
var isSagePlaying = false;
var activeSageCard = null;

function stopSageVoice() {
  if (sageAudio) {
    sageAudio.pause();
    sageAudio = null;
  }
  isSagePlaying = false;
  if (activeSageCard) {
    activeSageCard.classList.remove('playing');
    var btn = activeSageCard.querySelector('.sage-play-btn');
    if (btn) btn.classList.remove('playing');
    activeSageCard = null;
  }
}

function playSageVoice(btn) {
  var card = btn.closest('.sage-card-voice');
  var audioSrc = card.dataset.audio;

  // Stop any slide narration
  stopNarration();

  // Toggle off if same card
  if (activeSageCard === card && isSagePlaying) {
    stopSageVoice();
    return;
  }

  // Stop any other sage
  stopSageVoice();

  sageAudio = new Audio(audioSrc);
  isSagePlaying = true;
  activeSageCard = card;
  card.classList.add('playing');
  btn.classList.add('playing');

  sageAudio.play().then(function() {
    console.log('Sage voice playing: ' + card.dataset.sage);
  }).catch(function(err) {
    console.error('Sage audio failed:', err);
    stopSageVoice();
  });

  sageAudio.onended = function() {
    stopSageVoice();
  };
}
```

- [ ] **Step 2: Update showSlide to also stop sage audio**

In the `showSlide` function (line 3318), add `stopSageVoice();` right after `stopNarration();` (line 3320).

The modified lines should read:
```javascript
function showSlide(index) {
  if (index < 0 || index >= slides.length) return;
  stopNarration();
  stopSageVoice();
```

- [ ] **Step 3: Update playNarration to stop sage audio**

In the `playNarration` function (line 3433), add `stopSageVoice();` right after `stopNarration();` (line 3437).

The modified lines should read:
```javascript
function playNarration() {
  var slideIndex = current;
  var num = String(slideIndex + 1).padStart(2, '0');
  // Stop any existing
  stopNarration();
  stopSageVoice();
```

- [ ] **Step 4: Commit JS changes**

```bash
git add index.html
git commit -m "feat: Add sage voice playback JS with audio system integration"
```

---

## Chunk 3: Canvas Animations

### Task 6: Add Slide 6 Role-Based Architecture canvas animation

**Files:**
- Modify: `index.html` (Slide 6 HTML at ~line 1102, and JS section before `</script>`)

- [ ] **Step 1: Add canvas element to Slide 6 EN section**

In Slide 6 EN (line ~1104), add the canvas inside `.layout-statement` as the first child, before the `<p class="label reveal">`. The `.layout-statement` div needs `position: relative` added.

After `<div class="layout-statement" style="justify-content: flex-start; padding-top: 40px;">` add:
```html
      <canvas class="role-network" id="roleNetwork"></canvas>
```

And change the div's style to include `position: relative;`:
```html
    <div class="layout-statement" style="justify-content: flex-start; padding-top: 40px; position: relative;">
```

- [ ] **Step 2: Add canvas element to Slide 6 HE section**

Same pattern for the HE version. Find the corresponding `<div class="layout-statement"` in the `lang-he` section and add:
```html
      <canvas class="role-network" id="roleNetworkHe"></canvas>
```
And add `position: relative;` to that div's style too.

- [ ] **Step 3: Add role-network CSS**

Insert in the `<style>` section (after the sage-play-btn rules added in Task 2):

```css
/* === CANVAS ANIMATIONS === */
.role-network {
  position: absolute;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  opacity: 0.6;
}
.arena-network {
  position: absolute;
  inset: 0;
  z-index: 1;
  pointer-events: none;
  opacity: 0.5;
}
```

- [ ] **Step 4: Add role network animation JS**

Insert before `</script>` (before line 3583), after the slide watermark IIFE:

```javascript
// === ROLE NETWORK ANIMATION (Slide 6) ===
var slideAnimations = {};
(function() {
  var canvasIds = ['roleNetwork', 'roleNetworkHe'];
  canvasIds.forEach(function(id) {
    var canvas = document.getElementById(id);
    if (!canvas) return;
    var ctx = canvas.getContext('2d');
    var animId = null;
    var running = false;

    // 3 persona nodes (top) and 9 role nodes (below)
    var personas = [];
    var roles = [];
    var edges = [];
    var edgeMigrateTimer = 0;

    function resize() {
      canvas.width = canvas.offsetWidth;
      canvas.height = canvas.offsetHeight;
      initNodes();
    }

    function initNodes() {
      var w = canvas.width;
      var h = canvas.height;
      // 3 personas at top (proportional to 3 columns)
      personas = [
        { x: w * 0.167, y: h * 0.18, r: 6 },
        { x: w * 0.5, y: h * 0.18, r: 6 },
        { x: w * 0.833, y: h * 0.18, r: 6 }
      ];
      // 3 roles per persona column
      roles = [];
      for (var col = 0; col < 3; col++) {
        var cx = personas[col].x;
        for (var row = 0; row < 3; row++) {
          roles.push({ x: cx + (Math.random() - 0.5) * 30, y: h * (0.4 + row * 0.18), r: 3, col: col });
        }
      }
      // Initialize edges: each role connected to its column persona
      edges = [];
      for (var i = 0; i < roles.length; i++) {
        edges.push({ role: i, persona: roles[i].col, strength: 0.5 + Math.random() * 0.5, migrating: false, fromPersona: -1, progress: 1 });
      }
    }

    function draw() {
      if (!running) return;
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      var t = Date.now() * 0.001;

      // Migrate one edge every ~4 seconds
      if (t - edgeMigrateTimer > 4) {
        edgeMigrateTimer = t;
        var idx = Math.floor(Math.random() * edges.length);
        var newPersona = Math.floor(Math.random() * 3);
        if (newPersona !== edges[idx].persona) {
          edges[idx].fromPersona = edges[idx].persona;
          edges[idx].persona = newPersona;
          edges[idx].progress = 0;
          edges[idx].migrating = true;
        }
      }

      // Draw edges
      for (var i = 0; i < edges.length; i++) {
        var e = edges[i];
        var role = roles[e.role];
        var p = personas[e.persona];

        // Handle migration animation
        if (e.migrating && e.progress < 1) {
          e.progress = Math.min(e.progress + 0.02, 1);
          if (e.progress >= 1) e.migrating = false;
          var pOld = personas[e.fromPersona];
          var lerpX = pOld.x + (p.x - pOld.x) * e.progress;
          var lerpY = pOld.y + (p.y - pOld.y) * e.progress;
          // Fade old
          ctx.beginPath();
          ctx.moveTo(role.x, role.y);
          ctx.lineTo(lerpX, lerpY);
          ctx.strokeStyle = 'rgba(189,214,230,' + (e.strength * 0.4) + ')';
          ctx.lineWidth = 1.5;
          ctx.stroke();
        } else {
          var pulse = 0.2 + 0.2 * Math.sin(t * 1.2 + i);
          ctx.beginPath();
          ctx.moveTo(role.x, role.y);
          ctx.lineTo(p.x, p.y);
          ctx.strokeStyle = 'rgba(189,214,230,' + (e.strength * pulse + 0.1) + ')';
          ctx.lineWidth = 1;
          ctx.stroke();
        }
      }

      // Draw persona nodes
      for (var i = 0; i < personas.length; i++) {
        var p = personas[i];
        var glow = 0.5 + 0.3 * Math.sin(t * 1.5 + i * 2);
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(189,214,230,' + glow + ')';
        ctx.fill();
      }

      // Draw role nodes
      for (var i = 0; i < roles.length; i++) {
        var r = roles[i];
        var glow = 0.3 + 0.2 * Math.sin(t * 1.8 + i);
        ctx.beginPath();
        ctx.arc(r.x, r.y, r.r, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(189,214,230,' + glow + ')';
        ctx.fill();
      }

      animId = requestAnimationFrame(draw);
    }

    function start() {
      if (running) return;
      running = true;
      resize();
      edgeMigrateTimer = Date.now() * 0.001;
      draw();
    }

    function stop() {
      running = false;
      if (animId) { cancelAnimationFrame(animId); animId = null; }
    }

    window.addEventListener('resize', resize);

    // Register for slide lifecycle
    // Slide 6 is index 5 (0-based). Both EN and HE canvases activate on same slide.
    if (!slideAnimations[5]) slideAnimations[5] = [];
    slideAnimations[5].push({ start: start, stop: stop });
  });
})();
```

- [ ] **Step 5: Commit Slide 6 animation**

```bash
git add index.html
git commit -m "feat: Add dynamic role assignment canvas animation to Slide 6"
```

### Task 7: Add Slide 9 Physical Space canvas animation

**Files:**
- Modify: `index.html` (Slide 9 HTML at ~line 1385, and JS section)

- [ ] **Step 1: Add canvas element to Slide 9 EN section**

In Slide 9 EN (line ~1387), inside `.layout-hero`, insert after `<div class="hero-scrim"></div>` (line 1389):
```html
      <canvas class="arena-network" id="arenaNetwork"></canvas>
```

- [ ] **Step 2: Add canvas element to Slide 9 HE section**

In Slide 9 HE, inside `.layout-hero`, insert after `<div class="hero-scrim"></div>` (line 1406):
```html
      <canvas class="arena-network" id="arenaNetworkHe"></canvas>
```

- [ ] **Step 3: Add arena animation JS**

Insert after the role network IIFE, before `</script>`:

```javascript
// === ARENA ANIMATION (Slide 9 - Physical Space) ===
(function() {
  var canvasIds = ['arenaNetwork', 'arenaNetworkHe'];
  canvasIds.forEach(function(id) {
    var canvas = document.getElementById(id);
    if (!canvas) return;
    var ctx = canvas.getContext('2d');
    var animId = null;
    var running = false;
    var kiosks = [];
    var participants = [];
    var sparks = [];
    var hub = { x: 0, y: 0, baseR: 12 };

    function resize() {
      canvas.width = canvas.offsetWidth;
      canvas.height = canvas.offsetHeight;
      initArena();
    }

    function initArena() {
      var w = canvas.width;
      var h = canvas.height;
      var cx = w / 2;
      var cy = h / 2;
      var radius = Math.min(w, h) * 0.35;

      hub.x = cx;
      hub.y = cy;

      // 12 kiosks in a circle
      kiosks = [];
      for (var i = 0; i < 12; i++) {
        var angle = (i / 12) * Math.PI * 2 - Math.PI / 2;
        kiosks.push({
          x: cx + Math.cos(angle) * radius,
          y: cy + Math.sin(angle) * radius,
          r: 4
        });
      }

      // 25 participant dots drifting between kiosks and hub
      participants = [];
      for (var i = 0; i < 25; i++) {
        var target = Math.random() < 0.4 ? -1 : Math.floor(Math.random() * 12); // -1 = hub
        var src = Math.floor(Math.random() * 12);
        participants.push({
          x: kiosks[src].x + (Math.random() - 0.5) * 20,
          y: kiosks[src].y + (Math.random() - 0.5) * 20,
          target: target,
          speed: 0.3 + Math.random() * 0.5,
          phase: Math.random() * Math.PI * 2
        });
      }

      sparks = [];
    }

    function draw() {
      if (!running) return;
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      var t = Date.now() * 0.001;

      // Draw connection arcs between kiosks
      for (var i = 0; i < kiosks.length; i++) {
        var next = (i + 1) % kiosks.length;
        var alpha = 0.08 + 0.05 * Math.sin(t * 0.8 + i);
        ctx.beginPath();
        ctx.moveTo(kiosks[i].x, kiosks[i].y);
        ctx.lineTo(kiosks[next].x, kiosks[next].y);
        ctx.strokeStyle = 'rgba(189,214,230,' + alpha + ')';
        ctx.lineWidth = 0.5;
        ctx.stroke();
      }

      // Draw kiosk-to-hub lines
      for (var i = 0; i < kiosks.length; i++) {
        var alpha = 0.06 + 0.04 * Math.sin(t * 0.6 + i * 0.5);
        ctx.beginPath();
        ctx.moveTo(kiosks[i].x, kiosks[i].y);
        ctx.lineTo(hub.x, hub.y);
        ctx.strokeStyle = 'rgba(189,214,230,' + alpha + ')';
        ctx.lineWidth = 0.5;
        ctx.stroke();
      }

      // Central hub (pulsing)
      var hubR = hub.baseR + 4 * Math.sin(t * 1.2);
      var hubAlpha = 0.3 + 0.15 * Math.sin(t * 1.2);
      ctx.beginPath();
      ctx.arc(hub.x, hub.y, hubR, 0, Math.PI * 2);
      ctx.fillStyle = 'rgba(189,214,230,' + hubAlpha + ')';
      ctx.fill();
      // Inner glow
      ctx.beginPath();
      ctx.arc(hub.x, hub.y, hubR * 0.5, 0, Math.PI * 2);
      ctx.fillStyle = 'rgba(255,255,255,' + (hubAlpha * 0.6) + ')';
      ctx.fill();

      // Kiosk nodes
      for (var i = 0; i < kiosks.length; i++) {
        var k = kiosks[i];
        var pulse = 0.4 + 0.2 * Math.sin(t * 1.5 + i * 0.5);
        ctx.beginPath();
        ctx.arc(k.x, k.y, k.r, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(189,214,230,' + pulse + ')';
        ctx.fill();
      }

      // Move and draw participants
      for (var i = 0; i < participants.length; i++) {
        var p = participants[i];
        var tx, ty;
        if (p.target === -1) {
          tx = hub.x;
          ty = hub.y;
        } else {
          tx = kiosks[p.target].x;
          ty = kiosks[p.target].y;
        }

        var dx = tx - p.x;
        var dy = ty - p.y;
        var dist = Math.sqrt(dx * dx + dy * dy);

        if (dist < 8) {
          // Arrived, pick new target
          if (p.target === -1) {
            p.target = Math.floor(Math.random() * 12);
          } else {
            p.target = Math.random() < 0.3 ? -1 : Math.floor(Math.random() * 12);
          }
        } else {
          p.x += (dx / dist) * p.speed;
          p.y += (dy / dist) * p.speed;
        }

        var alpha = 0.3 + 0.2 * Math.sin(t * 2 + p.phase);
        ctx.beginPath();
        ctx.arc(p.x, p.y, 1.5, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(255,255,255,' + alpha + ')';
        ctx.fill();
      }

      // Spawn occasional spark
      if (Math.random() < 0.005 && sparks.length < 3) {
        var from = Math.floor(Math.random() * 12);
        var to = (from + Math.floor(Math.random() * 5) + 3) % 12;
        sparks.push({
          fromX: kiosks[from].x, fromY: kiosks[from].y,
          toX: kiosks[to].x, toY: kiosks[to].y,
          progress: 0, speed: 0.03
        });
      }

      // Draw and advance sparks
      for (var i = sparks.length - 1; i >= 0; i--) {
        var s = sparks[i];
        s.progress += s.speed;
        if (s.progress >= 1) {
          sparks.splice(i, 1);
          continue;
        }
        var sx = s.fromX + (s.toX - s.fromX) * s.progress;
        var sy = s.fromY + (s.toY - s.fromY) * s.progress;
        ctx.beginPath();
        ctx.arc(sx, sy, 3, 0, Math.PI * 2);
        ctx.fillStyle = 'rgba(255,255,255,' + (0.8 - s.progress * 0.6) + ')';
        ctx.fill();
      }

      animId = requestAnimationFrame(draw);
    }

    function start() {
      if (running) return;
      running = true;
      resize();
      draw();
    }

    function stop() {
      running = false;
      if (animId) { cancelAnimationFrame(animId); animId = null; }
    }

    window.addEventListener('resize', resize);

    // Slide 9 is index 8 (0-based)
    if (!slideAnimations[8]) slideAnimations[8] = [];
    slideAnimations[8].push({ start: start, stop: stop });
  });
})();
```

- [ ] **Step 4: Commit Slide 9 animation**

```bash
git add index.html
git commit -m "feat: Add living arena canvas animation to Slide 9 (Physical Space)"
```

### Task 8: Wire animation lifecycle into showSlide

**Files:**
- Modify: `index.html` (the showSlide override at ~line 3569)

- [ ] **Step 1: Update the showSlide override**

The current override (line 3569-3580) wraps showSlide for counter animation. Update it to also manage canvas animation lifecycle:

Replace the existing override block:
```javascript
var _origShowSlide = showSlide;
showSlide = function(index) {
  _origShowSlide(index);
  // Reset counters on other slides
  document.querySelectorAll('[data-count]').forEach(function(el) {
    if (!el.closest('.slide.active')) {
      delete el.dataset.counted;
      el.textContent = '0';
    }
  });
  setTimeout(animateCounters, 400);
};
```

With:
```javascript
var _origShowSlide = showSlide;
showSlide = function(index) {
  // Stop all canvas animations
  Object.keys(slideAnimations).forEach(function(key) {
    slideAnimations[key].forEach(function(anim) { anim.stop(); });
  });

  _origShowSlide(index);

  // Start animations for current slide
  if (slideAnimations[index]) {
    slideAnimations[index].forEach(function(anim) { anim.start(); });
  }

  // Reset counters on other slides
  document.querySelectorAll('[data-count]').forEach(function(el) {
    if (!el.closest('.slide.active')) {
      delete el.dataset.counted;
      el.textContent = '0';
    }
  });
  setTimeout(animateCounters, 400);
};
```

- [ ] **Step 2: Commit lifecycle wiring**

```bash
git add index.html
git commit -m "feat: Wire canvas animation lifecycle into slide transitions"
```

---

## Chunk 4: Final Integration + Deploy

### Task 9: Update STATE.md with Session 13 changes

**Files:**
- Modify: `STATE.md`

- [ ] **Step 1: Add Session 13 entry to STATE.md**

Add Session 13 to the session history and update the "What To Do Next" section. Add entry after Session 12 in the changelog and update the session table.

- [ ] **Step 2: Commit STATE.md**

```bash
git add STATE.md
git commit -m "docs: Update STATE.md with Session 13 changes"
```

### Task 10: Push to master for deploy

- [ ] **Step 1: Push to master**

```bash
git push origin master
```

Expected: Render auto-deploys. Verify at https://sanhedrin-deck.onrender.com

- [ ] **Step 2: Verify the deploy**

Check that:
1. Slide 5 shows 9 sage cards
2. Hovering a card shows the overlay with play button
3. Clicking play button plays the sage voice
4. Slide 6 has the role network animation
5. Slide 9 has the arena animation
6. Animations start/stop on slide transitions
7. Audio stops when changing slides
