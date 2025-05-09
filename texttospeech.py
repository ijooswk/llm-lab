import torch
from TTS.api import TTS
import sounddevice as sd
import numpy as np
from scipy.io import wavfile
import os

# pip install TTS
# pip install torch
# pip install sounddevice scipy numpy

class TextToSpeech:
    def __init__(self):
        """Initialize TTS engine"""
        # List available models
        print("Available models:", TTS().list_models())
        # Initialize TTS with a specific model
        self.tts = TTS(model_name="tts_models/en/ljspeech/glow-tts")
        self.sample_rate = 22050  # Default sample rate for TTS
        self.duration = 5

    def text_to_speech(self, text, output_file="output.wav"):
        """Convert text to speech and save to file"""
        try:
            # Generate speech from text
            self.tts.tts_to_file(text=text, file_path=output_file)
            return True
        except Exception as e:
            print(f"Error in text to speech conversion: {e}")
            return False

    def record_audio(self):
        """Record audio from microphone"""
        print("Recording...")
        audio = sd.rec(
            int(self.duration * self.sample_rate),
            samplerate=self.sample_rate,
            channels=1,
            dtype=np.int16
        )
        sd.wait()
        return audio

    def save_audio(self, audio, filename="recorded.wav"):
        """Save audio to WAV file"""
        wavfile.write(filename, self.sample_rate, audio)

def main():
    # Initialize TTS engine
    tts = TextToSpeech()
    
    # Test text-to-speech
    text = input("Enter text to convert to speech: ")
    if tts.text_to_speech(text):
        print(f"Speech generated successfully! Check output.wav")
    

if __name__ == "__main__":
    main()