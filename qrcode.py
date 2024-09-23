import qrcode

# Data you want to encode in the QR code
data = "https://www.cybersquare.org/"

# Create a QR code instance with specific settings
qr = qrcode.QRCode(
    version=1,  # Version of the QR code (1 = smallest, 40 = largest)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of the box where the QR code will be displayed
    border=4,  # Thickness of the border (default is 4)
)

# Add data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create an image from the QR code instance
img = qr.make_image(fill='black', back_color='white')

# Save the generated QR code as an image file
img.save("qrcode.png")

print("QR code generated and saved as 'qrcode.png'.")
