#!/usr/bin/env python3
"""Generate hero images for Sanhedrin deck slides via Gemini API."""

import json, base64, sys, os, time
from urllib.request import Request, urlopen
from urllib.error import HTTPError

API_KEY = os.environ.get("GEMINI_API_KEY", "AIzaSyA5LvFesI77ctnUAKmvZ7jF-YzxlRKTTT0")
MODEL = "gemini-2.5-flash-image"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"
BASE_DIR = "/home/jsagi/sanhedrin-deck/slides"

SLIDES = {
    "slide-01": "High-end 3D isometric architectural visualization of a futuristic circular museum arena, isolated on a pure white background for easy cutout. In the center, a sleek brushed-aluminum and frosted glass digital console. Surrounding the console are life-sized, high-fidelity glowing blue holographic projections of historical figures. Semi-translucent architectural scale figures of modern visitors and one central facilitator stand around them. Two large vertical frosted-glass 'Sage Screens' flank a massive curved immersive display wall in the background. Warm walnut wood curved benches with integrated screens radiate outward. Premium corporate tech aesthetic, studio lighting, hyper-realistic, 8k.",

    "slide-02": "High-end 3D isometric conceptual illustration, isolated on a pure white background for easy cutout. A sleek, minimalist white platform split by a glowing, jagged red chasm. On opposite sides stand semi-translucent architectural scale figures. Above them, sleek frosted-glass speech bubbles collide and shatter into digital data fragments. Premium corporate tech aesthetic, stark contrast, dramatic but clean studio lighting, hyper-detailed.",

    "slide-03": "High-end 3D isometric conceptual illustration, isolated on a pure white background for easy cutout. A complex, glowing jigsaw puzzle assembling itself mid-air over a sleek matte-black and walnut wood pedestal. The puzzle pieces are made of frosted glass, emitting soft cyan and amber light, containing faint etchings of ancient text and data nodes. Premium museum-tech aesthetic, glassmorphism, crisp shadows, 8k.",

    "slide-04": "High-end 3D isometric infographic, isolated on a pure white background for easy cutout. A sleek technological flow: on the left, a minimalist data console. A crisp laser beam flows to the center, branching into 5 floating, frosted-glass geometric nodes representing AI minds. The beams converge on the right into an elegant, glowing wireframe sculpture of a human brain. Premium corporate tech aesthetic, cyan and gold data streams, minimalist.",

    "slide-05": "High-end 3D isometric architectural pathway, isolated on a pure white background for easy cutout. A path of floating, illuminated frosted-glass stepping stones. The stones feature sleek, minimalist dioramas: a modern touchscreen kiosk, a subtle human facilitator silhouette, glowing AI data nodes, and a sleek smartphone displaying a QR code. Connected by thin glowing fiber-optic lines. Premium museum-tech aesthetic, clean studio lighting.",

    "slide-06": "High-end 3D isometric infographic, isolated on a pure white background for easy cutout. A digital architecture matrix. At the base, identical sleek glass pedestals labeled with minimalist typography. Above them float highly detailed, translucent holographic busts of historical figures encased in sleek brushed-metal frames, actively slotting down onto the pedestals. Premium corporate tech aesthetic, glassmorphism, cyan and warm gold lighting.",

    "slide-07": "High-end 3D isometric diorama, isolated on a pure white background for easy cutout. A sleek, minimalist white museum display table. On the table, two highly detailed, contrasting 3D models: a modern matte-white autonomous vehicle, and an ancient pair of polished brass scales of justice. Elegant fiber-optic data beams connect them. Floating frosted-glass interface panels display ethical queries. Premium architectural visualization, 8k.",

    "slide-08": "High-end 3D isometric infographic, isolated on a pure white background for easy cutout. A sleek, floating frosted-glass timeline bar. Above the timeline, three illuminated glass spheres float, containing minimalist 3D icons: a car and an ox, a smartphone and an ancient scroll, a medical DNA helix. Below, minimalist digital clocks read 02:00, 15:00, 25:00. Premium corporate tech aesthetic, clean lighting, highly professional.",

    "slide-09": "High-end 3D isometric split-screen architectural diorama, isolated on a pure white background for easy cutout. Left side: a calm, collaborative seminar setup with warm walnut tables, soft blue lighting, and semi-translucent figures studying. Right side: a dynamic, sleek debate podium setup with brushed metal, subtle amber lighting, and figures facing off. Premium museum-tech aesthetic, hyper-realistic materials, studio lighting.",

    "slide-10": "High-end 3D isometric architectural visualization of a circular museum room, isolated on a pure white background for easy cutout. A wide semi-circle of modern white and walnut curved benches with sleek glass touchscreens. A minimalist facilitator podium in the center. Tall, vertical frosted-glass 'Sage Screens' flank a massive, curved immersive display wall. High-end interior design, premium lighting, 8k resolution.",

    "slide-11": "High-end 3D isometric conceptual illustration, isolated on a pure white background for easy cutout. On the left, a single glowing ancient scroll transitions into a sleek, volumetric hologram of a historical figure. Elegant, fiber-optic light trails expand outward to the right, forming a network of multiple interconnected holographic pedestals. Premium museum-tech aesthetic, blue to gold gradient, hyper-detailed, minimalist.",

    "slide-12": "High-end 3D isometric architectural metaphor, isolated on a pure white background for easy cutout. A massive, sleek structure. The bottom 70% is built from solid, highly polished white marble and brushed steel. The top 30% transitions into a glowing cyan wireframe hologram, being actively constructed by precise laser beams. Premium corporate tech aesthetic, clean shadows, representing software architecture.",

    "slide-13": "High-end 3D isometric conceptual illustration, isolated on a pure white background for easy cutout. In the center, an elegant, multifaceted glass diamond tower projects warm internal lighting, surrounded by a subtle glowing ring. Scattered around the perimeter are basic, matte-gray, unlit cubic blocks. Premium corporate tech aesthetic, visual hierarchy, hyper-realistic glassmorphism, 8k.",

    "slide-14": "High-end 3D isometric ecosystem map, isolated on a pure white background for easy cutout. Three sleek, floating minimalist dioramas connected by glowing fiber-optic bridges. Top: a premium museum exhibition dome. Bottom-left: a modern, high-tech academic classroom. Bottom-right: a sleek home office desk. Premium architectural visualization, warm wood and frosted glass materials, clean corporate lighting.",

    "slide-15": "High-end 3D isometric infographic, isolated on a pure white background for easy cutout. A sleek, upward-winding staircase made of frosted glass and brushed metal. Step 1: a minimalist smartphone. Step 2: a sleek laptop with data charts. Step 3: a premium museum touchscreen kiosk. Step 4 (top): a miniaturized, glowing architectural model of the circular Sanhedrin arena. Premium corporate tech aesthetic, inspiring upward momentum.",

    "slide-16": "High-end 3D isometric conceptual illustration, isolated on a pure white background for easy cutout. An elegant, minimalist data funnel made of frosted glass. Glowing cyan data particles flow into the top. The funnel splits the output into two streams at the base: sleek, stylized gold coins, and floating, holographic academic documents. Premium corporate tech aesthetic, hyper-realistic materials, studio lighting.",

    "slide-17": "High-end 3D isometric architectural metaphor, isolated on a pure white background for easy cutout. Three solid, premium pillars made of polished white marble and brushed aluminum supporting a sleek platform. Next to them stands a fourth pillar that is an empty, glowing cyan wireframe hologram, representing a missing piece waiting to be filled. Premium corporate tech aesthetic, crisp shadows, minimalist.",

    "slide-18": "High-end 3D isometric conceptual illustration, isolated on a pure white background for easy cutout. Two highly realistic, elegant hands meeting over a sleek matte-black pedestal. One hand is slightly translucent, made of warm, amber holographic light (ancient wisdom). The other is a solid, modern human hand. Between their fingers, a brilliant, clean spark of blue and white light. Premium museum-tech aesthetic, emotional but highly professional.",
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
