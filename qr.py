import qrcode

qr = qrcode.QRCode(version=1, box_size=10, border=5)

data = "https://i.imgur.com/z6jQwCs.jpg"
qr.add_data(data)

qr.make(fit=True)

# create an image from the QR code
img = qr.make_image(fill_color="black", back_color="white")

# here the image is saved //
img.save("qr_code.png")
