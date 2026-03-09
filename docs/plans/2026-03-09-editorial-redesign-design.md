# Sanhedrin Deck - Editorial/Magazine Redesign

**Date:** 2026-03-09
**Context:** Deck is shared as a link (investor reads on laptop). Current design is dry, underuses screen real estate, text too small, images cut off.
**Direction:** Editorial/magazine - light background, bold typography, full-bleed photography, generous whitespace.

## Visual Language

### Color Palette (MOTJ brand, inverted usage)
| Role | Value | Usage |
|------|-------|-------|
| Base | #F5F2EB (warm off-white) | Page background |
| Surface | #FFFFFF | Cards, overlays |
| Navy | #003057 (PMS 540) | Headlines, hero blocks, CTA |
| Light Blue | #BDD6E6 (PMS 544) | Subtle accents, dividers |
| Taupe | #776E64 (PMS 404) | Labels, secondary text |
| Text | #1A1A1A | Body copy |
| Text Sub | #4A4A4A | Secondary body |
| Text Dim | #8A8A8A | Captions, metadata |

### Typography
- **Hero headlines:** Montserrat 800, 80-96px, navy
- **Section headlines:** Montserrat 700, 56-64px, navy
- **Subheads:** Montserrat 600, 28-32px, text
- **Body:** Montserrat 400, 22-24px, line-height 1.6
- **Labels:** JetBrains Mono 500, 12-13px, uppercase, taupe, letter-spacing 4px
- **Pull quotes:** Montserrat 300 italic, 36-40px, navy

### Image Style (regenerate via nanobanana)
- Photographic/editorial: real-feeling museum spaces, people deliberating, close-up details
- Warm lighting, shallow depth-of-field aesthetic
- Color grading: warm tones with MOTJ navy accents
- 16:9 ratio, full-bleed ready (no white backgrounds)
- No isometric renders, no cartoon/diagram style

## Layout System

### 3 Layout Types

**1. Hero (full-bleed image + text overlay)**
- Image covers 100% viewport
- Text overlaid with semi-transparent gradient scrim
- Used for: title slide, CTA slide, section openers

**2. Editorial Split (image bleeds to edge)**
- Image column: 50-55%, bleeds to viewport edge (no padding)
- Text column: 45-50%, comfortable 60-80px padding
- Image can be left or right
- Used for: most content slides

**3. Statement (typography-driven, no image)**
- Centered or left-aligned massive headline
- Supporting text and/or card grid below
- Used for: value prop, modes, roadmap, team

### Slide Padding
- Text areas: 60px top, 80px sides, 72px bottom
- Image areas: 0px (bleed to edges)
- Nav bar remains fixed at bottom

### Cards
- Background: white (#FFFFFF)
- Border: 1px solid rgba(0,48,87,0.08)
- Shadow: 0 2px 12px rgba(0,0,0,0.06)
- Border-radius: 12px
- Padding: 28-32px

## Slide-by-Slide Plan

### ACT 1: THE HOOK

**Slide 1 - Title/Hero**
- Layout: Hero (full-bleed)
- Full-bleed editorial photo (circular discussion space, warm light)
- MOTJ logo top-left, white
- "The Sanhedrin Educational Experience" in massive white text
- "Disagree Better. Discover Together." as tagline
- Gradient scrim from bottom

**Slide 2 - The Problem**
- Layout: Editorial split (image right, bleeds)
- Photo: polarized crowd or divided space
- Bold stat or pull quote as visual anchor
- Body text with "The Gap" callout

**Slide 3 - Cognitive Twist**
- Layout: Editorial split (image left, bleeds)
- Photo: puzzle/investigation metaphor
- 3 bullet points, larger text
- L'Shem Shamayim as styled callout

**Slide 4 - Value Prop**
- Layout: Statement
- Massive centered quote: "Learn to argue better in 30 minutes."
- INPUT / ENGINE / OUTPUT as 3 bold graphic blocks (navy bg, white text, large)
- No image needed

### ACT 2: THE EXPERIENCE

**Slide 5 - Visitor Journey**
- Layout: Statement + cards
- 6 journey steps as large cards (2x3 grid or horizontal)
- Each card: large step number, title, description at readable size
- Subtle connecting line or arrow between cards

**Slide 6 - Architecture**
- Layout: Editorial split (image right)
- Photo: abstract tech/system visualization
- 3 key points as styled cards, not bullet list

**Slide 7 - Sample Session**
- Layout: Editorial split (image left)
- Photo: dramatic deliberation scene
- Thinker chips much larger (pill-shaped, with role description)
- Scenario description prominent

**Slide 8 - Two Configurations**
- Layout: Statement + 2 cards
- Two large side-by-side mode cards
- Each card: distinct visual treatment (different accent color or icon)
- Supporting text below

**Slide 9 - Physical Space**
- Layout: Hero (full-bleed)
- Architectural render bleeds full viewport
- Feature pills overlay on semi-transparent bar at bottom
- Text overlay with gradient scrim

### ACT 3: WHY IT WORKS

**Slide 10 - POC (Rambam)**
- Layout: Editorial split (image right)
- Photo: museum exhibit / interactive kiosk
- Pull quote from Micha Goodman prominent
- "Scaling a validated mechanism" as callout

**Slide 11 - 70/30 Risk**
- Layout: Statement
- Large "70%" and "30%" as visual graphic elements
- 3 bullet points enlarged
- Progress bar or visual indicator

**Slide 12 - Competitive**
- Layout: Statement (wide)
- Full-width editorial table
- Alternating row colors, generous cell padding
- Checkmarks styled as filled circles

**Slide 13 - EdTech**
- Layout: Editorial split (image right)
- Photo: students/classroom engagement
- Museum / Schools / Home as 3 distinct tier cards

### ACT 4: THE ASK

**Slide 14 - Roadmap**
- Layout: Statement + cards
- 4 phase cards in a row, each with timeline, title, description
- Connecting timeline line between them
- Generous card size

**Slide 15 - Business Case**
- Layout: Editorial split (image left)
- Photo: research/data visualization
- Revenue model as styled list/cards
- Research Hub callout

**Slide 16 - Team**
- Layout: Statement + cards
- 4 team cards (2x2), larger with photos if available
- "Missing Piece" card with dashed border remains

**Slide 17 - CTA**
- Layout: Hero (full-bleed)
- Dramatic closing image
- Large pull quote overlay
- Two prominent CTA buttons

### APPENDIX (A-D)
- Keep current content structure
- Switch to light editorial styling
- Increase font sizes across the board
- Better grid layouts for lists

## Image Generation Prompts (18 images)
All images: "Editorial photography style, warm natural lighting, shallow depth of field, 16:9 aspect ratio, professional color grading with warm tones"

1. Title: "Circular amphitheater-style discussion space with warm wood and modern design, people gathered in discussion, dramatic warm lighting from above, museum setting"
2. Problem: "Diverse group of people in a room, some turning away from each other, tension and disconnection visible, editorial documentary style"
3. Cognitive Twist: "Hands arranging translucent puzzle pieces on a light table, warm overhead lighting, close-up detail shot"
4. (no image - statement slide)
5. Visitor Journey: "Museum visitors interacting with sleek touchscreen kiosks in a curved space, warm ambient lighting, architectural photography"
6. Architecture: "Abstract visualization of connected nodes and pathways, warm tones, editorial tech photography style"
7. Sample Session: "Three people in animated but respectful discussion at a round table, warm lighting, editorial portrait style"
8. (no image - statement slide)
9. Physical Space: "Circular amphitheater with 12 modern interactive stations, curved wooden benches, dramatic overhead lighting, architectural interior photography"
10. POC: "Person engaging with an interactive museum exhibit, glowing screen, intimate close-up, warm editorial lighting"
11. (no image - statement slide)
12. (no image - statement slide)
13. EdTech: "Students in a modern classroom using tablets, engaged in discussion, warm natural light from windows, editorial education photography"
14. (no image - statement slide)
15. Business: "Aerial view of a modern research hub with screens showing data visualizations, warm tones, editorial corporate photography"
16. (no image - statement slide)
17. CTA: "Wide shot of the amphitheater space from above, all stations active with warm glowing screens, people engaged, dramatic cinematic lighting"

## Navigation
- Keep arrow key/swipe navigation
- Keep progress bar (restyle to match light theme)
- Keep bottom nav bar (restyle: light bg, navy text)
- Keep fullscreen toggle
- Add: slide thumbnail strip (optional, low priority)

## What Does NOT Change
- Single HTML file architecture
- Slide engine JS (transitions, navigation)
- Content text (17 + 4 appendix structure)
- MOTJ brand compliance (3 Pantone colors)
- No em-dashes, no emojis rules
