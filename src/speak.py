from gtts import gTTS

def speak(text, filename="detected_number.mp3"):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    return filename
