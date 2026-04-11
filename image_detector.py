import easyocr
from PIL import Image

def analyze_image(image):
    try:
        reader = easyocr.Reader(['en'])
        result = reader.readtext(image)
        
        # Extract text from results
        text = "\n".join([detection[1] for detection in result])
        
        # Spam detection based on keywords
        spam_keywords = ['verify', 'confirm', 'urgent', 'click', 'update', 'login', 'password', 'bank', 'secure']
        
        spam_count = sum(1 for keyword in spam_keywords if keyword.lower() in text.lower())
        
        if spam_count >= 3:
            prediction = 1  # Spam
            prob = min(100, (spam_count * 20))
        else:
            prediction = 0  # Safe
            prob = max(0, 100 - (spam_count * 15))
        
        return text, prediction, prob
        
    except Exception as e:
        return f"Error analyzing image: {str(e)}", 0, 0
