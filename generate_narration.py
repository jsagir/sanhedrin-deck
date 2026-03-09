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
VOICE_ID = "onwK4e9ZLuTA"  # Daniel - Steady Broadcaster, British
URL = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}/with-timestamps"
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "slides")

NARRATIONS = {
    "slide-01": "The Sanhedrin Educational Experience. Disagree better. Discover together. What would history's greatest minds say about today's dilemmas?",

    "slide-02": "Discourse is broken. We live in a polarized society where young people walk out of rooms when exposed to opposing views. I disagree with you has become synonymous with tribal identity defense. Currently, there is no civic discourse simulator to train society on how to navigate complex, emotionally charged issues.",

    "slide-03": "We are reframing the concept of a dispute. It is no longer a battle to be won, but a collaborative investigation. Participants uncover hidden puzzle pieces to see the full picture. The ultimate goal is shared truth-seeking, for the sake of heaven.",

    "slide-04": "Learn to argue better in 30 minutes. Without needing to agree. An AI-powered immersive space where visitors engage with 71 historical Jewish figures in real-time deliberation. The input is a human dilemma. The engine is AI characters and humans deliberating together. The output is expanded thinking and new perspectives.",

    "slide-05": "The visitor journey is a 25-minute loop. Up to 12 visitors select a dilemma and set their confidence level. A human game master sets the stage. The Wheel of Sages assigns AI historical figures to join the teams. AI and humans engage through structured rounds of arguments. Midpoint check-ins track how perspectives shift. Finally, visitors receive a personalized digital summary.",

    "slide-06": "This is not a standard chatbot array. It utilizes a modular role-based architecture layered over 13 Talmudic thinking modes. We separate the character from the system function. A persona can step into different roles depending on the session's needs. The system actively fact-checks, filters for cultural sensitivity, and tracks logical contradictions in real-time.",

    "slide-07": "The Goring Ox. We modernize the ancient Talmudic case into today's reality. Who is liable when an autonomous vehicle causes a fatal accident? Rambam analyzes systemic causation. Shammai challenges liability assumptions. Herzl envisions future solutions. The research agent injects real-time crash statistics into the dialogue.",

    "slide-08": "One platform. Two configurations. Culture of Disagreement is pedagogical, process-focused, and collaborative, with a polarization score and L'Shem Shamayim index. Ideal for school groups. Debate mode is competitive, outcome-focused, and rhetorical, with structured rounds and audience voting. Ideal for general visitors and corporate groups.",

    "slide-09": "The physical space. A circular civic discourse arena designed by Yazdani Studio. Not a passive aquarium. Every person in the room participates. 12 interactive kiosks, curved benches, sage portrait screens, and dynamic spotlights.",

    "slide-10": "We already did this. The Rambam interactive exhibit is our proven sibling project. Expert Micha Goodman validated the conversational quality and depth of our AI model. Rambam was a monologue. Sanhedrin is a multi-agent dialogue. The next evolution. We are scaling a validated mechanism, not starting from scratch.",

    "slide-11": "70 percent solved. 30 percent ahead. Individual agent quality, conversation protocols, character modeling of 68 figures, and the core content framework are established. What remains is A2A2H orchestration, getting AI agents to debate each other while synthesizing outputs for human interaction. We are proving this now via a Phase 1 proof of concept using a multi-agent WhatsApp group.",

    "slide-12": "Competitive advantage. Multi-perspective dialogue with 5 to 7 characters. No single right answer. Orchestrated meta-logic across 13 thinking modes. A physical immersive space. And institutional backing from the Museum of Tolerance Jerusalem. The moat is clear. The innovation is in integrating agentic systems with structured dispute methodology.",

    "slide-13": "The EdTech platform play. The Debate Gym. This is not just a museum exhibit. It is a scalable education technology ecosystem. The museum provides the premium immersive experience. Schools run School of Civic Discourse programs with direct curriculum integration. And at home, an async platform provides AI analysis on your rhetoric and argumentation.",

    "slide-14": "Roadmap and milestones. Phase 1, happening now: a WhatsApp group proof of concept with 3 agents and 2 humans. Phase 2 at 3 months: a working text-based demo with 5 historical characters. Phase 3 at 6 months: a full experience prototype with physical space mockup. Phase 4 at 12 months: launch-ready deployment for over 100,000 annual visitors.",

    "slide-15": "The business case. Funding is required for tech architecture, content development, and spatial build-out. Revenue comes from museum admission, premium VIP tiers, licensing, and EdTech B2B subscriptions. The system also creates a privacy-first, anonymized data repository on societal moral reasoning, establishing prestigious academic partnerships.",

    "slide-16": "The team. Jonathan leads tech architecture. Daniel drives project strategy. Doron handles knowledge and design. And the missing piece: a world-renowned debate content expert to help design the competitive mode.",

    "slide-17": "The Sanhedrin didn't give answers. They gave people the tools to think. We're bringing that to the 21st century. Give us the green light to move past the 70 percent mark, fund the Phase 1 proof of concept, and schedule the deep-dive technical review.",
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
    print(f"Voice: Daniel (onwK4e9ZLuTA)")
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
