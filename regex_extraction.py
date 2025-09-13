import re

def extract_email(text):
    return re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b", text)

def extract_phone(text):
    return re.findall(r'\+?\d[\d\s-]{8,}', text)

def extract_links(text):
    return re.findall(r'https?://[^\s]+', text)
