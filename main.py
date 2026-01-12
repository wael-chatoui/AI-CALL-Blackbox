#!/usr/bin/env python3
"""
Screen AI Assistant - A voice-controlled AI that can see your screen.

Usage:
    1. Create a .env file with your BLACKBOX_API_KEY
    2. Run: python main.py
    3. Speak your question when prompted
    4. Say "exit" or "quit" to stop
"""

import sys
from voice_input import VoiceInput
from screen_capture import capture_screen
from blackbox_api import chat_with_screen
from text_to_speech import TextToSpeech
from config import BLACKBOX_API_KEY


def main():
    print("=" * 50)
    print("  Screen AI Assistant")
    print("  Powered by Blackbox AI")
    print("=" * 50)
    print()

    if not BLACKBOX_API_KEY:
        print("ERROR: No API key found!")
        print("Please create a .env file with:")
        print("  BLACKBOX_API_KEY=your_api_key_here")
        sys.exit(1)

    print("Initializing voice input...")
    voice = VoiceInput()

    print("Initializing text-to-speech...")
    tts = TextToSpeech(rate=170)

    print()
    print("Ready! Speak your question about the screen.")
    print("Say 'exit' or 'quit' to stop.")
    print("-" * 50)

    tts.speak("Screen AI Assistant ready. Ask me anything about your screen.")

    while True:
        try:
            question = voice.listen(timeout=10, phrase_time_limit=15)

            if question is None:
                continue

            print(f"You said: {question}")

            lower_question = question.lower().strip()
            if lower_question in ["exit", "quit", "stop", "goodbye", "bye"]:
                print("Goodbye!")
                tts.speak("Goodbye!")
                break

            print("Capturing screen...")
            screenshot = capture_screen()

            print("Asking AI...")
            response = chat_with_screen(question, screenshot)

            print(f"\nAI: {response}\n")
            print("-" * 50)

            tts.speak(response)

        except KeyboardInterrupt:
            print("\nInterrupted by user.")
            tts.speak("Goodbye!")
            break
        except Exception as e:
            print(f"Error: {e}")
            tts.speak("Sorry, an error occurred. Please try again.")


if __name__ == "__main__":
    main()
