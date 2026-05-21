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

# required job skills
required_skills = [
    "python",
    "sql",
    "pandas",
    "machine learning"
]

# matched skills
matched_skills = []

for skill in required_skills:
    if skill in found_skills:
        matched_skills.append(skill)

# calculate score
score = (len(matched_skills) / len(required_skills)) * 100

print("\nMatched Skills:")
print(matched_skills)

print(f"\nResume Score: {score:.2f}%")

missing_skills = []

for skill in required_skills:
    if skill not in found_skills:
        missing_skills.append(skill)

print("\nMissing Skills:")
print(missing_skills)