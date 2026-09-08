from gtts import gTTS

text = "hello everyone, welcome to python coding"

tts = gTTS(text=text, lang='en')
tts.save("output.mp3")
print("audio saved successfully")