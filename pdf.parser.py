from PyPDF2 import PdfReader

reader = PdfReader("PDF TEST.pdf")
page = reader.pages[0]
text = page.extract_text()
print(text)