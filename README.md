# YouTube Transcript Summarizer

A Python script that fetches YouTube video transcripts and generates summaries using the Ollama API.

## Features

- Extracts transcripts from YouTube videos using video URL
- Supports multiple languages (default: English and Korean)
- Generates summaries using local Ollama API
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
