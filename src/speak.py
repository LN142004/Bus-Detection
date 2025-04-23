from gtts import gTTS
import os

def speak(text, filename="detected_number.mp3"):
    os.makedirs("output", exist_ok=True)
    path = os.path.join("output", filename)
    tts = gTTS(text=text, lang='en')
    tts.save(path)
    return path  # <--- return full path

