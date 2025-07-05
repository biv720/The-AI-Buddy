from gtts import gTTS
import re
import os
import uuid

def remove_emojis(text):
    emoji_pattern = re.compile(
        "["
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F1E0-\U0001F1FF"  # flags
        "\U00002500-\U00002BEF"  # Chinese characters
        "\U00002702-\U000027B0"
        "\U000024C2-\U0001F251"
        "]+", flags=re.UNICODE)
    return emoji_pattern.sub(r'', text)

def speak(text, lang='en'):
    clean_text = remove_emojis(text)
    filename = f"static/{uuid.uuid4().hex}.mp3"
    tts = gTTS(text=clean_text, lang=lang)
    tts.save(filename)
    return filename  # so Flask can serve it
