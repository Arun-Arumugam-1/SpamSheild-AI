import pytesseract
from PIL import Image
from model import predict_spam

# IMPORTANT: Set your tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def analyze_image(image):
    text = pytesseract.image_to_string(image)

    prediction, prob = predict_spam(text)

    return text, prediction, prob