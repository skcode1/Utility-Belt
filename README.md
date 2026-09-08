# Utility-Belt 🛠️

A curated collection of lightweight Python automation scripts and utility libraries for simplifying everyday tasks, media handling, and routine workflows.

---

## 📂 Available Tools & Utilities

| Tool | Description | Quick Link |
| :--- | :--- | :--- |
| **🚀 YouTube Downloader** | Fetch high-resolution video/audio streams via `yt-dlp`. | [View Guide](docs/yt-dlp-guide.md) |
| **📄 PDF Merger** | Sequentially merge multiple PDF files into a single unified document via `pypdf`. | [View Guide](docs/pypdf-guide.md) |
| **🔊 Text-to-Speech Generator** | Convert custom text strings into spoken MP3 audio files via `gTTS`. | [View Guide](docs/text-to-speech-guide.md) |

---

## 📥 Global Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/iqbuzzhhh/Utility-Belt.git
   cd Utility-Belt
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

---

## 🗂️ Project Structure

```text
Utility-Belt/
├── docs/
│   └── yt-dlp-guide.md           # Setup and usage for the YouTube Downloader
│   ├── text-to-speech-guide.md   # Setup and usage for the Text-to-Speech Generator
│   ├── pypdf-guide.md            # Setup and usage for the PDF Merger
├── venv/                         # Virtual environment (ignored by Git)
├── pdf_processor.py              # PDF merger script
├── text_to_speech_generator.py   # Text-to-speech script
├── yt-dlp.py                     # YouTube downloader script
├── .gitignore                    # Git ignore rules for media & venvs
└── README.md                     # Project dashboard & routing
```

## 📄 License

This repository is distributed under the **MIT License**. Feel free to use and modify it for your personal workflows.
