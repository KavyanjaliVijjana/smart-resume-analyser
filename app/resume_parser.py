import pdfplumber

pdf_path = "../data/sample_resume.pdf"

text = ""

with pdfplumber.open("C:\\Users\\anju&janu\\OneDrive\\kavya\\smart-resume-analyzer\\data\\sample_resume.pdf") as pdf:
    for page in pdf.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted

# basic preprocessing
text = text.lower()

print(text)