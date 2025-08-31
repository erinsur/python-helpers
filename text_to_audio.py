from gtts import gTTS

def text_to_audio(text):
    tts = gTTS(text, lang="en")
    tts.save("output.mp3")

text_to_audio("Wait a min.")
