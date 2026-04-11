import streamlit as st
from model import predict_spam
from link_detector import check_link
from PIL import Image
from image_detector import analyze_image

# Page settings
st.set_page_config(page_title="SpamShield AI", page_icon="🛡", layout="centered")

# Custom styling (Premium look)
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #1f4037, #99f2c8);
        padding: 20px;
        border-radius: 15px;
    }
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: white;
    }
    .subtitle {
        text-align: center;
        color: #e0e0e0;
        margin-bottom: 30px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🛡 SpamShield AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Smart Email & Link Security System</div>', unsafe_allow_html=True)

# ---------------- EMAIL SECTION ----------------
st.markdown("## 📧 Email Spam Detection")

email_input = st.text_area("Enter your email content here...")

if st.button("🔍 Analyze Email"):
    prediction, prob = predict_spam(email_input)

    confidence = prob[1] * 100 if prediction == 1 else prob[0] * 100

    if prediction == 1:
        st.error(f"🚨 Spam Detected ({confidence:.2f}% confidence)")
    else:
        st.success(f"✅ Safe Email ({confidence:.2f}% confidence)")

    st.progress(int(confidence))

# ---------------- LINK SECTION ----------------
st.markdown("## 🔗 Link Safety Check")

link_input = st.text_input("Enter URL here...")

if st.button("🌐 Check Link"):
    result = check_link(link_input)

    if "Safe" in result:
        st.success(result)
    else:
        st.warning(result)


# ---------------- IMAGE SECTION ----------------
st.markdown("## 🖼️ Screenshot Spam Detection")
st.markdown("Upload a screenshot to detect spam indicators using OCR")

uploaded_file = st.file_uploader("Upload screenshot", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image")
    st.info("🔍 Analyzing screenshot...")
    text, prediction, prob = analyze_image(image)
    st.markdown("### 📄 Extracted Text:")
    st.text_area("Text from screenshot:", text, height=150, disabled=True)
    st.markdown("### 🎯 Detection Result:")
    if prediction == 1:
        st.error(f"⚠️ *SPAM DETECTED* ({prob:.1f}% confidence)")
    else:
        st.success(f"✅ *SAFE* ({prob:.1f}% confidence)")

# Footer
st.markdown("---")
st.markdown("⚡ Built with Machine Learning , NLP & OCR | Hackathon Project")


