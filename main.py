from pdf_parser import extract_text
from nlp_extractor import nlp_extraction
from regex_extraction import extract_phone, extract_email, extract_links

path = "Dean Francis Tolero - Resume.pdf"

text = extract_text(path)

# Regex Extraction
phone = extract_phone(text)
email = extract_email(text)
links = extract_links(text)
print("Phone: ", phone)
print("Email:", email)
print("Links:", links)

# spaCy Extraction
entities = nlp_extraction(text)
print("Entities: ", entities)