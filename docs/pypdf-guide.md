# 🚀 PDF Merger (pypdf wrapper)

A lightweight script to sequentially merge multiple PDF files into a single, unified document.

---

## 🛠️ Prerequisites

* **Python 3.10+**

---

## 📦 Dependency Installation

Make sure your virtual environment is activated, then install the required package:

```bash
pip install pypdf
```

---

## 💻 Usage

1. Open `pdf_processor.py` and add your target filenames to the file list:
   ```python
   files_to_merge = ["document1.pdf", "document2.pdf", "document3.pdf"]
   ```

2. Run the script directly from your terminal:
   ```bash
   python pdf_processor.py
   ```

### ℹ️ How it Works
The script initializes a `PdfWriter` instance, loops through your specified list of files to append their pages sequentially, and outputs a combined file named `merged.pdf` into your current working directory.

---

## 📚 Resources & Documentation

* [pypdf GitHub Repository](https://github.com)
* [pypdf Official Documentation](https://readthedocs.io)
