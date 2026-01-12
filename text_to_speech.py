import pyttsx3


class TextToSpeech:
    def __init__(self, rate: int = 150, volume: float = 1.0):
        """
        Initialize the text-to-speech engine.

        Args:
            rate: Speech rate (words per minute)
            volume: Volume level (0.0 to 1.0)
        """
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", rate)
        self.engine.setProperty("volume", volume)

        voices = self.engine.getProperty("voices")
        if voices:
            self.engine.setProperty("voice", voices[0].id)

    def speak(self, text: str):
        """
        Convert text to speech and play it.

        Args:
            text: The text to speak
        """
        if not text:
            return

        self.engine.say(text)
        self.engine.runAndWait()

    def set_voice(self, voice_index: int):
        """
        Change the voice.

        Args:
            voice_index: Index of the voice to use
        """
        voices = self.engine.getProperty("voices")
        if voices and 0 <= voice_index < len(voices):
            self.engine.setProperty("voice", voices[voice_index].id)

    def list_voices(self) -> list:
        """
        List all available voices.

        Returns:
            List of voice names
        """
        voices = self.engine.getProperty("voices")
        return [voice.name for voice in voices] if voices else []


def speak(text: str, rate: int = 150):
    """
    Quick function to speak text.

    Args:
        text: Text to speak
        rate: Speech rate
    """
    engine = pyttsx3.init()
    engine.setProperty("rate", rate)
    engine.say(text)
    engine.runAndWait()
