import speech_recognition as sr


class VoiceInput:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

        with self.microphone as source:
            print("Calibrating microphone for ambient noise...")
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Microphone ready.")

    def listen(self, timeout: int = None, phrase_time_limit: int = None) -> str | None:
        """
        Listen for voice input and convert to text.

        Args:
            timeout: Maximum seconds to wait for speech to start
            phrase_time_limit: Maximum seconds for a single phrase

        Returns:
            Transcribed text or None if recognition failed
        """
        try:
            with self.microphone as source:
                print("Listening...")
                audio = self.recognizer.listen(
                    source,
                    timeout=timeout,
                    phrase_time_limit=phrase_time_limit
                )

            print("Processing speech...")
            text = self.recognizer.recognize_google(audio)
            return text

        except sr.WaitTimeoutError:
            print("No speech detected within timeout.")
            return None
        except sr.UnknownValueError:
            print("Could not understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"Speech recognition service error: {e}")
            return None


def listen_once(timeout: int = None, phrase_time_limit: int = None) -> str | None:
    """
    Quick function to listen for a single voice input.

    Returns:
        Transcribed text or None if recognition failed
    """
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            print("Listening...")
            audio = recognizer.listen(
                source,
                timeout=timeout,
                phrase_time_limit=phrase_time_limit
            )

        print("Processing speech...")
        text = recognizer.recognize_google(audio)
        return text

    except sr.WaitTimeoutError:
        print("No speech detected.")
        return None
    except sr.UnknownValueError:
        print("Could not understand the audio.")
        return None
    except sr.RequestError as e:
        print(f"Speech recognition error: {e}")
        return None
