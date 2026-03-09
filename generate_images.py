#!/usr/bin/env python3
"""Generate hero images for Sanhedrin deck slides via Gemini API.
Style: Editorial photography, warm lighting, shallow depth of field, 16:9."""

import json, base64, sys, os, time
from urllib.request import Request, urlopen
from urllib.error import HTTPError

# Load from .env file if present
_env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")
if os.path.exists(_env_path):
    with open(_env_path) as f:
        for line in f:
            if "=" in line and not line.startswith("#"):
                k, v = line.strip().split("=", 1)
                os.environ.setdefault(k, v)

API_KEY = os.environ.get("GEMINI_API_KEY", "")
MODEL = "gemini-2.5-flash-image"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"
BASE_DIR = "/home/jsagi/sanhedrin-deck/slides"

STYLE = "Editorial photography style, warm natural lighting, shallow depth of field, 16:9 wide aspect ratio, professional color grading with warm tones, no text or watermarks"

SLIDES = {
    "slide-01": f"Circular amphitheater-style discussion space with warm walnut wood seating and modern design, diverse group of people gathered in animated discussion, dramatic warm golden lighting from above, premium museum interior setting. {STYLE}",

    "slide-02": f"Diverse group of people in a modern room, some turning away from each other with visible tension and disconnection, body language showing disagreement and frustration, warm muted tones, dramatic side lighting. {STYLE}",

    "slide-03": f"Close-up of hands carefully arranging translucent glass puzzle pieces on a warmly lit wooden table, soft overhead lighting creating gentle reflections, warm amber tones, premium product photography. {STYLE}",

    "slide-05": f"Museum visitors interacting with sleek modern touchscreen kiosks arranged in a curved space, warm ambient lighting, people engaged and focused, architectural interior photography. {STYLE}",

    "slide-06": f"Abstract visualization of connected glowing nodes and digital pathways, warm amber and deep navy blue tones, soft bokeh lights in background, modern technology aesthetic with warm human feel. {STYLE}",

    "slide-07": f"Three diverse professionals in animated but respectful discussion at a round wooden table, warm natural lighting, expressive hand gestures, engaged facial expressions, modern office with warm wood interior. {STYLE}",

    "slide-10": f"Circular amphitheater interior with modern interactive touchscreen stations arranged in a circle, curved wooden benches, warm dramatic overhead spotlighting, brushed aluminum and walnut wood materials, premium museum space. {STYLE}",

    "slide-11": f"Person engaging with a glowing interactive museum exhibit screen, their face illuminated by warm screen light, hands touching the display, dark blurred background, intimate close-up. {STYLE}",

    "slide-14": f"Students in a bright modern classroom using tablets, engaged in lively group discussion, warm natural sunlight streaming through large windows, diverse young people, education setting. {STYLE}",

    "slide-16": f"Aerial view of a modern research hub workspace with large screens showing colorful data visualizations and analytics dashboards, people collaborating at desks, warm ambient lighting, premium corporate interior. {STYLE}",

    "slide-18": f"Dramatic wide-angle view of a circular amphitheater from above, all interactive stations active with warm glowing screens, people engaged in discussion at each station, dramatic cinematic overhead lighting with warm golden tones, museum interior. {STYLE}",
}

def generate_image(slide_name, prompt):
    payload = json.dumps({
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {"responseModalities": ["TEXT", "IMAGE"]}
    }).encode()

    req = Request(URL, data=payload, headers={"Content-Type": "application/json"})
    try:
        resp = urlopen(req, timeout=120)
        data = json.loads(resp.read())
    except HTTPError as e:
        error_body = e.read().decode()
        print(f"  FAILED {slide_name}: HTTP {e.code} - {error_body[:200]}", flush=True)
        return False
    except Exception as e:
        print(f"  FAILED {slide_name}: {e}", flush=True)
        return False

    for candidate in data.get("candidates", []):
        fr = candidate.get("finishReason", "")
        if fr == "SAFETY":
            print(f"  BLOCKED {slide_name}: Safety filter", flush=True)
            return False
        if fr == "RECITATION":
            print(f"  BLOCKED {slide_name}: Recitation filter", flush=True)
            return False
        for part in candidate.get("content", {}).get("parts", []):
            if "inlineData" in part:
                img_data = base64.b64decode(part["inlineData"]["data"])
                mime = part["inlineData"].get("mimeType", "image/png")
                ext = "png" if "png" in mime else "jpg" if "jpeg" in mime or "jpg" in mime else "webp"
                out_dir = os.path.join(BASE_DIR, slide_name)
                os.makedirs(out_dir, exist_ok=True)
                path = os.path.join(out_dir, f"hero.{ext}")
                with open(path, "wb") as f:
                    f.write(img_data)
                print(f"  OK {slide_name}/hero.{ext} ({len(img_data)//1024}KB)", flush=True)
                return path

    print(f"  FAILED {slide_name}: No image in response", flush=True)
    return False

if __name__ == "__main__":
    total = len(SLIDES)
    success = 0
    failed = []

    for i, (name, prompt) in enumerate(SLIDES.items(), 1):
        print(f"[{i}/{total}] Generating {name}...", flush=True)
        result = generate_image(name, prompt)
        if result:
            success += 1
        else:
            failed.append(name)
        if i < total:
            time.sleep(3)

    print(f"\nDone: {success}/{total} images generated", flush=True)
    if failed:
        print(f"Failed: {', '.join(failed)}")
