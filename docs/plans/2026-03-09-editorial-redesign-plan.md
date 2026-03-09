# Editorial/Magazine Redesign - Implementation Plan

> **For Claude:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task.

**Goal:** Transform the Sanhedrin deck from a dry, dark corporate presentation into an editorial/magazine-style experience with light backgrounds, bold typography, full-bleed photography, and generous whitespace.

**Architecture:** Single-file HTML rewrite. Replace entire `<style>` block with new editorial design system. Restructure each `<section class="slide">` to use new layout classes (hero-full, editorial-split, statement). Restyle nav bar for light theme. Then generate new editorial images via nanobanana MCP tool.

**Tech Stack:** HTML/CSS/JS (single file), nanobanana MCP (image generation), Montserrat + JetBrains Mono (Google Fonts)

---

## Task 1: Replace CSS Design System

**Files:**
- Modify: `index.html` lines 9-341 (entire `<style>` block)

**Step 1: Replace the CSS variables and base styles**

Replace everything from `<style>` through the closing `</style>` with the new editorial design system. Key changes:

```css
/* NEW DESIGN SYSTEM - Editorial/Magazine */
:root {
  --bg: #F5F2EB;
  --bg-surface: #FFFFFF;
  --bg-nav: rgba(245,242,235,0.96);
  --navy: #003057;
  --navy-light: #004680;
  --blue: #BDD6E6;
  --blue-dim: rgba(189,214,230,0.3);
  --taupe: #776E64;
  --taupe-light: #9a9189;
  --text: #1A1A1A;
  --text-sub: #4A4A4A;
  --text-dim: #8A8A8A;
  --font-d: 'Montserrat', system-ui, sans-serif;
  --font-m: 'JetBrains Mono', monospace;
  --card-bg: #FFFFFF;
  --card-border: rgba(0,48,87,0.08);
  --card-shadow: 0 2px 12px rgba(0,0,0,0.06);
  --card-hover-shadow: 0 4px 20px rgba(0,0,0,0.1);
}
```

New layout classes:
```css
/* Hero full-bleed: image covers viewport, text overlaid */
.layout-hero {
  display: flex; flex-direction: column; justify-content: flex-end;
  padding: 0; position: relative;
}
.layout-hero .hero-bg {
  position: absolute; inset: 0;
  object-fit: cover; width: 100%; height: 100%;
}
.layout-hero .hero-scrim {
  position: absolute; inset: 0;
  background: linear-gradient(to top, rgba(0,48,87,0.85) 0%, rgba(0,48,87,0.4) 40%, transparent 70%);
}
.layout-hero .hero-content {
  position: relative; z-index: 2;
  padding: 0 80px 90px;
  color: #fff;
}

/* Editorial split: image bleeds one side, text padded other */
.layout-split {
  display: grid; grid-template-columns: 1fr 1fr; gap: 0;
  height: 100%; align-items: stretch;
}
.layout-split.img-right { grid-template-columns: 45% 55%; }
.layout-split.img-left { grid-template-columns: 55% 45%; }
.layout-split .split-text {
  display: flex; flex-direction: column; justify-content: center;
  padding: 60px 64px 72px;
}
.layout-split .split-img {
  overflow: hidden;
}
.layout-split .split-img img {
  width: 100%; height: 100%; object-fit: cover;
}

/* Statement: centered typography, no image */
.layout-statement {
  display: flex; flex-direction: column; align-items: center;
  justify-content: center; text-align: center;
  padding: 60px 80px 72px;
}
```

New typography:
```css
h1 { font-family: var(--font-d); font-weight: 800; font-size: 88px; line-height: 1.02; letter-spacing: -2px; color: var(--navy); }
h2 { font-family: var(--font-d); font-weight: 700; font-size: 60px; line-height: 1.06; letter-spacing: -1px; color: var(--navy); margin-bottom: 24px; }
.label { font-family: var(--font-m); font-size: 13px; letter-spacing: 4px; text-transform: uppercase; color: var(--taupe); margin-bottom: 16px; }
.tagline { font-family: var(--font-d); font-weight: 500; font-size: 32px; color: var(--text-sub); line-height: 1.3; }
.body-text { font-size: 24px; line-height: 1.65; color: var(--text-sub); }
.body-sm { font-size: 20px; line-height: 1.55; color: var(--text-dim); margin-top: 16px; }
.pull-quote { font-family: var(--font-d); font-weight: 300; font-style: italic; font-size: 38px; color: var(--navy); line-height: 1.35; }
```

New card styles:
```css
.card {
  background: var(--card-bg); border: 1px solid var(--card-border);
  box-shadow: var(--card-shadow); border-radius: 12px; padding: 28px 32px;
  transition: box-shadow 0.2s;
}
.card:hover { box-shadow: var(--card-hover-shadow); }
```

Updated nav bar (light theme):
```css
.nav-bar {
  background: var(--bg-nav); backdrop-filter: blur(14px);
  border-top: 1px solid rgba(0,48,87,0.08);
}
.slide-counter { color: var(--navy); }
.act-label { color: var(--taupe); }
.nav-btn {
  background: rgba(0,48,87,0.04); border: 1px solid rgba(0,48,87,0.12);
  color: var(--navy);
}
.nav-btn:hover { background: rgba(0,48,87,0.1); border-color: var(--navy); }
```

Remove the dark/light theme toggle entirely (we're editorial light only).

**Step 2: Verify the page loads without errors**

Open index.html in browser, confirm no broken styles.

**Step 3: Commit**

```bash
git add index.html
git commit -m "refactor: replace dark corporate CSS with editorial/magazine design system"
```

---

## Task 2: Restructure Slide 1 (Title/Hero)

**Files:**
- Modify: `index.html` - slide 1 section

**Step 1: Replace slide 1 HTML**

From:
```html
<section class="slide active" data-act="ACT 1: THE HOOK">
  <div class="en-content centered">
    ...centered layout with small image...
  </div>
</section>
```

To:
```html
<section class="slide active" data-act="ACT 1: THE HOOK">
  <div class="layout-hero">
    <img src="slides/slide-01/hero.png" alt="" class="hero-bg">
    <div class="hero-scrim"></div>
    <div class="hero-content">
      <img src="assets/logos/motj-logo-horizontal-white.svg" alt="MOTJ" style="height: 40px; margin-bottom: 32px;" class="reveal">
      <h1 class="reveal r1" style="color: #fff; font-size: 80px;">The Sanhedrin<br>Educational Experience</h1>
      <p class="tagline reveal r2" style="color: rgba(255,255,255,0.85); margin-top: 16px;">Disagree Better. Discover Together.</p>
      <p class="reveal r3" style="font-size: 22px; color: rgba(255,255,255,0.65); margin-top: 12px; font-style: italic;">What would history's greatest minds say about today's dilemmas?</p>
    </div>
  </div>
</section>
```

**Step 2: Verify slide 1 renders with full-bleed image and text overlay**

**Step 3: Commit**

```bash
git add index.html
git commit -m "feat: slide 1 hero full-bleed layout with text overlay"
```

---

## Task 3: Restructure Slides 2-3 (Problem + Cognitive Twist)

**Files:**
- Modify: `index.html` - slides 2 and 3

**Step 1: Rebuild slide 2 as editorial split (image right)**

```html
<section class="slide" data-act="ACT 1: THE HOOK">
  <div class="layout-split img-right">
    <div class="split-text">
      <p class="label reveal">The Urgency</p>
      <h2 class="reveal r1">Discourse<br>is Broken</h2>
      <p class="body-text reveal r2">We live in a polarized society where young people literally walk out of rooms when exposed to opposing views. "I disagree with you" has become synonymous with tribal identity defense.</p>
      <p class="body-text reveal r3" style="margin-top: 20px;">Proper civic discourse cannot be taught via passive history lectures; it is a "muscle" requiring emotional strength training to sit with discomfort.</p>
      <div class="card reveal r4" style="margin-top: 24px; border-left: 4px solid var(--navy);">
        <p style="font-size: 20px; color: var(--text); font-weight: 600;">The Gap: Currently, there is no "civic discourse simulator" to train society on how to navigate complex, emotionally charged issues.</p>
      </div>
    </div>
    <div class="split-img">
      <img src="slides/slide-02/hero.png" alt="Polarization">
    </div>
  </div>
</section>
```

**Step 2: Rebuild slide 3 as editorial split (image left)**

```html
<section class="slide" data-act="ACT 1: THE HOOK">
  <div class="layout-split img-left">
    <div class="split-img">
      <img src="slides/slide-03/hero.png" alt="Puzzle metaphor">
    </div>
    <div class="split-text">
      <p class="label reveal">The Cognitive Twist</p>
      <h2 class="reveal r1">Dispute as a<br>Dynamic Puzzle</h2>
      <p class="body-text reveal r2">We are reframing the concept of a dispute. It is no longer a battle to be won, but a collaborative investigation, a Sherlock Holmes-style inquiry.</p>
      <ul class="bullets reveal r3" style="margin-top: 20px;">
        <li>Participants uncover hidden "puzzle pieces" (arguments, facts, agreements) to see the full picture.</li>
        <li>Adding depth earns pieces; demagoguery or personal attacks cause pieces to blur or be lost.</li>
        <li>The ultimate goal is shared truth-seeking: <em>L'Shem Shamayim</em> (for the sake of heaven).</li>
      </ul>
    </div>
  </div>
</section>
```

**Step 3: Verify both slides render correctly with edge-bleed images**

**Step 4: Commit**

```bash
git add index.html
git commit -m "feat: slides 2-3 editorial split layouts with full-bleed images"
```

---

## Task 4: Restructure Slide 4 (Value Prop - Statement)

**Files:**
- Modify: `index.html` - slide 4

**Step 1: Rebuild as bold statement slide**

```html
<section class="slide" data-act="ACT 1: THE HOOK">
  <div class="layout-statement">
    <p class="label reveal">Key Value Proposition</p>
    <h2 class="reveal r1" style="font-size: 72px; max-width: 900px;">"Learn to argue better<br>in 30 minutes."</h2>
    <p class="tagline reveal r2" style="margin-top: 8px;">Without needing to agree.</p>
    <p class="body-text reveal r3" style="text-align: center; margin-top: 28px; max-width: 800px;">An AI-powered immersive space where visitors engage with 71 historical Jewish figures in real-time deliberation.</p>
    <div style="display: flex; gap: 24px; margin-top: 40px;" class="reveal r4">
      <div style="background: var(--navy); color: #fff; padding: 28px 40px; border-radius: 12px; min-width: 200px;">
        <div style="font-family: var(--font-m); font-size: 13px; letter-spacing: 2px; opacity: 0.6;">INPUT</div>
        <p style="font-size: 20px; margin-top: 8px; font-weight: 500;">Human Visitor<br>Inputs Dilemma</p>
      </div>
      <div style="background: var(--navy); color: #fff; padding: 28px 40px; border-radius: 12px; min-width: 200px;">
        <div style="font-family: var(--font-m); font-size: 13px; letter-spacing: 2px; opacity: 0.6;">ENGINE</div>
        <p style="font-size: 20px; margin-top: 8px; font-weight: 500;">AI Characters &<br>Humans Deliberate</p>
      </div>
      <div style="background: var(--navy); color: #fff; padding: 28px 40px; border-radius: 12px; min-width: 200px;">
        <div style="font-family: var(--font-m); font-size: 13px; letter-spacing: 2px; opacity: 0.6;">OUTPUT</div>
        <p style="font-size: 20px; margin-top: 8px; font-weight: 500;">Expanded Thinking &<br>New Perspectives</p>
      </div>
    </div>
  </div>
</section>
```

**Step 2: Verify the navy pillar blocks render prominently**

**Step 3: Commit**

```bash
git add index.html
git commit -m "feat: slide 4 statement layout with bold navy pillar blocks"
```

---

## Task 5: Restructure Slides 5-9 (ACT 2: The Experience)

**Files:**
- Modify: `index.html` - slides 5 through 9

**Step 1: Rebuild slide 5 (Visitor Journey) as statement + large cards**

Replace the cramped steps-grid with large 2x3 card grid:
```html
<section class="slide" data-act="ACT 2: THE EXPERIENCE">
  <div class="layout-statement" style="justify-content: flex-start; padding-top: 48px;">
    <p class="label reveal">The 25-Minute Loop</p>
    <h2 class="reveal r1">The Visitor Journey</h2>
    <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 32px; width: 100%; max-width: 1100px;" class="reveal r2">
      <!-- 6 cards with large step numbers, each ~180px tall -->
      <div class="card">
        <span style="font-family: var(--font-m); font-size: 36px; font-weight: 700; color: var(--blue);">01</span>
        <div style="font-size: 22px; font-weight: 700; color: var(--text); margin-top: 8px;">Input Dilemma</div>
        <div style="font-size: 18px; color: var(--text-sub); margin-top: 8px; line-height: 1.4;">Up to 12 visitors select a dilemma and set their initial confidence level via touchscreens.</div>
      </div>
      <!-- repeat for steps 02-06 with same structure -->
      <div class="card">
        <span style="font-family: var(--font-m); font-size: 36px; font-weight: 700; color: var(--blue);">02</span>
        <div style="font-size: 22px; font-weight: 700; color: var(--text); margin-top: 8px;">Facilitator Opens</div>
        <div style="font-size: 18px; color: var(--text-sub); margin-top: 8px; line-height: 1.4;">A human Game Master sets the stage. Human charisma is non-negotiable for live orchestration.</div>
      </div>
      <div class="card">
        <span style="font-family: var(--font-m); font-size: 36px; font-weight: 700; color: var(--blue);">03</span>
        <div style="font-size: 22px; font-weight: 700; color: var(--text); margin-top: 8px;">Sages Assigned</div>
        <div style="font-size: 18px; color: var(--text-sub); margin-top: 8px; line-height: 1.4;">The "Wheel of Sages" dynamically assigns AI historical figures to join the human teams.</div>
      </div>
      <div class="card">
        <span style="font-family: var(--font-m); font-size: 36px; font-weight: 700; color: var(--blue);">04</span>
        <div style="font-size: 22px; font-weight: 700; color: var(--text); margin-top: 8px;">Deliberate</div>
        <div style="font-size: 18px; color: var(--text-sub); margin-top: 8px; line-height: 1.4;">AI and humans engage through structured rounds of arguments, questioning, and clarification.</div>
      </div>
      <div class="card">
        <span style="font-family: var(--font-m); font-size: 36px; font-weight: 700; color: var(--blue);">05</span>
        <div style="font-size: 22px; font-weight: 700; color: var(--text); margin-top: 8px;">Re-evaluate</div>
        <div style="font-size: 18px; color: var(--text-sub); margin-top: 8px; line-height: 1.4;">Midpoint and final check-ins track how confidence levels and perspectives shift during the debate.</div>
      </div>
      <div class="card">
        <span style="font-family: var(--font-m); font-size: 36px; font-weight: 700; color: var(--blue);">06</span>
        <div style="font-size: 22px; font-weight: 700; color: var(--text); margin-top: 8px;">Takeaway</div>
        <div style="font-size: 18px; color: var(--text-sub); margin-top: 8px; line-height: 1.4;">The audience awards a "Gold Star". Visitors receive a personalized digital summary via QR code.</div>
      </div>
    </div>
  </div>
</section>
```

**Step 2: Rebuild slide 6 (Architecture) as editorial split with card-based points**

```html
<section class="slide" data-act="ACT 2: THE EXPERIENCE">
  <div class="layout-split img-right">
    <div class="split-text">
      <p class="label reveal">System Design</p>
      <h2 class="reveal r1">Role-Based<br>Architecture</h2>
      <p class="body-text reveal r2" style="margin-bottom: 24px;">Not a standard chatbot array. A modular Role-Based Architecture layered over 13 Talmudic Thinking Modes.</p>
      <div style="display: flex; flex-direction: column; gap: 12px;" class="reveal r3">
        <div class="card" style="padding: 20px 24px;">
          <div style="font-size: 20px; font-weight: 600; color: var(--text);">Separate Persona from Role</div>
          <div style="font-size: 18px; color: var(--text-sub); margin-top: 4px;">The character (e.g., Rambam) is separated from the function (e.g., Devil's Advocate).</div>
        </div>
        <div class="card" style="padding: 20px 24px;">
          <div style="font-size: 20px; font-weight: 600; color: var(--text);">Seamless Swapping</div>
          <div style="font-size: 18px; color: var(--text-sub); margin-top: 4px;">Personas step into different roles depending on the session's needs. Humans and AI swap freely.</div>
        </div>
        <div class="card" style="padding: 20px 24px;">
          <div style="font-size: 20px; font-weight: 600; color: var(--text);">Active Intelligence</div>
          <div style="font-size: 18px; color: var(--text-sub); margin-top: 4px;">Real-time fact-checking, cultural sensitivity filtering, and logical contradiction tracking.</div>
        </div>
      </div>
    </div>
    <div class="split-img">
      <img src="slides/slide-06/hero.png" alt="Architecture">
    </div>
  </div>
</section>
```

**Step 3: Rebuild slide 7 (Sample Session) as editorial split (image left)**

```html
<section class="slide" data-act="ACT 2: THE EXPERIENCE">
  <div class="layout-split img-left">
    <div class="split-img">
      <img src="slides/slide-07/hero.png" alt="Goring Ox session">
    </div>
    <div class="split-text">
      <p class="label reveal">Make It Real</p>
      <h2 class="reveal r1">Sample Session:<br>The Goring Ox</h2>
      <p class="body-text reveal r2">We modernize the ancient Talmudic "Goring Ox" into today's reality: <strong>"Who is liable when an Autonomous Vehicle causes a fatal accident?"</strong></p>
      <div style="display: flex; flex-direction: column; gap: 10px; margin-top: 24px;" class="reveal r3">
        <div style="display: flex; align-items: center; gap: 16px; padding: 14px 20px; background: var(--card-bg); border: 1px solid var(--card-border); border-radius: 10px; box-shadow: var(--card-shadow);">
          <span style="font-family: var(--font-m); font-size: 13px; color: var(--navy); font-weight: 600; white-space: nowrap;">RAMBAM</span>
          <span style="font-size: 18px; color: var(--text-sub);">Analyzes systemic causation</span>
        </div>
        <div style="display: flex; align-items: center; gap: 16px; padding: 14px 20px; background: var(--card-bg); border: 1px solid var(--card-border); border-radius: 10px; box-shadow: var(--card-shadow);">
          <span style="font-family: var(--font-m); font-size: 13px; color: var(--navy); font-weight: 600; white-space: nowrap;">SHAMMAI</span>
          <span style="font-size: 18px; color: var(--text-sub);">Challenges liability assumptions</span>
        </div>
        <div style="display: flex; align-items: center; gap: 16px; padding: 14px 20px; background: var(--card-bg); border: 1px solid var(--card-border); border-radius: 10px; box-shadow: var(--card-shadow);">
          <span style="font-family: var(--font-m); font-size: 13px; color: var(--navy); font-weight: 600; white-space: nowrap;">HERZL</span>
          <span style="font-size: 18px; color: var(--text-sub);">Envisions future systemic solutions</span>
        </div>
      </div>
      <p class="body-sm reveal r4">The Research Agent injects real-time crash statistics into the dialogue.</p>
    </div>
  </div>
</section>
```

**Step 4: Rebuild slide 8 (Two Configurations) as statement + 2 large cards**

```html
<section class="slide" data-act="ACT 2: THE EXPERIENCE">
  <div class="layout-statement">
    <p class="label reveal">Platform Versatility</p>
    <h2 class="reveal r1">One Platform.<br>Two Configurations.</h2>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 28px; margin-top: 32px; width: 100%; max-width: 1000px;" class="reveal r2">
      <div class="card" style="padding: 36px; border-top: 4px solid var(--navy);">
        <h3 style="font-size: 26px; font-weight: 700; color: var(--navy); margin-bottom: 12px;">Culture of Disagreement</h3>
        <p style="font-size: 20px; color: var(--text-sub); line-height: 1.5;">Pedagogical, process-focused, and collaborative. Includes real-time analytics like a "Polarization Score" and a "L'Shem Shamayim" index.</p>
        <div style="font-family: var(--font-m); font-size: 13px; color: var(--taupe); letter-spacing: 1px; margin-top: 20px; text-transform: uppercase;">Ideal for school groups</div>
      </div>
      <div class="card" style="padding: 36px; border-top: 4px solid var(--taupe);">
        <h3 style="font-size: 26px; font-weight: 700; color: var(--navy); margin-bottom: 12px;">Debate Mode</h3>
        <p style="font-size: 20px; color: var(--text-sub); line-height: 1.5;">Competitive, outcome-focused, and heavily rhetorical. Features structured rounds, opening statements, rebuttals, and audience voting.</p>
        <div style="font-family: var(--font-m); font-size: 13px; color: var(--taupe); letter-spacing: 1px; margin-top: 20px; text-transform: uppercase;">Ideal for general visitors & corporate</div>
      </div>
    </div>
    <p class="body-sm reveal r3" style="text-align: center; max-width: 800px; margin-top: 28px;">The same infrastructure serves both the pedagogical team's vision and the museum's need for a high-energy attraction.</p>
  </div>
</section>
```

**Step 5: Rebuild slide 9 (Physical Space) as hero full-bleed**

```html
<section class="slide" data-act="ACT 2: THE EXPERIENCE">
  <div class="layout-hero">
    <img src="slides/slide-10/hero.png" alt="Physical space" class="hero-bg">
    <div class="hero-scrim"></div>
    <div class="hero-content">
      <p class="label reveal" style="color: rgba(255,255,255,0.6);">Spatial Design</p>
      <h2 class="reveal r1" style="color: #fff; margin-bottom: 16px;">The Physical Space</h2>
      <p class="reveal r2" style="font-size: 24px; color: rgba(255,255,255,0.85); max-width: 700px;">A circular civic discourse arena designed by Yazdani Studio. Not a passive "aquarium" - every person in the room participates.</p>
      <div style="display: flex; gap: 12px; margin-top: 24px; flex-wrap: wrap;" class="reveal r3">
        <span style="padding: 10px 20px; border-radius: 8px; font-size: 16px; color: #fff; background: rgba(255,255,255,0.15); backdrop-filter: blur(8px); border: 1px solid rgba(255,255,255,0.2);">12 Interactive Kiosks</span>
        <span style="padding: 10px 20px; border-radius: 8px; font-size: 16px; color: #fff; background: rgba(255,255,255,0.15); backdrop-filter: blur(8px); border: 1px solid rgba(255,255,255,0.2);">Curved Benches</span>
        <span style="padding: 10px 20px; border-radius: 8px; font-size: 16px; color: #fff; background: rgba(255,255,255,0.15); backdrop-filter: blur(8px); border: 1px solid rgba(255,255,255,0.2);">Sage Portrait Screens</span>
        <span style="padding: 10px 20px; border-radius: 8px; font-size: 16px; color: #fff; background: rgba(255,255,255,0.15); backdrop-filter: blur(8px); border: 1px solid rgba(255,255,255,0.2);">Dynamic Spotlights</span>
      </div>
    </div>
  </div>
</section>
```

**Step 6: Verify all 5 slides render correctly**

**Step 7: Commit**

```bash
git add index.html
git commit -m "feat: slides 5-9 editorial layouts (cards, splits, hero)"
```

---

## Task 6: Restructure Slides 10-13 (ACT 3: Why It Works)

**Files:**
- Modify: `index.html` - slides 10 through 13

**Step 1: Rebuild slide 10 (POC) as editorial split with prominent pull quote**

```html
<section class="slide" data-act="ACT 3: WHY IT WORKS">
  <div class="layout-split img-right">
    <div class="split-text">
      <p class="label reveal">Proven Foundation</p>
      <h2 class="reveal r1">We Already<br>Did This.</h2>
      <p class="body-text reveal r2">The Maimonides (Rambam) interactive exhibit serves as our proven sibling project. Expert Micha Goodman validated the conversational quality and depth of our AI model.</p>
      <div class="reveal r3" style="margin-top: 28px; padding: 28px 32px; border-left: 4px solid var(--navy); background: rgba(0,48,87,0.03); border-radius: 0 12px 12px 0;">
        <p class="pull-quote" style="font-size: 28px;">"Rambam was a monologue sold in one slide. Sanhedrin is a multi-agent dialogue, the next evolution."</p>
      </div>
      <p class="body-sm reveal r4">We are scaling a validated mechanism, building immediate trust rather than starting from scratch.</p>
    </div>
    <div class="split-img">
      <img src="slides/slide-11/hero.png" alt="Proof of concept">
    </div>
  </div>
</section>
```

**Step 2: Rebuild slide 11 (70/30) as statement with large typography**

```html
<section class="slide" data-act="ACT 3: WHY IT WORKS">
  <div class="layout-statement">
    <p class="label reveal">Transparent Risk Assessment</p>
    <div class="reveal r1" style="display: flex; align-items: baseline; gap: 48px; margin-bottom: 32px;">
      <div style="text-align: center;">
        <div style="font-family: var(--font-d); font-size: 120px; font-weight: 800; color: var(--navy); line-height: 1;">70%</div>
        <div style="font-family: var(--font-m); font-size: 14px; letter-spacing: 2px; color: var(--taupe); margin-top: 8px;">SOLVED</div>
      </div>
      <div style="text-align: center;">
        <div style="font-family: var(--font-d); font-size: 120px; font-weight: 800; color: var(--blue); line-height: 1;">30%</div>
        <div style="font-family: var(--font-m); font-size: 14px; letter-spacing: 2px; color: var(--taupe); margin-top: 8px;">AHEAD</div>
      </div>
    </div>
    <div style="display: flex; flex-direction: column; gap: 16px; max-width: 900px; text-align: left;" class="reveal r2">
      <div class="card" style="padding: 20px 28px;">
        <p style="font-size: 20px; color: var(--text-sub); line-height: 1.5;"><strong style="color: var(--text);">Solved:</strong> Individual agent quality, conversation protocols, character modeling (68 figures), and core content framework.</p>
      </div>
      <div class="card" style="padding: 20px 28px;">
        <p style="font-size: 20px; color: var(--text-sub); line-height: 1.5;"><strong style="color: var(--text);">Ahead:</strong> A2A2H orchestration. Getting AI agents to debate each other while synthesizing outputs for human interaction.</p>
      </div>
      <div class="card" style="padding: 20px 28px;">
        <p style="font-size: 20px; color: var(--text-sub); line-height: 1.5;"><strong style="color: var(--text);">Mitigation:</strong> Proving this via Phase 1 POC using a multi-agent WhatsApp group to test live dynamics before building the UI.</p>
      </div>
    </div>
  </div>
</section>
```

**Step 3: Rebuild slide 12 (Competitive) with full-width editorial table**

```html
<section class="slide" data-act="ACT 3: WHY IT WORKS">
  <div class="layout-statement" style="justify-content: flex-start; padding-top: 48px;">
    <p class="label reveal">Market Position</p>
    <h2 class="reveal r1">Competitive Advantage</h2>
    <table class="matrix reveal r2" style="max-width: 1000px; margin-top: 28px;">
      <thead>
        <tr><th style="padding: 16px 20px;">Capability</th><th style="padding: 16px 20px;">Chatbots</th><th style="padding: 16px 20px;">Museums</th><th style="padding: 16px 20px;">Debate AI</th><th style="padding: 16px 20px; color: var(--navy);">Sanhedrin</th></tr>
      </thead>
      <tbody>
        <tr><td>Multi-perspective (5-7 characters)</td><td class="x">-</td><td class="x">-</td><td class="x">-</td><td class="check">Yes</td></tr>
        <tr><td>No single "right answer"</td><td class="x">-</td><td class="check">Yes</td><td class="x">-</td><td class="check">Yes</td></tr>
        <tr><td>Orchestrated Meta-Logic (13 Modes)</td><td class="x">-</td><td class="x">-</td><td class="x">-</td><td class="check">Yes</td></tr>
        <tr><td>Physical immersive space</td><td class="x">-</td><td class="check">Yes</td><td class="x">-</td><td class="check">Yes</td></tr>
        <tr class="highlight"><td>Institutional backing (MOTJ)</td><td class="x">-</td><td class="check">Yes</td><td class="x">-</td><td class="check">Yes</td></tr>
      </tbody>
    </table>
    <p class="body-sm reveal r3" style="text-align: center; max-width: 800px; margin-top: 24px;">The "moat" is clear: The innovation is in the brilliant integration of agentic systems with a structured dispute methodology, not inventing new LLMs.</p>
  </div>
</section>
```

**Step 4: Rebuild slide 13 (EdTech) as editorial split with tier cards**

```html
<section class="slide" data-act="ACT 3: WHY IT WORKS">
  <div class="layout-split img-right">
    <div class="split-text">
      <p class="label reveal">Expanding the TAM</p>
      <h2 class="reveal r1">The EdTech<br>Platform Play</h2>
      <p class="body-text reveal r2">The "Debate Gym". This is not just a museum exhibit, it is a highly scalable education technology ecosystem.</p>
      <div style="display: flex; flex-direction: column; gap: 12px; margin-top: 24px;" class="reveal r3">
        <div class="card" style="padding: 20px 24px; border-left: 4px solid var(--navy);">
          <div style="font-size: 20px; font-weight: 600; color: var(--text);">Museum</div>
          <div style="font-size: 18px; color: var(--text-sub); margin-top: 4px;">The premium, peak, immersive live experience.</div>
        </div>
        <div class="card" style="padding: 20px 24px; border-left: 4px solid var(--blue);">
          <div style="font-size: 20px; font-weight: 600; color: var(--text);">Schools</div>
          <div style="font-size: 18px; color: var(--text-sub); margin-top: 4px;">"School of Civic Discourse" programs with direct curriculum integration.</div>
        </div>
        <div class="card" style="padding: 20px 24px; border-left: 4px solid var(--taupe);">
          <div style="font-size: 20px; font-weight: 600; color: var(--text);">Home / Online</div>
          <div style="font-size: 18px; color: var(--text-sub); margin-top: 4px;">Async platform and debate training tools. Open your camera, speak, get AI analysis on your rhetoric.</div>
        </div>
      </div>
    </div>
    <div class="split-img">
      <img src="slides/slide-14/hero.png" alt="EdTech platform">
    </div>
  </div>
</section>
```

**Step 5: Verify all 4 slides**

**Step 6: Commit**

```bash
git add index.html
git commit -m "feat: slides 10-13 editorial layouts (split, statement, table)"
```

---

## Task 7: Restructure Slides 14-17 (ACT 4: The Ask)

**Files:**
- Modify: `index.html` - slides 14 through 17

**Step 1: Rebuild slide 14 (Roadmap) with timeline cards**

```html
<section class="slide" data-act="ACT 4: THE ASK">
  <div class="layout-statement" style="justify-content: flex-start; padding-top: 48px;">
    <p class="label reveal">Execution Plan</p>
    <h2 class="reveal r1">Roadmap & Milestones</h2>
    <div style="display: flex; gap: 20px; margin-top: 36px; width: 100%; max-width: 1100px; position: relative;" class="reveal r2">
      <!-- Timeline connector line -->
      <div style="position: absolute; top: 50%; left: 5%; right: 5%; height: 2px; background: var(--blue); z-index: 0;"></div>
      <div class="card" style="flex: 1; position: relative; z-index: 1; padding: 28px;">
        <div style="font-family: var(--font-m); font-size: 12px; letter-spacing: 2px; color: var(--taupe); text-transform: uppercase;">Phase 1 (Now)</div>
        <div style="font-size: 28px; font-weight: 700; color: var(--navy); margin-top: 8px;">POC</div>
        <div style="font-size: 18px; color: var(--text-sub); margin-top: 10px; line-height: 1.4;">WhatsApp group with 3 agents + 2 humans to test live dynamics and A2A mechanics.</div>
      </div>
      <div class="card" style="flex: 1; position: relative; z-index: 1; padding: 28px;">
        <div style="font-family: var(--font-m); font-size: 12px; letter-spacing: 2px; color: var(--taupe); text-transform: uppercase;">Phase 2 (3 Months)</div>
        <div style="font-size: 28px; font-weight: 700; color: var(--navy); margin-top: 8px;">Working Demo</div>
        <div style="font-size: 18px; color: var(--text-sub); margin-top: 10px; line-height: 1.4;">Text-based demo with 5 historical characters and the orchestrator logic.</div>
      </div>
      <div class="card" style="flex: 1; position: relative; z-index: 1; padding: 28px;">
        <div style="font-family: var(--font-m); font-size: 12px; letter-spacing: 2px; color: var(--taupe); text-transform: uppercase;">Phase 3 (6 Months)</div>
        <div style="font-size: 28px; font-weight: 700; color: var(--navy); margin-top: 8px;">Prototype</div>
        <div style="font-size: 18px; color: var(--text-sub); margin-top: 10px; line-height: 1.4;">Full experience prototype with physical space mockup and AV testing.</div>
      </div>
      <div class="card" style="flex: 1; position: relative; z-index: 1; padding: 28px;">
        <div style="font-family: var(--font-m); font-size: 12px; letter-spacing: 2px; color: var(--taupe); text-transform: uppercase;">Phase 4 (12 Months)</div>
        <div style="font-size: 28px; font-weight: 700; color: var(--navy); margin-top: 8px;">Deployment</div>
        <div style="font-size: 18px; color: var(--text-sub); margin-top: 10px; line-height: 1.4;">Launch-ready at MOTJ, ready for 100,000+ annual visitors.</div>
      </div>
    </div>
  </div>
</section>
```

**Step 2: Rebuild slide 15 (Business Case) as editorial split (image left)**

```html
<section class="slide" data-act="ACT 4: THE ASK">
  <div class="layout-split img-left">
    <div class="split-img">
      <img src="slides/slide-16/hero.png" alt="Business case">
    </div>
    <div class="split-text">
      <p class="label reveal">Strategic ROI</p>
      <h2 class="reveal r1">Business Case &<br>The Research Hub</h2>
      <div style="display: flex; flex-direction: column; gap: 12px;" class="reveal r2">
        <div class="card" style="padding: 20px 24px;">
          <div style="font-size: 20px; font-weight: 600; color: var(--text);">The External Ask</div>
          <div style="font-size: 18px; color: var(--text-sub); margin-top: 4px;">Funding for tech architecture, content development, and AV spatial build-out.</div>
        </div>
        <div class="card" style="padding: 20px 24px;">
          <div style="font-size: 20px; font-weight: 600; color: var(--text);">Revenue Model</div>
          <div style="font-size: 18px; color: var(--text-sub); margin-top: 4px;">Museum admission, premium VIP tiers, licensing, and EdTech B2B subscriptions.</div>
        </div>
        <div class="card" style="padding: 20px 24px;">
          <div style="font-size: 20px; font-weight: 600; color: var(--text);">The Research Hub</div>
          <div style="font-size: 18px; color: var(--text-sub); margin-top: 4px;">Privacy-first, anonymized data repository on societal moral reasoning. Academic partnerships.</div>
        </div>
      </div>
    </div>
  </div>
</section>
```

**Step 3: Rebuild slide 16 (Team) as statement with larger cards**

```html
<section class="slide" data-act="ACT 4: THE ASK">
  <div class="layout-statement">
    <p class="label reveal">Internal Alignment</p>
    <h2 class="reveal r1">The Team</h2>
    <div style="display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; margin-top: 28px; max-width: 900px;" class="reveal r2">
      <div class="card" style="padding: 28px 32px;">
        <div style="font-size: 26px; font-weight: 700; color: var(--navy);">Jonathan</div>
        <div style="font-size: 20px; color: var(--text-sub); margin-top: 6px;">Tech Architecture</div>
      </div>
      <div class="card" style="padding: 28px 32px;">
        <div style="font-size: 26px; font-weight: 700; color: var(--navy);">Daniel</div>
        <div style="font-size: 20px; color: var(--text-sub); margin-top: 6px;">Project Strategy</div>
      </div>
      <div class="card" style="padding: 28px 32px;">
        <div style="font-size: 26px; font-weight: 700; color: var(--navy);">Doron</div>
        <div style="font-size: 20px; color: var(--text-sub); margin-top: 6px;">Knowledge & Design</div>
      </div>
      <div class="card" style="padding: 28px 32px; border-style: dashed; border-color: var(--taupe);">
        <div style="font-size: 26px; font-weight: 700; color: var(--taupe);">The Missing Piece</div>
        <div style="font-size: 20px; color: var(--text-sub); margin-top: 6px;">World-renowned debate content expert for competitive mode design.</div>
      </div>
    </div>
  </div>
</section>
```

**Step 4: Rebuild slide 17 (CTA) as hero full-bleed**

```html
<section class="slide" data-act="ACT 4: THE ASK">
  <div class="layout-hero">
    <img src="slides/slide-18/hero.png" alt="Closing" class="hero-bg">
    <div class="hero-scrim"></div>
    <div class="hero-content" style="text-align: center; display: flex; flex-direction: column; align-items: center;">
      <div class="pull-quote reveal r1" style="color: #fff; max-width: 800px; font-size: 34px; border-left: none; padding: 0;">"The Sanhedrin didn't give answers. They gave people the tools to think. We're bringing that to the 21st century."</div>
      <p class="reveal r2" style="font-size: 22px; color: rgba(255,255,255,0.8); margin-top: 24px; max-width: 700px;">Give us the "Green Light" to move past the 70% mark, fund the Phase 1 POC, and schedule the deep-dive technical review.</p>
      <div style="display: flex; gap: 16px; margin-top: 32px;" class="reveal r3">
        <button class="cta-btn" style="background: #fff; color: var(--navy);">Approve Phase 1 POC</button>
        <a class="cta-btn-outline" style="color: #fff; border-color: rgba(255,255,255,0.5);" href="#" target="_blank">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polygon points="5 3 19 12 5 21 5 3"/></svg>
          View Tech Architecture
        </a>
      </div>
    </div>
  </div>
</section>
```

**Step 5: Verify all 4 slides**

**Step 6: Commit**

```bash
git add index.html
git commit -m "feat: slides 14-17 editorial layouts (timeline, split, hero CTA)"
```

---

## Task 8: Restyle Appendix Slides + Nav Bar + Progress Bar

**Files:**
- Modify: `index.html` - appendix sections and nav/progress elements

**Step 1: Update appendix slides to use light editorial typography**

Increase all appendix text sizes: headings to 48px, list items to 20px, grid gaps wider. Keep current content structure but apply `.card` class to persona cards. Remove dark theme references.

**Step 2: Restyle nav bar for light theme**

Remove theme toggle button and its JS handler. Update counter/label colors to navy/taupe. Update progress bar gradient to navy-based.

**Step 3: Update JS to remove theme toggle references**

Remove `toggleTheme()` function. Remove `data-theme` attribute handling. Set body to always use the light variables.

**Step 4: Verify appendix and nav render correctly**

**Step 5: Commit**

```bash
git add index.html
git commit -m "feat: appendix editorial styling, light-only nav bar, remove theme toggle"
```

---

## Task 9: Update Responsive Breakpoints

**Files:**
- Modify: `index.html` - `@media` blocks in CSS

**Step 1: Update 1024px and 640px breakpoints**

```css
@media (max-width: 1024px) {
  .slide { padding: 36px 36px 64px; }
  h1 { font-size: 56px; }
  h2 { font-size: 44px; }
  .body-text { font-size: 20px; }
  .tagline { font-size: 26px; }
  .layout-split, .layout-split.img-right, .layout-split.img-left {
    grid-template-columns: 1fr; gap: 0;
  }
  .layout-split .split-img { max-height: 40vh; }
  .layout-split .split-img img { height: 40vh; }
  .layout-hero .hero-content { padding: 0 36px 64px; }
}
@media (max-width: 640px) {
  h1 { font-size: 40px; }
  h2 { font-size: 36px; }
  .body-text { font-size: 18px; }
  .layout-hero .hero-content { padding: 0 18px 64px; }
  .pull-quote { font-size: 28px; }
}
```

**Step 2: Test at various widths**

**Step 3: Commit**

```bash
git add index.html
git commit -m "fix: responsive breakpoints for editorial layouts"
```

---

## Task 10: Generate New Editorial Images via Nanobanana

**Files:**
- Output: `slides/slide-NN/hero.png` (11 images)

**Step 1: Generate images using nanobanana MCP tool**

Generate each image one at a time with editorial prompts. Save to existing `slides/slide-NN/` directories. Target 16:9 aspect ratio.

Image prompts (from design doc):
1. slide-01: "Circular amphitheater-style discussion space with warm wood and modern design, people gathered in discussion, dramatic warm lighting from above, museum setting, editorial photography, 16:9"
2. slide-02: "Diverse group of people in a room, some turning away from each other, tension and disconnection visible, editorial documentary style, warm tones, 16:9"
3. slide-03: "Hands arranging translucent puzzle pieces on a light table, warm overhead lighting, close-up detail shot, editorial photography, 16:9"
5. slide-05: (no image needed - statement slide with cards)
6. slide-06: "Abstract visualization of connected nodes and pathways, warm tones, editorial tech photography, 16:9"
7. slide-07: "Three people in animated but respectful discussion at a round table, warm lighting, editorial portrait, 16:9"
9. slide-10: "Circular amphitheater with 12 modern interactive stations, curved wooden benches, dramatic overhead lighting, architectural interior photography, 16:9"
10. slide-11: "Person engaging with interactive museum exhibit, glowing screen, intimate close-up, warm editorial lighting, 16:9"
13. slide-14: "Students in modern classroom using tablets, engaged in discussion, warm natural light, editorial education photography, 16:9"
15. slide-16: "Aerial view of modern research hub with data visualizations on screens, warm tones, editorial corporate photography, 16:9"
17. slide-18: "Wide shot of amphitheater from above, all stations active with warm glowing screens, people engaged, dramatic cinematic lighting, 16:9"

**Step 2: Verify all images load in the deck**

**Step 3: Commit**

```bash
git add slides/
git commit -m "feat: regenerate hero images in editorial photography style"
```

---

## Task 11: Final QA and Push

**Step 1: Full scroll-through of all 21 slides**

Check: text readability, image display, card visibility, nav functionality, responsive at 1440px and 1024px.

**Step 2: Verify no em-dashes or emojis**

```bash
grep -n '—' index.html  # should return nothing
```

**Step 3: Push to deploy**

```bash
git push origin master
```

Render auto-deploys. Verify at https://sanhedrin-deck.onrender.com
