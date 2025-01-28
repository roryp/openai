#!/usr/bin/env rye run python

import time
from pathlib import Path

from openai import OpenAI

# gets OPENAI_API_KEY from your environment variables
openai = OpenAI()

speech_file_path = Path(__file__).parent / "Tech_Feature_Using_AI_to_find_work_-life_balance_in_2025_pt_2.mp3"


def main() -> None:

    # Create transcription from audio file
    transcription = openai.audio.transcriptions.create(
        model="whisper-1",
        file=speech_file_path,
    )
    print(transcription.text)


if __name__ == "__main__":
    main()