# 🚀 QR Code Generator (qrcode wrapper)

A lightweight script to quickly encode text or URLs into a clean, shareable QR code image.

---

## 🛠️ Prerequisites

* **Python 3.10+**

---

## 📦 Dependency Installation

Make sure your virtual environment is activated, then install the required package:

```bash
pip install qrcode[pil]
```

---

## 💻 Usage

1. Open `qr_generator.py` and replace the placeholder text with your desired content or URL:
   ```python
   data = "your text or URL here"
   ```

2. Run the script directly from your terminal:
   ```bash
   python qr_generator.py
   ```

### ℹ️ How it Works
The script imports the `qrcode` library, takes the string provided in the `data` variable, generates the corresponding matrix format, and saves the final output as a image file named `qrcode.png` in your current working directory.

---

## 📚 Resources & Documentation

* [qrcode GitHub Repository](https://github.com)
* [qrcode Official Documentation](https://pypi.org)
