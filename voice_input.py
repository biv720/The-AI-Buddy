import speech_recognition as sr
from typing import Optional, Dict

def get_voice_input(
    language: str = "en-IN",
    timeout: int = 6,
    phrase_time_limit: int = 12,
    mic_index: Optional[int] = None,
    ambient_duration: float = 1.0,
    retries: int = 1
) -> Dict[str, Optional[str]]:
    """
    Capture speech from the default (or selected) microphone and return a structured result.

    Returns:
      {
        "success": bool,
        "transcript": str | None,
        "error": str | None
      }

    Parameters:
      language: language code for recognition (e.g. 'en-US', 'en-IN', 'hi-IN')
      timeout: seconds to wait for phrase to start (raises WaitTimeoutError if none)
      phrase_time_limit: max seconds for the phrase (prevents very long blocking listen)
      mic_index: optional microphone device index (useful when multiple mics are present)
      ambient_duration: seconds to adjust for ambient noise
      retries: number of times to retry on UnknownValueError (>=1)
    """
    recognizer = sr.Recognizer()

    mic_args = {}
    if mic_index is not None:
        mic_args["device_index"] = mic_index

    for attempt in range(1, retries + 1):
        try:
            with sr.Microphone(**mic_args) as source:
                recognizer.adjust_for_ambient_noise(source, duration=ambient_duration)
                print("🎤 Listening... (speak now)")

                audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)

            try:
                transcript = recognizer.recognize_google(audio, language=language)
                return {"success": True, "transcript": transcript, "error": None}
            except sr.UnknownValueError:
                if attempt < retries:
                    print(f"⚠️ Could not understand audio — retrying ({attempt}/{retries})...")
                    continue
                return {"success": False, "transcript": None, "error": "Could not understand audio."}
            except sr.RequestError as e:
                return {"success": False, "transcript": None, "error": f"API error: {e}"}

        except sr.WaitTimeoutError:
            return {"success": False, "transcript": None, "error": "Listening timed out — no speech detected."}
        except OSError as e:
            return {"success": False, "transcript": None, "error": f"Microphone error: {e}"}
        except Exception as e:
            return {"success": False, "transcript": None, "error": f"Unexpected error: {e}"}

    # fallback (shouldn't normally be reached)
    return {"success": False, "transcript": None, "error": "Failed to capture speech."}
