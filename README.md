# OpenAI Whisper Transcription

This project demonstrates how to create a transcription from an audio file using OpenAI's Whisper model.

## Transcription Process

The transcription process involves using OpenAI's Whisper model to convert speech from an audio file into text. The `transcribe.py` script handles this process by loading the audio file and creating a transcription using the Whisper model.

## Dependencies

The following dependencies are required for this project:
- `openai`
- `pyaudio`

These dependencies are listed in the `requirements.txt` file.

## Usage Instructions

To run the transcription script, follow these steps:

1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set the `OPENAI_API_KEY` environment variable:
   ```bash
   export OPENAI_API_KEY='your_openai_api_key'
   ```

3. Run the transcription script:
   ```bash
   python transcribe.py
   ```

The script requires the `OPENAI_API_KEY` to be set in order to work. The script will print the transcription text to the console.
