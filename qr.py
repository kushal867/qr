import qrcode
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Get the link from .env
file_url = os.getenv("GOOGLE_DRIVE_LINK")

if not file_url:
    print("GOOGLE_DRIVE_LINK not found in .env")
    exit()

# Generate the QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4
)
qr.add_data(file_url)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
qr_filename = "drive_link_qr.png"
img.save(qr_filename)

print(f"QR code saved as '{qr_filename}'")
