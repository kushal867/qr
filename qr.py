import qrcode
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Read environment variable
file_url = os.getenv("GOOGLE_DRIVE_LINK")

if not file_url:
    print("Error: GOOGLE_DRIVE_LINK not found in .env")
    exit(1)

# Configure QR code
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

qr.add_data(file_url)
qr.make(fit=True)

# Generate QR image
img = qr.make_image(fill_color="black", back_color="white")

# Save output file
qr_filename = "drive_link_qr.png"
img.save(qr_filename)

print(f"QR code saved as '{qr_filename}'")
