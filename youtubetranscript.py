from youtube_transcript_api import YouTubeTranscriptApi
import requests
import json

def get_transcript(youtube_url, languages=['en']):
    # Extract video ID from URL
    import re
    match = re.search(r'(?:v=|youtu\.be/)([A-Za-z0-9_-]{11})', youtube_url)
    if not match:
        raise ValueError("Invalid YouTube URL")
    video_id = match.group(1)
    
    # Fetch transcript
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
        return transcript
    except Exception as e:
        print(f"Error: {e}")
        return None


# This script will get the summary from the transcript of a youtube video and call ollama API (local) to summarize it.
def summarize_transcript(transcript, model="gemma:7b"):
    # Combine transcript text
    full_text = " ".join([entry['text'] for entry in transcript])
    prompt = f"Summarize the following YouTube transcript:\n\n{full_text}"
    print("Calling Ollama API...")
    # Call Ollama API
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": model,
            "prompt": prompt,
            "stream": False
        }
    )
    if response.status_code == 200:
        result = response.json()
        return result.get("response", "").strip()
    else:
        print(f"Ollama API error: {response.status_code} {response.text}")
        return None

if __name__ == "__main__":
    url = "https://youtube.com/watch?v=Hf9eemAnKHI"
    if not url:
        url = input("Enter YouTube URL (leave empty for default): ").strip()
    lang = ['en','ko']  # Change to desired language code(s), e.g., ['en', 'es']
    transcript = get_transcript(url, lang)
    
    summary = summarize_transcript(transcript)
    