#!/usr/bin/env python3
"""Generate narration audio + word timestamps for each slide via ElevenLabs API."""

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

API_KEY = os.environ.get("ELEVENLABS_API_KEY", "")
VOICE_ID = "onwK4e9ZLuTAKqWW03F9"  # Daniel - Steady Broadcaster, British
URL = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/with-timestamps"
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "slides")

NARRATIONS = {
    "slide-01": "The Sanhedrin Educational Experience. Disagree better. Discover together. What would history's greatest minds say about the dilemmas tearing our society apart right now? That is what we are building. And it is unlike anything that exists today.",

    "slide-02": "Here is the crisis. Discourse is broken. Young people literally walk out of rooms when they hear something they disagree with. Disagreement has become tribal. It triggers identity defense, not critical thinking. And here is the gap no one has filled: there is no civic discourse simulator. No place where society can train the muscle of sitting with discomfort. We are building that place.",

    "slide-03": "Now here is where everything shifts. We are not building another debate platform. We are reframing what a dispute even is. A dispute is not a battle to be won. It is a dynamic puzzle to be solved. Participants uncover hidden pieces, arguments, facts, points of agreement, to see the full picture. Demagoguery makes the picture blur. Depth makes it sharpen. The goal is shared truth-seeking. L'Shem Shamayim. For the sake of heaven.",

    "slide-04": "Our promise is simple. Learn to argue better in 30 minutes. Without needing to agree. This is an AI-powered immersive space where visitors step into real-time deliberation with 71 historical Jewish figures. A visitor brings a dilemma. Our engine, a mix of AI characters and human participants, deliberates together. And the output? Expanded thinking. New perspectives. A visitor who leaves sharper than when they walked in.",

    "slide-05": "Here is how the experience works. It is a tight 25-minute loop. Twelve visitors select a dilemma and lock in their initial confidence level. A human game master, think game show host, sets the stage. Then our Wheel of Sages dynamically assigns AI historical figures to join the teams. What follows is structured deliberation, arguments, questioning, and clarification. Midpoint check-ins track how perspectives actually shift. And at the end, every visitor walks out with a personalized digital summary of their journey.",

    "slide-06": "Now let me show you what is under the hood. This is not a chatbot. It is a modular role-based architecture layered over 13 Talmudic thinking modes. We do something no one else does: we separate the persona from the role. Rambam is a character. Facilitator is a function. Any persona can fill any role. Humans can swap in. AI can swap out. And running behind all of it, our system is actively fact-checking, filtering for cultural sensitivity, and tracking logical contradictions. In real time.",

    "slide-07": "Let me make this real for you. The Goring Ox. It is an ancient Talmudic case. We modernize it: who is liable when an autonomous vehicle kills someone? Is it the manufacturer? The owner? The software developer? The city that built the road? There is no right answer, and that is the point. Rambam analyzes systemic causation. Shammai challenges every assumption. Herzl envisions systemic solutions. And our research agent injects live crash statistics into the conversation as it unfolds.",

    "slide-08": "Now, we faced a real internal tension. One team wanted collaborative pedagogy. The other wanted competitive debate. Our solution? One platform, two configurations. Culture of Disagreement mode is pedagogical, process-focused, with a live polarization score and a L'Shem Shamayim index. Perfect for school groups. Debate mode is competitive, rhetorical, with structured rounds, opening statements, rebuttals, and audience voting. Perfect for general visitors and corporate groups. Same infrastructure. Two completely different experiences.",

    "slide-09": "The physical space. A circular civic discourse arena. Designed by Yazdani Studio. This is not a passive aquarium where people watch screens. Every single person in this room participates. Twelve interactive kiosks. Curved benches. Sage portrait screens that come alive. Dynamic spotlights. And the peripheral audience? They are actively voting, reacting, and engaging through their mobile devices. Zero bystanders.",

    "slide-10": "And here is why you should believe us. We already did this. The Rambam interactive exhibit at the museum is our proven sibling project. Micha Goodman, one of Israel's leading public intellectuals, tested our AI and validated its conversational depth. His reaction? Rambam was a monologue sold in one slide. Sanhedrin is a multi-agent dialogue. The next evolution. We are not starting from scratch. We are scaling a validated mechanism.",

    "slide-11": "Let me be transparent about where we stand. 70 percent solved. Agent quality, conversation protocols, character modeling of 68 historical figures, and our entire content framework: done. The remaining 30 percent is the hard part. Agent-to-agent-to-human orchestration. Getting AI characters to debate each other in the background while synthesizing coherent outputs for the human layer. That is the frontier. And we are proving it right now with a Phase 1 POC, a live multi-agent WhatsApp group testing real dynamics before we build the UI.",

    "slide-12": "Look at the competitive landscape. Chatbots give you one perspective. Museums give you passive exhibits. Debate AI gives you structured arguments. Nobody, nobody, combines multi-perspective dialogue with 5 to 7 characters, orchestrated meta-logic across 13 thinking modes, a physical immersive space, and institutional backing from the Museum of Tolerance Jerusalem. Our moat is not a new LLM. Our moat is integration. Agentic systems plus structured dispute methodology, combined in a way no one else has attempted.",

    "slide-13": "And this is bigger than a museum exhibit. This is the Debate Gym. A scalable EdTech platform. The museum is the premium peak experience. Schools run School of Civic Discourse programs with direct curriculum integration. And at home? Open your camera, speak, and get real-time AI analysis on your rhetoric and argumentation. Museum, school, home. Three tiers. One technology stack. Massive total addressable market.",

    "slide-14": "Here is the roadmap. Phase 1, right now: a WhatsApp-based proof of concept with 3 AI agents and 2 humans testing live agent-to-agent mechanics. Phase 2 at 3 months: a working text-based demo with 5 historical characters and full orchestrator logic. Phase 3 at 6 months: a complete experience prototype integrated with a physical space mockup. Phase 4 at 12 months: launch-ready deployment at the Museum of Tolerance Jerusalem, serving over 100,000 annual visitors.",

    "slide-15": "The business case. We need funding for tech architecture, content development, and spatial build-out. Revenue flows from four streams: museum admission with premium VIP tiers, content licensing, EdTech B2B subscriptions for schools, and here is the hidden gem: the system generates a privacy-first, anonymized data repository on how society reasons about moral questions. That data creates prestigious academic partnerships and a unique research asset that appreciates over time.",

    "slide-16": "The team. Jonathan leads tech architecture, the person who built the Rambam AI. Daniel drives project strategy and stakeholder management. Doron handles knowledge design and the creative layer. And there is one missing piece we need your help finding: a world-renowned debate content expert to mathematically design the competitive mode, the way Barry Lenny shaped the Rambam content.",

    "slide-17": "Two thousand years ago, the Sanhedrin did not give people answers. They gave people the tools to think. We are bringing that into the 21st century. Give us the green light. Fund the Phase 1 proof of concept. Let us prove the final 30 percent. And schedule the deep-dive technical review where we show you exactly how this works under the hood.",
}


def chars_to_words(text, char_starts, char_ends):
    """Convert character-level timings to word-level timings."""
    words = []
    current_word = ""
    word_start = None
    word_end = None

    for i, char in enumerate(text):
        if char == ' ' or char == '\n':
            if current_word:
                words.append({
                    "word": current_word,
                    "start": round(word_start, 4),
                    "end": round(word_end, 4)
                })
                current_word = ""
                word_start = None
        else:
            if not current_word:
                word_start = char_starts[i] if i < len(char_starts) else 0
            current_word += char
            word_end = char_ends[i] if i < len(char_ends) else word_start

    if current_word:
        words.append({
            "word": current_word,
            "start": round(word_start, 4),
            "end": round(word_end, 4)
        })

    return words


def generate_slide(slide_id, text, index, total):
    """Generate narration for a single slide. Returns True on success."""
    slide_dir = os.path.join(BASE_DIR, slide_id)
    os.makedirs(slide_dir, exist_ok=True)

    audio_path = os.path.join(slide_dir, "narration.mp3")
    timing_path = os.path.join(slide_dir, "timing.json")

    payload = json.dumps({
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.75
        }
    }).encode("utf-8")

    headers = {
        "xi-api-key": API_KEY,
        "Content-Type": "application/json"
    }

    req = Request(URL, data=payload, headers=headers, method="POST")

    t0 = time.time()
    try:
        with urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(f"  ERROR: HTTP {e.code} - {body[:200]}")
        return False
    except Exception as e:
        print(f"  ERROR: {e}")
        return False

    elapsed = round(time.time() - t0, 1)

    # Save audio
    audio_bytes = base64.b64decode(data["audio_base64"])
    with open(audio_path, "wb") as f:
        f.write(audio_bytes)

    # Convert character timings to word timings
    alignment = data.get("alignment", {})
    characters = alignment.get("characters", list(text))
    char_starts = alignment.get("character_start_times_seconds", [])
    char_ends = alignment.get("character_end_times_seconds", [])

    words = chars_to_words(text, char_starts, char_ends)

    # Calculate duration from last word end or last char end
    duration = 0.0
    if words:
        duration = round(words[-1]["end"], 2)
    elif char_ends:
        duration = round(char_ends[-1], 2)

    timing_data = {
        "words": words,
        "duration": duration
    }

    with open(timing_path, "w") as f:
        json.dump(timing_data, f, indent=2)

    print(f"[{index}/{total}] Generating {slide_id}... OK ({elapsed}s, {len(words)} words, {duration}s duration)")
    return True


def main():
    if not API_KEY:
        print("ERROR: ELEVENLABS_API_KEY not set. Add it to .env or export it.")
        sys.exit(1)

    total = len(NARRATIONS)
    success = 0
    failed = 0

    print(f"Generating narration for {total} slides...")
    print(f"Voice: Daniel (onwK4e9ZLuTAKqWW03F9)")
    print(f"Output: {BASE_DIR}/slide-NN/narration.mp3 + timing.json")
    print()

    for i, (slide_id, text) in enumerate(sorted(NARRATIONS.items()), 1):
        if generate_slide(slide_id, text, i, total):
            success += 1
        else:
            failed += 1

        # Rate limit: 2s between calls
        if i < total:
            time.sleep(2)

    print()
    print(f"Done. {success} succeeded, {failed} failed.")


if __name__ == "__main__":
    main()
