# 🚀 Video to GIF Generator (MoviePy wrapper)

A lightweight script to convert an MP4 video file into an animated GIF document.

---

## 🛠️ Prerequisites

* **Python 3.10+**

---

## 📦 Dependency Installation

Make sure your virtual environment is activated, then install the required package:

```bash
pip install moviepy
```

---

## 💻 Usage

1. Open `video_to_gif.py` and specify your target input filename:
   ```python
   clip = VideoFileClip("my_video.mp4")
   ```

2. Run the script directly from your terminal:
   ```bash
   python video_to_gif.py
   ```

### ℹ️ How it Works
The script initializes a `VideoFileClip` instance to read the input target, parses the stream information, and processes it via `imageio` to export a clean, animated asset named `my_video.gif` into your current working directory.

---

## 📚 Resources & Documentation

* [MoviePy GitHub Repository](https://github.com)
* [MoviePy Official Documentation](https://github.io)
