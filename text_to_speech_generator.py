from gtts import gTTS

text = "hello world, welcome to the text to speech generator."   # write your text here

tts = gTTS(text=text, lang='en')
tts.save("output.mp3")
print("audio saved successfully")