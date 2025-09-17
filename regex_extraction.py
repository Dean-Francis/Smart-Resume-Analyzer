import re

def extract_phone(text: str) -> list[str]:
    # Extract phone numbers with improved patterns
    patterns = [
        r'\+\d{1,3}[\s-]?\d{1,3}[\s-]?\d{3,4}[\s-]?\d{4}',  # International format
        r'\+\d{1,3}\s*\d{2,3}\s*\d{3,4}\s*\d{4}',          # With spaces
        r'\(\d{3}\)\s*\d{3}[-\s]?\d{4}',                    # US format (xxx) xxx-xxxx
        r'\d{3}[-\s]?\d{3}[-\s]?\d{4}',                     # Simple xxx-xxx-xxxx
        r'\d{2,3}[\s-]?\d{3,4}[\s-]?\d{4}'                  # Local variations
    ]
    
    phones = []
    for pattern in patterns:
        matches = re.findall(pattern, text)
        phones.extend(matches)
    
    # Clean and deduplicate
    cleaned_phones = []
    for phone in phones:
        # Remove extra spaces and standardize
        clean_phone = re.sub(r'\s+', ' ', phone.strip())
        if clean_phone and clean_phone not in cleaned_phones:
            cleaned_phones.append(clean_phone)
    
    return cleaned_phones

def extract_email(text):
    text_clean = text.replace("\n", "")
    return re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b', text_clean)

def extract_links(text):
    return re.findall(r'https?://[^\s]+', text)
