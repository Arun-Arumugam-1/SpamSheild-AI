import easyocr
from PIL import Image
import numpy as np

def analyze_image(image):
    try:
        # Convert PIL image to numpy array
        image_array = np.array(image)
        
        # Initialize EasyOCR reader
        reader = easyocr.Reader(['en'])
        
        # Read text from image
        result = reader.readtext(image_array)
        
        # Extract text
        text = "\n".join([detection[1] for detection in result])
        
        # Spam keywords
        spam_keywords = ['verify', 'confirm', 'urgent', 'click', 'update', 'login', 'password', 'bank', 'secure', 'confirm', 'act now', 'limited time']
        
        spam_count = sum(1 for keyword in spam_keywords if keyword.lower() in text.lower())
        
        if spam_count >= 2:
            prediction = 1  # Spam
            prob = min(100, (spam_count * 25))
        else:
            prediction = 0  # Safe
            prob = max(0, 100 - (spam_count * 20))
        
        return text, prediction, prob
        
    except Exception as e:
        return f"Error: {str(e)}", 0, 0
