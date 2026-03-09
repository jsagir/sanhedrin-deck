#!/usr/bin/env python3
"""Generate hero images for Sanhedrin deck slides via Gemini API.
Style: Cinematic First-Person, Shallow DOF, Photorealistic Museum-Tech."""

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

SLIDES = {
    "slide-01": "Cinematic first-person view entering a dark, breathtaking museum exhibition space. In the center foreground, a warm walnut-wood interactive console glows with cyan data. Standing directly across the console is a hyper-realistic, life-sized translucent blue hologram of Maimonides holding a scroll, making eye contact with the camera. In the blurred background (bokeh), tiered seating and other holographic figures are visible. Dramatic museum spotlighting, anamorphic lens, 8k resolution, photorealistic, awe-inspiring.",

    "slide-02": "Cinematic over-the-shoulder shot of a modern teenager sitting on a dark bedroom floor, face illuminated entirely by the harsh, cold glare of a smartphone screen displaying angry red notification bubbles. The background is completely swallowed in dark, isolating shadows. Moody, dramatic lighting, portraying digital isolation and the toxicity of modern social media discourse. Photorealistic, highly emotional.",

    "slide-03": "Extreme macro close-up, cinematic photography. A human hand is interacting with a sleek, glowing frosted-glass touchscreen embedded in warm walnut wood. Under the glass, glowing golden digital puzzle pieces are snapping together. One puzzle piece contains ancient Hebrew text, another contains modern data graphs. Shallow depth of field, warm inviting lighting, tactile and highly detailed, representing the fusion of ancient wisdom and modern tech.",

    "slide-04": "Cinematic, low-angle shot looking up at five distinct, glowing holographic data-pillars in a dark, premium museum space. Inside each pillar is the faint, dignified silhouette of a different historical thinker. Beams of warm gold light connect the pillars to each other, representing Agent-to-Agent communication. Sleek, high-end corporate technology aesthetic, moody volumetric lighting, photorealistic, 8k.",

    "slide-05": "Cinematic first-person POV walking along a sleek, illuminated pathway through a dark museum corridor. Each section of the path is marked by glowing frosted-glass stations: a touchscreen kiosk, a human facilitator silhouette, holographic AI avatars deliberating, and a smartphone with a QR code. Dramatic museum lighting, shallow depth of field on the nearest station, warm walnut and brushed metal materials, photorealistic.",

    "slide-06": "Cinematic close-up of a sleek digital display showing a futuristic role-assignment interface. Translucent holographic portrait cards of historical figures are being dragged and dropped onto labeled role slots (Judge, Advocate, Questioner). The UI glows with cyan and warm gold accents on a dark background. Hands visible at the edge of frame interacting with the display. Premium museum-tech UX design, shallow DOF, photorealistic.",

    "slide-07": "Cinematic over-the-shoulder shot of a museum visitor looking at a large, sleek digital table. On the table, a glowing 3D hologram of a modern autonomous car is colliding with a hologram of an ancient ox. A translucent blue hologram of Golda Meir stands across the table, gesturing passionately toward the car. Floating UI text boxes hover in the air. High-end museum tech, interactive, dynamic lighting, photorealistic.",

    "slide-08": "Cinematic bird's-eye view of a sleek, dark museum exhibit table displaying a grid of glowing scenario cards. Each card shows a different ethical dilemma: an autonomous vehicle, a smartphone with speech bubbles, a DNA helix, scales of justice. A visitor's hands hover over the cards, about to select one. Warm walnut wood table surface, premium cyan and gold UI glow, dramatic museum lighting, photorealistic.",

    "slide-09": "Cinematic close-up from the perspective of an audience member sitting in the Sanhedrin tiered seating. In the foreground, hands are holding a sleek digital tablet displaying elegant voting buttons (Agree, Disagree, Need Clarification). In the blurred background (bokeh), a heated debate is happening in the glowing central pit between human participants and holographic avatars. Warm wood textures, premium UI design, immersive perspective.",

    "slide-10": "Cinematic wide-angle interior shot of the Sanhedrin circular museum room. Modern white and walnut curved benches with integrated glass touchscreens form a semi-circle. A minimalist facilitator podium stands center. Tall vertical frosted-glass Sage Screens flank a massive curved immersive projection wall showing a historical scene. Warm museum lighting, volumetric light rays, premium interior design, photorealistic, 8k.",

    "slide-11": "Cinematic split composition. Left side: a single ancient Hebrew scroll on a warm walnut pedestal, lit by a warm golden spotlight. Right side: the same scroll has transformed into a glowing, volumetric holographic figure of Maimonides speaking, surrounded by multiple smaller holographic figures in animated deliberation. The transition between old and new is marked by streaks of light. Museum lighting, emotional, photorealistic.",

    "slide-12": "Cinematic architectural visualization. A massive, gleaming white marble and brushed-steel structure fills the lower 70% of the frame, solid and imposing. The top 30% dissolves into a glowing cyan wireframe hologram being assembled by precise laser beams. The structure represents software architecture transitioning from proven foundation to cutting-edge development. Dramatic uplighting, dark background, corporate-tech aesthetic, photorealistic.",

    "slide-13": "Cinematic dramatic composition. In the center, a brilliant, multifaceted glass diamond tower glows with warm internal light, rotating slowly, surrounded by a protective ring of light. Scattered around the perimeter at a distance, basic gray cubic blocks sit unlit and inert, representing standard chatbots. The visual hierarchy is stark and immediate. Dark premium background, volumetric lighting, photorealistic, 8k.",

    "slide-14": "Cinematic split-screen montage. Left side: A high school student eagerly pointing at a smartboard displaying the Sanhedrin interface. Right side: A young professional at a coffee shop using a sleek laptop, interacting with a webcam while the screen shows AI feedback on their debate skills. Bright, optimistic lighting, lifestyle photography, showing the technology actively improving real lives.",

    "slide-15": "Cinematic upward-tracking shot of a grand spiral staircase made of frosted glass and brushed metal in a dark museum atrium. Each landing represents a development phase: a smartphone at the bottom, a laptop on the next level, a museum kiosk above, and at the summit a glowing miniature model of the circular Sanhedrin arena. Dramatic volumetric lighting from above, inspiring upward momentum, photorealistic.",

    "slide-16": "Cinematic close-up of a sleek, frosted-glass data visualization funnel in a dark premium space. Glowing cyan data particles stream into the top. At the base, the funnel splits into two elegant output streams: one producing golden coins (revenue), the other producing glowing holographic documents and research papers (intellectual property). Corporate-tech aesthetic, volumetric lighting, photorealistic.",

    "slide-17": "Cinematic low-angle shot of three solid, gleaming white marble pillars supporting a platform, dramatically lit from below. Next to them stands a fourth position marked only by a glowing cyan wireframe hologram outline of a pillar, pulsing gently, waiting to be filled. The scene represents a team with one missing expert. Dark museum background, dramatic shadows, architectural photography, photorealistic.",

    "slide-18": "Cinematic, emotional extreme close-up. A solid, warm human hand is reaching out and gently touching a glowing, translucent holographic hand made of floating cyan data particles. The point of contact creates a soft, brilliant burst of golden light. Dark background, hyper-detailed, symbolizing the perfect, harmonious connection between ancient human wisdom and future AI technology.",
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
