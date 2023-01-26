from PIL import Image

# Open the screenshot
screenshot = Image.open(r"C:\Users\AG\Desktop\PRACA\LEKCJE\LEK1.0\screenshot.png")

# Convert the image to grayscale
gray_screenshot = screenshot.convert("L")

# Perform OCR on the grayscale image
from pytesseract import image_to_string
text = image_to_string(gray_screenshot)

print(text)