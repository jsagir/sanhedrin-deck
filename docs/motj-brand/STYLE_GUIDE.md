# MOTJ Brand Style Guide — Sanhedrin Deck Reference

## Brand Colors

| Swatch | PMS | Hex | Usage |
|--------|-----|-----|-------|
| Navy (Primary) | PMS 540 | `#003057` | Primary dark backgrounds, text on light surfaces |
| Light Blue Accent | PMS 544 | `#BDD6E6` | Accent elements, secondary icon fills, highlights |
| Warm Taupe | PMS 404 | `#776E64` | Neutral accent, body text on light backgrounds |

### CSS Variable Mapping (index.html)

```css
--bg-deep:       #003057;   /* PMS 540 — Primary navy */
--gold-primary:  #BDD6E6;   /* PMS 544 — Light blue accent */
--teal:          #776E64;   /* PMS 404 — Warm taupe */
--text-primary:  #f0f4f7;   /* White on dark */
```

## Fonts

| Role | Brand Font | Web Proxy | Notes |
|------|-----------|-----------|-------|
| Display / Heading | Gotham Medium | Montserrat 600 | Google Fonts, closest match to Gotham |
| Body Text | Gotham Book | Montserrat 400 | Google Fonts |
| Hebrew | Almoni Neue DL 4.0 AAA | — | Not loaded in web deck |
| Arabic | Markazi Text | — | Not loaded in web deck |
| Mono / Labels | — | JetBrains Mono | Technical text, data labels |

## Logo Assets

All logos live in `assets/logos/`. Source files from the MOTJ brand guide are also copied here.

### Naming Convention

| File | Description | Use Case |
|------|-------------|----------|
| `motj-icon-color.svg` | Icon (mountain mark + MOTJ text), navy + light blue | Light backgrounds |
| `motj-icon-white.svg` | Icon, all white (light blue at 44% opacity) | Dark backgrounds |
| `motj-logo-horizontal.png` | Full horizontal logo, color PNG | Light backgrounds |
| `motj-logo-horizontal-color.png` | Full horizontal logo, color PNG (alt) | Light backgrounds |
| `motj-logo-horizontal-white.svg` | Full horizontal logo, white SVG | Dark backgrounds |
| `motj-logo-icon.png` | Icon-only PNG | Nav bars, favicons |
| `MOTJ Logo_2023-09-04_w long.svg` | Source white horizontal SVG (with border) | Reference only |
| `MOTJ Logo_2023-09-04.svg` | Source color full logo SVG | Reference only |
| `MOTJ Logo_2023-09-04_logo&motj.svg` | Source short-form SVG | Reference only |

### Logo Usage Rules

1. **Horizontal layout** — Use for headers, hero areas, and wide placements.
2. **Short form** (icon + MOTJ text) — Use for compact spaces where full name is too wide.
3. **Icon only** — Use for minimal placements: nav bars, favicons, small badges.
4. **On dark backgrounds** — Always use the white version (`-white` suffix).
5. **On light backgrounds** — Always use the color version (`-color` suffix or default).
6. **Clear space** — Maintain minimum clear space around the logo equal to the height of the "M" in MOTJ.
7. **Do not** — Stretch, rotate, recolor beyond provided variants, or place on busy backgrounds without sufficient contrast.

## Brand Reference Images

The following reference images from the original brand guide are stored in `docs/motj-brand/`:

- `Pallete colors .png` — Official color palette card
- `Fonts.png` — Font specimens
- `Font setup.png` — Font sizing and setup guide
