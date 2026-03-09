#!/usr/bin/env python3
"""Generate hero images for Sanhedrin deck slides via Gemini API."""

import json, base64, sys, os, time
from urllib.request import Request, urlopen
from urllib.error import HTTPError

API_KEY = "AIzaSyBTygbL5lzZYonciNrRhgDv79NK9yC_qDQ"
MODEL = "gemini-2.5-flash-image"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"
OUT_DIR = "/home/jsagi/sanhedrin-deck/assets"

SLIDES = {
    "slide-01-hero": 'High-fidelity top-down isometric 3D render, next-gen "Sims 8" stylized realism aesthetic. A futuristic circular museum arena isolated on a pure white background for easy cutout. Expressive, modern "Sims" style visitors are standing around a sleek, glowing circular digital console. Surrounding them are life-sized, high-fidelity holographic projections of historical figures. The space features curved wooden benches and vertical glass touchscreens. Vibrant global illumination, deep blue and warm gold color palette, Unreal Engine 5 life-simulation style, hyper-detailed, clean edges.',

    "slide-02-polarization": 'High-fidelity top-down isometric 3D render, next-gen "Sims 8" stylized realism aesthetic. Isolated on a pure white background for easy cutout. Two groups of expressive, modern "Sims" style characters stand on opposite sides of a glowing, jagged red chasm splitting the white floor. Above them, floating 3D digital speech bubbles collide and shatter into glitch effects. Crisp, vibrant lighting, deep blue and glowing red color palette, high-end life-simulation game style, clean edges.',

    "slide-03-puzzle": 'High-fidelity top-down isometric 3D render, next-gen "Sims 8" stylized realism aesthetic. Isolated on a pure white background for easy cutout. A complex, glowing 3D jigsaw puzzle assembling itself mid-air over a sleek modern pedestal. Each puzzle piece emits a soft light, containing faint etchings of historical faces and data charts. The pieces lock together into a unified sphere of light. Crisp global illumination, cyan and amber glowing accents, high-end life-simulation UI style, clean cutout.',

    "slide-04-value-prop": 'High-fidelity top-down isometric 3D infographic, next-gen "Sims 8" stylized realism aesthetic. Isolated on a pure white background for easy cutout. A glowing technological loop: On the left, an expressive modern character inputs data into a sleek console. A light beam branches to the center into 5 floating, glowing nodes representing AI minds deliberating. The beams converge on the right into a brightly illuminated, stylized 3D human brain. Crisp lighting, neon blue and gold data streams, glass textures, game-ready UI aesthetic.',

    "slide-05-journey": 'High-fidelity top-down isometric 3D render, next-gen "Sims 8" stylized realism aesthetic. Isolated on a pure white background for easy cutout. A path of floating, illuminated glass stepping stones. The stones show sequential steps: a touchscreen kiosk, a friendly human facilitator character, a group of glowing AI avatars, and a glowing QR code on a smartphone. Interconnected laser lines map the journey. Bright, welcoming lighting, deep blue and warm gold accents, clean life-simulation UI design.',

    "slide-06-architecture": 'High-fidelity top-down isometric 3D render, next-gen "Sims 8" stylized realism aesthetic. Isolated on a pure white background for easy cutout. A digital "wardrobe" system. At the base, sleek glowing wireframe mannequins labeled with roles like Judge. Above them float highly detailed, stylized portrait avatars of historical figures inside glass data cards, actively slotting down into the wireframes. Clean, crisp lighting, deep blue and warm gold color palette, modern game UI aesthetic.',

    "slide-07-session": 'High-fidelity top-down isometric 3D render, next-gen "Sims 8" stylized realism aesthetic. Isolated on a pure white background for easy cutout. A sleek, interactive white display table. On the table, two glowing holographic 3D models: a modern autonomous vehicle and an ancient pair of brass scales of justice. Beams of data connect them, surrounded by floating game-style text boxes showing ethical questions. Crisp, vibrant lighting, deep blue and warm gold UI accents, hyper-detailed.',

    "slide-08-dilemma": 'High-fidelity top-down isometric 3D infographic, next-gen "Sims 8" stylized realism aesthetic. Isolated on a pure white background for easy cutout. A glowing, floating timeline. Above the timeline, three distinct, illuminated holographic bubbles float: a modern self-driving car next to an ancient ox, a smartphone with a chat bubble next to a scroll, and a medical DNA helix. Below the timeline, small sleek digital clocks. Bright, clean corporate game-tech aesthetic, deep blue and warm gold.',

    "slide-09-modes": 'High-fidelity top-down isometric 3D render, next-gen "Sims 8" stylized realism aesthetic. Isolated on a pure white background for easy cutout. A split-screen architectural diorama. The left side has calm, collaborative blue lighting with expressive student characters sitting peacefully around a glowing table. The right side features dynamic orange lighting with two distinct teams of characters facing each other in a game-show style debate setup. Crisp global illumination, high-end life-simulation graphics, clean cutout edges.',

    "slide-10-space": 'High-fidelity top-down isometric 3D architectural render, next-gen "Sims 8" build-mode aesthetic. Isolated on a pure white background for easy cutout. A wide semi-circle of modern white curved benches with individual glowing touchscreens. A sleek facilitator podium sits in the center. Vertical digital Sage Screens flank a curved immersive projection wall. Vibrant, inviting lighting, deep blue and warm gold color palette, clean modern game-design style.',

    "slide-11-proof": 'High-fidelity top-down isometric 3D render, next-gen "Sims 8" stylized realism aesthetic. Isolated on a pure white background for easy cutout. On the left, a single glowing ancient Hebrew manuscript transitions into a stylized, high-quality digital hologram of a historical figure. Sweeping lines of light expand outward to the right, forming a network of multiple interconnected holographic figures deliberating together. Crisp lighting, blue to gold gradient, clean cutout.',

    "slide-12-progress": 'High-fidelity top-down isometric 3D render, next-gen "Sims 8" stylized realism aesthetic. Isolated on a pure white background for easy cutout. A glowing architectural structure. The bottom 70% is solid, sleek, polished white metal and glass. The top 30% consists of glowing blue wireframes and holographic blueprints being actively constructed by digital laser beams representing Agent-to-Agent integration. Bright, inspiring tech-startup vibe, life-simulation build-mode aesthetic.',

    "slide-13-competitive": 'High-fidelity top-down isometric 3D render, next-gen "Sims 8" stylized realism aesthetic. Isolated on a pure white background for easy cutout. In the center, a sleek, multifaceted glowing diamond tower projects different colors of light, protected by a glowing digital moat. Around it sit basic, dull gray square boxes representing standard chatbots. Crisp, vibrant lighting, deep blue and warm gold UI palette, clean metaphorical game-art style.',

    "slide-14-edtech": 'High-fidelity top-down isometric 3D render, next-gen "Sims 8" stylized realism aesthetic. Isolated on a pure white background for easy cutout. Three floating stylized diorama islands connected by glowing data bridges. Top island: a sleek museum dome. Bottom-left: a vibrant modern classroom with smartboards and student characters. Bottom-right: a cozy home desk with a laptop and ring light. Bright, welcoming educational game aesthetic, crisp lighting, easy cutout.',

    "slide-15-roadmap": 'High-fidelity top-down isometric 3D render, next-gen "Sims 8" stylized realism aesthetic. Isolated on a pure white background for easy cutout. A glowing frosted glass staircase winding upward. Step 1: a smartphone with a chat bubble. Step 2: a laptop screen. Step 3: a modern museum kiosk. Step 4 (top): a fully realized, illuminated Sanhedrin circular arena diorama. Bright, uplifting lighting, deep blue and warm gold, clean edges for transparency.',

    "slide-16-business": 'High-fidelity top-down isometric 3D render, next-gen "Sims 8" stylized realism aesthetic. Isolated on a pure white background for easy cutout. A sleek, modern technological funnel mechanism. Glowing blue data particles flow into the top. The machine outputs two distinct streams at the bottom: shiny stylized gold coins, and illuminated, holographic academic documents and graphs. Vibrant, clean corporate-game UI illustration, crisp global illumination.',

    "slide-17-team": 'High-fidelity top-down isometric 3D render, next-gen "Sims 8" stylized realism aesthetic. Isolated on a pure white background for easy cutout. Three solid, glowing pillars made of sleek white marble and metal support a glowing platform. Next to them stands a fourth pillar that is an empty, glowing blue wireframe hologram, representing a missing expert waiting to be filled. Bright, clean architectural game-style graphics, deep blue and warm gold.',

    "slide-18-closing": 'High-fidelity top-down isometric 3D render, next-gen "Sims 8" stylized realism aesthetic. Isolated on a pure white background for easy cutout. Two stylized, expressive hands meeting over a sleek digital pedestal. One hand is slightly translucent, made of warm, ancient glowing light. The other is modern, solid, and reaching out. A brilliant spark of blue and white light illuminates the space between them. Crisp, vibrant lighting, emotional but clean game-art style.',
}

os.makedirs(OUT_DIR, exist_ok=True)

def generate_image(name, prompt):
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
        print(f"  FAILED {name}: HTTP {e.code} - {error_body[:200]}", flush=True)
        return False
    except Exception as e:
        print(f"  FAILED {name}: {e}", flush=True)
        return False

    for candidate in data.get("candidates", []):
        fr = candidate.get("finishReason", "")
        if fr == "SAFETY":
            print(f"  BLOCKED {name}: Safety filter", flush=True)
            return False
        if fr == "RECITATION":
            print(f"  BLOCKED {name}: Recitation filter", flush=True)
            return False
        for part in candidate.get("content", {}).get("parts", []):
            if "inlineData" in part:
                img_data = base64.b64decode(part["inlineData"]["data"])
                mime = part["inlineData"].get("mimeType", "image/png")
                ext = "png" if "png" in mime else "jpg" if "jpeg" in mime or "jpg" in mime else "webp"
                path = os.path.join(OUT_DIR, f"{name}.{ext}")
                with open(path, "wb") as f:
                    f.write(img_data)
                print(f"  OK {name}.{ext} ({len(img_data)//1024}KB)", flush=True)
                return True

    print(f"  FAILED {name}: No image in response", flush=True)
    return False

if __name__ == "__main__":
    total = len(SLIDES)
    success = 0
    failed = []

    for i, (name, prompt) in enumerate(SLIDES.items(), 1):
        print(f"[{i}/{total}] Generating {name}...", flush=True)
        if generate_image(name, prompt):
            success += 1
        else:
            failed.append(name)
        if i < total:
            time.sleep(3)

    print(f"\nDone: {success}/{total} images generated", flush=True)
    if failed:
        print(f"Failed: {', '.join(failed)}")
