import re

def check_link(url):
    suspicious_keywords = ["login", "verify", "update", "free", "win", "bank"]

    # Rule 1: HTTP is unsafe
    if url.startswith("http://"):
        return "⚠️ Unsafe (HTTP)"

    # Rule 2: Too many dots
    if url.count('.') > 3:
        return "⚠️ Suspicious structure"

    # Rule 3: Check keywords
    for word in suspicious_keywords:
        if word in url.lower():
            return "🚨 Phishing suspected"

    # Rule 4: Shortened links
    if re.search(r"bit\.ly|tinyurl|goo\.gl", url):
        return "⚠️ Shortened URL"

    return "✅ Safe"