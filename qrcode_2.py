import qrcode
from PIL import Image


link = input("Enter the link you want to encode: ")
filename = input("Enter the filename for the QR code (without extension): ")


qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)

qr.add_data(link)
qr.make(fit=True)

img = qr.make_image(fill_color="grey", back_color="black")

img.save(f"{filename}.png")

print(f"QR code saved as {filename}.png")
