import streamlit as st
import pdfplumber
import re

st.title("Smart Resume Analyzer")

text=""
uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)
if uploaded_file is not None:

    

    with pdfplumber.open(uploaded_file) as pdf:

        for page in pdf.pages:

            extracted = page.extract_text()

            if extracted:
                text += extracted

    text = text.lower()

    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)

skills = [
    "python",
    "sql",
    "pandas",
    "numpy",
    "machine learning",
    "java",
    "html",
    "css"
]

found_skills = []

for skill in skills:

    if skill in text:
        found_skills.append(skill)

st.subheader("Extracted Skills")

for skill in found_skills:
    st.write("-", skill)

required_skills = [
    "python",
    "sql",
    "pandas",
    "machine learning"
]

matched_skills = []

for skill in required_skills:

    if skill in found_skills:
        matched_skills.append(skill)

score = (
    len(matched_skills)
    / len(required_skills)
) * 100

st.subheader("ATS Score")

st.write(f"{score:.2f}%")

missing_skills = []

for skill in required_skills:

    if skill not in found_skills:
        missing_skills.append(skill)

st.subheader("Missing Skills")

for skill in missing_skills:
    st.write("-", skill)

