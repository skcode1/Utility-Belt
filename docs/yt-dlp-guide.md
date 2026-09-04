# 🚀 YouTube Downloader (yt-dlp wrapper)

A lightweight script to fetch high-resolution video and audio streams directly from a provided YouTube URL.

---

## 🛠️ Prerequisites

* **Python 3.10+**
* [FFmpeg](https://ffmpeg.org/) (highly recommended for automatic video and audio merging)

---

## 📦 Dependency Installation

Make sure your virtual environment is activated, then install the required package:

```bash
pip install yt-dlp
```

---

## 💻 Usage

1. Run the script directly from your terminal:
   ```bash
   python yt-dlp.py
   ```

2. Paste the target YouTube video link when prompted:
   ```text
   Youtube URL : https://www.youtube.com/watch?v=example
   ```

### ℹ️ How it Works
The script automatically requests the best available video and audio streams (`bestvideo+bestaudio/best`) and uses FFmpeg to merge them into a single file in your current working directory.

---

## 📚 Resources & Documentation

* [yt-dlp GitHub Repository](https://github.com)
* [FFmpeg Download & Setup Guide](https://ffmpeg.org)
