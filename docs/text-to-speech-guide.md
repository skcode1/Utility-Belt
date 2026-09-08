# 🔊 Text-to-Speech Generator (gTTS wrapper)

A lightweight script to convert text strings into spoken audio files using Google Text-to-Speech.

---

## 🛠️ Prerequisites

* **Python 3.10+**

---

## 📦 Dependency Installation

Make sure your virtual environment is activated, then install the required package:

```bash
pip install gTTS
```

---

## 💻 Usage

1. Open `text_to_speech_generator.py` and modify the target text string variable:
   ```python
   text = "Hello world, welcome to the text to speech generator."
   ```

2. Run the script directly from your terminal:
   ```bash
   python text_to_speech_generator.py
   ```

### ℹ️ How it Works
The script imports the `gTTS` library, initializes an engine instance with your custom text and language configuration (`lang='en'`), renders the speech, and outputs an audio file named `output.mp3` into your current working directory.

---

## 📚 Resources & Documentation

* [gTTS GitHub Repository](https://github.com)
* [gTTS Official Documentation](https://gtts.readthedocs.io)
