from PyPDF2 import PdfReader

reader = PdfReader("test.pdf")
page = reader.pages[0]
print("     ")
print(page.extract_text())