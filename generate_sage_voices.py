#!/usr/bin/env python3
"""Generate sage voice clips using ElevenLabs TTS API."""

import os
import time
from pathlib import Path
from dotenv import load_dotenv
from elevenlabs import ElevenLabs

load_dotenv()

client = ElevenLabs(api_key=os.getenv("ELEVENLABS_API_KEY"))

OUTPUT_DIR = Path("audio/sages")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

SAGES = [
    {
        "name": "abraham",
        "voice_id": "nPczCjzI2devNBz1zQrb",
        "stability": 0.7,
        "similarity_boost": 0.8,
        "text": "I am Abraham. I was chosen because I broke my father's idols before I built anything of my own. In this council, I challenge every inherited assumption. I force you to question what you take for granted. So tell me: what if everything your fathers taught you is wrong?"
    },
    {
        "name": "maimonides",
        "voice_id": "VXFdnKU6k5XRvwf2xfEY",
        "stability": 0.75,
        "similarity_boost": 0.8,
        "text": "I am Maimonides. I unified Aristotelian logic with Torah law, and I bring that same rigor here. In the Sanhedrin, I classify, I systematize, I cut through confusion to find the underlying structure. There are exactly four categories, and here they are."
    },
    {
        "name": "herzl",
        "voice_id": "onwK4e9ZLuTAKqWW03F9",
        "stability": 0.6,
        "similarity_boost": 0.75,
        "text": "I am Herzl. They called me a dreamer, but I built a state from a pamphlet. In this council, I generate radical new possibilities when others see only deadlock. If you will it, it is no dream."
    },
    {
        "name": "golda-meir",
        "voice_id": "RILOU7YmBhvwJGDGjNmP",
        "stability": 0.65,
        "similarity_boost": 0.8,
        "text": "I am Golda. I speak for collective fate, not personal interest. In every deliberation, I ask: what does this mean for our people? Not for me, not for you, for all of us. We have no one else."
    },
    {
        "name": "einstein",
        "voice_id": "pqHfZKP75CvOlQylNhV4",
        "stability": 0.4,
        "similarity_boost": 0.7,
        "text": "I am Einstein. I propose thought experiments that reframe the entire discussion. I take your fixed assumptions and I ask: what if they are wrong? What if the very thing you are certain of is the thing preventing you from seeing clearly? Imagine everything you assume is wrong."
    },
    {
        "name": "anne-frank",
        "voice_id": "cgSgspJ2msm6clMCkdW9",
        "stability": 0.35,
        "similarity_boost": 0.75,
        "text": "I am Anne Frank. I remind the council that grand principles are lived in small daily moments. I do not argue from theory. I testify from experience. I still believe people are good. But let me tell you what I saw."
    },
    {
        "name": "houdini",
        "voice_id": "N2lVS1w4EtoT3dr4eOWO",
        "stability": 0.4,
        "similarity_boost": 0.7,
        "text": "I am Houdini. No cage can hold a determined mind, and no framework is as solid as it appears. My role in the Sanhedrin is to find the hidden exit, the trick door, the constraint everyone else accepts. What the eyes see and the ears hear, the mind believes."
    },
    {
        "name": "moses",
        "voice_id": "pNInz6obpgDQGcFmaJgB",
        "stability": 0.8,
        "similarity_boost": 0.85,
        "text": "I am Moses. I did not choose this role. I was chosen. In this council, I translate values into actionable statutes. I cut through abstraction to ask: what is the law? That is the principle. Now here is the statute."
    },
    {
        "name": "freud",
        "voice_id": "JBFqnCBsd6RMkjVDRZzb",
        "stability": 0.6,
        "similarity_boost": 0.8,
        "text": "I am Sigmund Freud. What you think you believe is not what drives you. My role in this council is to expose hidden motivations, the fears beneath the arguments, the desires behind the positions. Before you insist on your reasons, let us examine your resistance."
    },
]


def generate_voice(sage, max_retries=3):
    """Generate a single sage voice clip."""
    output_path = OUTPUT_DIR / f"{sage['name']}.mp3"

    # Skip if already generated
    if output_path.exists() and output_path.stat().st_size > 0:
        print(f"  SKIP {sage['name']} (already exists: {output_path.stat().st_size} bytes)")
        return True

    for attempt in range(max_retries):
        try:
            print(f"  Generating {sage['name']} (attempt {attempt + 1})...")
            audio_generator = client.text_to_speech.convert(
                voice_id=sage["voice_id"],
                text=sage["text"],
                model_id="eleven_multilingual_v2",
                voice_settings={
                    "stability": sage["stability"],
                    "similarity_boost": sage["similarity_boost"],
                },
            )

            # Write audio chunks to file
            with open(output_path, "wb") as f:
                for chunk in audio_generator:
                    f.write(chunk)

            size = output_path.stat().st_size
            if size < 1000:
                print(f"  WARNING: {sage['name']} file suspiciously small ({size} bytes)")
                output_path.unlink()
                continue

            print(f"  OK {sage['name']} ({size:,} bytes)")
            return True

        except Exception as e:
            error_msg = str(e)
            print(f"  ERROR {sage['name']}: {error_msg}")
            if "429" in error_msg or "rate" in error_msg.lower():
                wait = 2 ** (attempt + 1)
                print(f"  Rate limited, waiting {wait}s...")
                time.sleep(wait)
            elif attempt < max_retries - 1:
                time.sleep(1)

    print(f"  FAILED {sage['name']} after {max_retries} attempts")
    return False


def main():
    print(f"Generating {len(SAGES)} sage voice clips...")
    print(f"Output: {OUTPUT_DIR.resolve()}\n")

    success = 0
    failed = 0
    for sage in SAGES:
        if generate_voice(sage):
            success += 1
        else:
            failed += 1
        # Brief pause between API calls
        time.sleep(0.5)

    print(f"\nDone: {success} succeeded, {failed} failed")
    if failed:
        print("Re-run the script to retry failed generations.")


if __name__ == "__main__":
    main()
