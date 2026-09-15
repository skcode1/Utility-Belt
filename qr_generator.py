import qrcode 

data = "your text or URL here"  # Replace with the data you want to encode in the QR code

qr = qrcode.make(data)

qr.save("qrcode.png")