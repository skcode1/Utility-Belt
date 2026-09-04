from pypdf import PdfWriter

writer = PdfWriter()

for file in [
    # your PDF files here
    "document1.pdf", 
    "document2.pdf",
    "document3.pdf"
]: writer.append(file)

writer.write("merged.pdf")

writer.close()


"""
If you want to make this script more robust so it doesn't crash if a file is missing, 
you can add a quick check using Python's built-in os module:

import os
from pypdf import PdfWriter

writer = PdfWriter()

files_to_merge = ["document1.pdf", "document2.pdf", "document3.pdf"]

for file in files_to_merge:
    if os.path.exists(file):
        writer.append(file)
    else:
        print(f"⚠️ Warning: Skipping missing file -> {file}")

writer.write("merged.pdf")
writer.close()
print("✅ Success: merged.pdf created!")

"""