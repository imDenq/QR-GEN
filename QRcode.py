import qrcode
import os

data = "salut toi, comment va l'équipe"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

downloads_path = os.path.join(os.path.expanduser('~'), 'Downloads')
file_path = os.path.join(downloads_path, "qr_code.png")

img.save(file_path)  
