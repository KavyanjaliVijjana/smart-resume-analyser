import pdfplumber
import re

# resume path
pdf_path = "C:\\Users\\anju&janu\\OneDrive\\kavya\\smart-resume-analyzer\\data\\sample_resume.pdf"

# extract text
text = ""
text = re.sub(r'[^a-zA-Z0-9 ]', '', text)

with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        extracted = page.extract_text()

        if extracted:
            text += extracted

# preprocessing
text = text.lower()

# predefined skills
skills = [
    "python",
    "sql",
    "pandas",
    "numpy",
    "machine learning",
    "java",
    "c",
    "html",
    "css",
    "javascript",
    "data analysis"
]

# extracted skills
found_skills = []

for skill in skills:
    if skill in text:
        found_skills.append(skill)

print("Skills Found:")

for skill in found_skills:
    print("-", skill)