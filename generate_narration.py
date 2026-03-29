#!/usr/bin/env python3
"""Generate slide narration MP3s using ElevenLabs TTS API.

22 main slides (new deck structure), presenter-style narration (~15-20s each).
Uses eleven_multilingual_v2 model. Output: audio/narration/slide-NN.mp3
"""

import os
import time
from pathlib import Path
from dotenv import load_dotenv
from elevenlabs import ElevenLabs

load_dotenv()

client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

OUTPUT_DIR = Path("audio/narration")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# Daniel voice - Steady Broadcaster, same as original narration
NARRATOR_VOICE_ID = "onwK4e9ZLuTAKqWW03F9"

# 22 main slides in new deck order (no narration for appendices)
SLIDES = [
    {
        "file": "slide-01.mp3",
        "text": "The Sanhedrin Educational Experience. Disagree better. Discover together. What would history's greatest minds say about the dilemmas tearing our society apart? That is what we are building at the Museum of Tolerance Jerusalem. And it is unlike anything that exists today."
    },
    {
        "file": "slide-02.mp3",
        "text": "Discourse is broken. Young people literally walk out of rooms when they hear something they disagree with. Disagreement has become tribal. It triggers identity defense, not critical thinking. There is no civic discourse simulator. No place where society can train the muscle of sitting with discomfort. We are building that place."
    },
    {
        "file": "slide-03.mp3",
        "text": "Meet the core MOTJ team. Daniel Muller, PhD in Planning and Decision-Making in AI. Technology executive and CTO of the Museum of Tolerance Jerusalem and MileZero, with 18 years of R&D experience including 12 years in AI. Jonathan Sagir, MBA, project operations and coordination. Marla Supnick, creative director and visitor experience lead. And Sharon Jacobson, director of design and content."
    },
    {
        "file": "slide-04.mp3",
        "text": "Our academic partner: Bar-Ilan University. Professor Jonathan Schler brings deep NLP and computational linguistics expertise. Dr. Alex Tal contributes research in digital humanities and AI ethics. Together, they ground our approach in rigorous academic methodology."
    },
    {
        "file": "slide-05.mp3",
        "text": "Our advisory team. Dr. Micha Goodman, bestselling author and public intellectual, serves as content and philosophical advisor. Lieutenant Colonel Miri Dayan, retired, is the principal of the School of Civic Discourse and developed much of the foundational learning methodology we build upon."
    },
    {
        "file": "slide-06.mp3",
        "text": "The cognitive twist. We reframe dispute not as conflict, but as a dynamic puzzle. The Talmudic tradition treated disagreement as a structured intellectual exercise. Our system transforms confrontation into collaborative discovery. L'Shem Shamayim: for the sake of heaven."
    },
    {
        "file": "slide-07.mp3",
        "text": "Discourse Training. Train how to disagree better. This is an AI-mediated civic discourse arena where visitors deliberate with 80 historical thinkers in real time. The flow: a structured dilemma goes in. Multi-agent deliberation happens, with Rambam, Einstein, Golda Meir and 77 more debating together. And what comes out: expanded thinking and new perspectives."
    },
    {
        "file": "slide-08.mp3",
        "text": "The thinkers behind the Sanhedrin. 80 historical figures from the Jewish Lives series by Yale University Press. From Abraham to Einstein, Maimonides to Golda Meir, Spinoza to Houdini. Each sage brings a distinct thinking mode and deliberative role to the council. Click any card to hear them speak."
    },
    {
        "file": "slide-09.mp3",
        "text": "The visitor journey: a tight 25-minute loop. Choose a pre-selected dilemma. Meet your sage panel. Engage in structured deliberation. Hear counterarguments. Reach synthesis. Reflect on what shifted. All dilemmas are supra-moral, non-political."
    },
    {
        "file": "slide-10.mp3",
        "text": "Role-based architecture. We separate persona from role. Rambam is a character. Facilitator is a function. Any persona can fill any role. Three visitor personas encounter sages playing Sanhedrin roles: Nasi, Av Beit Din, Ipcha Mistabra, Praklit Satan. Authentic Talmudic deliberation, powered by modern AI."
    },
    {
        "file": "slide-11.mp3",
        "text": "A sample session: The Goring Ox. An ancient Talmudic case, modernized. Who is liable when an autonomous vehicle causes harm? Maimonides systematizes. Golda Meir advocates for the collective. Einstein reframes every assumption. Watch perspectives shift in real time."
    },
    {
        "file": "slide-12.mp3",
        "text": "One platform, two configurations. Culture of Disagreement mode: pedagogical, process-focused, with a live polarization score. Perfect for school groups. Debate mode: competitive, structured rounds, opening statements, rebuttals, audience voting. Perfect for general visitors and corporate groups. Same infrastructure, two different experiences."
    },
    {
        "file": "slide-13.mp3",
        "text": "The physical space. A circular civic discourse arena. Twelve interactive kiosks. Central display for live sentiment analysis and argument visualization. Curved benches. Dynamic spotlights. Every person in this room participates. Zero bystanders."
    },
    {
        "file": "slide-14.mp3",
        "text": "AI and context engineering. Under the hood: retrieval-augmented generation grounds each sage in their actual writings. Multi-agent orchestration enables debate dynamics between agents. Context engineering manages the weights: what each agent knows, remembers, and responds to in real time."
    },
    {
        "file": "slide-15.mp3",
        "text": "The debate and discourse framework. Two distinct engagement mechanics power the system. Culture of Disagreement: pedagogical, collaborative. State the opponent's case first, concede gray areas, ground in practice. Debate Mode: competitive, rhetorical. Win the argument, challenge premises, score points through logic and evidence. Same system, two fundamentally different cognitive architectures. Each sage carries 13 Talmudic thinking modes, from Ipkha Mistabra to Shakla Vetarya."
    },
    {
        "file": "slide-16.mp3",
        "text": "We already did this. The Rambam exhibit at the Museum of Tolerance is our proven sibling project. Visitors engaged with a single AI sage and the response was overwhelming. Rambam is a conversation. Sanhedrin is an orchestration. Rambam was built on an edge stack. We figured out how to connect components that were not connected before into a coherent experience, both digital and physical. We are not starting from scratch. We are scaling a validated mechanism."
    },
    {
        "file": "slide-17.mp3",
        "text": "Transparent risk assessment. 70 percent solved: agent quality, protocols, 80 characters, and the core framework. 30 percent ahead: agent-to-agent-to-human orchestration. We mitigate this with a Phase 1 proof of concept, a WhatsApp group testing live multi-agent dynamics before we build the full UI."
    },
    {
        "file": "slide-18.mp3",
        "text": "Why not just use ChatGPT? A chatbot gives you one voice, one perspective, generic responses. The Sanhedrin gives you a council of distinct thinkers with authentic viewpoints, dual engagement mechanics across two modes, and real cognitive challenge. Nobody combines multi-perspective dialogue with orchestrated meta-logic across 13 thinking modes, a human facilitation layer, and a physical immersive space with institutional backing."
    },
    {
        "file": "slide-19.mp3",
        "text": "EdTech platform and business model. Beyond the museum: a debate gym for schools, universities, and home learners. Museum, school, home. Three tiers, one technology stack. The business model: our 80 sage personas, discourse methodology, and frameworks generate licensable intellectual property. A privacy-first research hub produces publishable data on moral reasoning through academic partnerships. Massive total addressable market expanding from museum visitors to the global education sector."
    },
    {
        "file": "slide-20.mp3",
        "text": "Roadmap and milestones. Internal presentation and stakeholder alignment by end of March. Donor presentations, RFP, and vendor selection in April and May, with K1 through K4 content authoring starting. Proof of concept from June to August: a WhatsApp group with 3 AI agents and 2 humans, both modes tested, validated by Micha Goodman. Working demo from September to November: custom React UI, 5 Sages plus Nasi and Av Beit Din, voice for 2 to 3 Sages, and an AI talking portrait prototype. Museum deployment in June to July 2027 with physical space build-out, AV integration, and live launch."
    },
    {
        "file": "slide-21.mp3",
        "text": "The ask. Investment required. The full scope financial projection is being finalized based on our version 3.1 implementation architecture and vendor quotes. This covers tech architecture, content development, AV build-out, and physical space construction. The detailed architecture proposal is available in the appendix."
    },
    {
        "file": "slide-22.mp3",
        "text": "In Judaism, disagreement was never the problem. It was always the method. Every tradition that changed the world didn't silence its arguments. It sanctified them. Judaism didn't just tolerate disagreement. It institutionalized it, ritualized it, and built a 2,000 year body of wisdom on top of it. That ancient technology went dormant. The Museum of Tolerance Jerusalem just switched it back on."
    },
]


def generate_narration(slide, max_retries=3):
    """Generate a single slide narration clip."""
    output_path = OUTPUT_DIR / slide["file"]

    # Skip if already generated
    if output_path.exists() and output_path.stat().st_size > 0:
        print(f"  SKIP {slide['file']} (already exists: {output_path.stat().st_size} bytes)")
        return True

    for attempt in range(max_retries):
        try:
            print(f"  Generating {slide['file']} (attempt {attempt + 1})...")
            audio_generator = client.text_to_speech.convert(
                voice_id=NARRATOR_VOICE_ID,
                text=slide["text"],
                model_id="eleven_multilingual_v2",
                voice_settings={
                    "stability": 0.3,
                    "similarity_boost": 0.85,
                },
            )

            # Write audio chunks to file
            with open(output_path, "wb") as f:
                for chunk in audio_generator:
                    f.write(chunk)

            size = output_path.stat().st_size
            if size < 1000:
                print(f"  WARNING: {slide['file']} suspiciously small ({size} bytes)")
                output_path.unlink()
                continue

            print(f"  OK {slide['file']} ({size:,} bytes)")
            return True

        except Exception as e:
            error_msg = str(e)
            print(f"  ERROR {slide['file']}: {error_msg}")
            if "429" in error_msg or "rate" in error_msg.lower():
                wait = 2 ** (attempt + 1)
                print(f"  Rate limited, waiting {wait}s...")
                time.sleep(wait)
            elif attempt < max_retries - 1:
                time.sleep(1)

    print(f"  FAILED {slide['file']} after {max_retries} attempts")
    return False


def main():
    print(f"Generating {len(SLIDES)} slide narration clips...")
    print(f"Voice: Daniel ({NARRATOR_VOICE_ID})")
    print(f"Output: {OUTPUT_DIR.resolve()}\n")

    success = 0
    failed = 0
    for slide in SLIDES:
        if generate_narration(slide):
            success += 1
        else:
            failed += 1
        # Brief pause between API calls
        time.sleep(1)

    print(f"\nDone: {success} succeeded, {failed} failed")
    if failed:
        print("Re-run the script to retry failed generations.")


if __name__ == "__main__":
    main()
