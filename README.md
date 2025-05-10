# YouTube Transcript Summarizer

A Python script that fetches YouTube video transcripts and generates summaries using the Ollama API.

## Features

- Extracts transcripts from YouTube videos using video URL
- Supports multiple languages (default: English and Korean)
- Generates summaries using local Ollama # LLM Lab Tools

A collection of Python scripts for working with language and speech processing.

## Features

### 1. YouTube Transcript Summarizer
- Extracts transcripts from YouTube videos using video URL
- Supports multiple languages (default: English and Korean)
- Generates summaries using local Ollama API
- Uses Gemma 3 12B model by default

### 2. Text-to-Speech Converter
- Converts text to natural-sounding speech using Coqui TTS
- Supports multiple TTS models and languages
- Includes audio recording capabilities
- Saves output in WAV format

## Prerequisites

- Python 3.x
- Required Python packages:
  ```bash
  pip install youtube-transcript-api requests TTS torch sounddevice scipy numpy
  ```
- Ollama API running on `localhost:11434` (for transcript summarizer)

## Usage

### YouTube Transcript Summarizer
1. Run the script:
   ```bash
   python youtubetranscript.py
   ```
2. Enter a YouTube URL when prompted

### Text-to-Speech Converter
1. Run the script:
   ```bash
   python texttospeech.py
   ```
2. Enter the text you want to convert to speech
3. Check the generated `output.wav` file

## Configuration

### YouTube Transcript Summarizer
- Change language preferences by modifying the `lang` list
- Adjust the model by changing the `model` parameter
- Default model: `gemma3:12b`

### Text-to-Speech
- Default sample rate: 22050 Hz
- Default recording duration: 5 seconds
- Model: `tts_models/en/ljspeech/glow-tts`

## Error Handling

The scripts include error handling for:
- Invalid YouTube URLs
- Transcript fetch failures
- Ollama API connection issues
- Audio device errors
- Text-to-speech conversion failuresAPI
- Uses Gemma 3 12B model by default

## Prerequisites

- Python 3.x
- Ollama running locally
- Required Python packages:
  ```bash
  pip install youtube-transcript-api requests
  ```
- Ollama API running on `localhost:11434`

## Usage

1. Run the script:
   ```bash
   python youtubetranscript.py
   ```

2. Enter a YouTube URL when prompted

3. The script will:
   - Fetch the video transcript
   - Generate a summary using Ollama
   - Display the summary

## Configuration

- Change language preferences by modifying the `lang` list in the script
- Adjust the model by changing the `model` parameter in `summarize_transcript()`
- Default model: `gemma3:12b`

## Error Handling

The script includes error handling for:
- Invalid YouTube URLs
- Transcript fetch failures
- Ollama API connection issues
