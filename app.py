import streamlit as st
import PyPDF2
import re

st.set_page_config(page_title="AI Resume Analyzer")

st.title("AI Resume Analyzer")
st.write("Upload your resume PDF")

uploaded_file = st.file_uploader("Upload Resume", type=["pdf"])

skills = [
    "python",
    "java",
    "c++",
    "machine learning",
    "sql",
    "html",
    "css",
    "javascript",
    "communication",
    "teamwork"
]

if uploaded_file is not None:

    pdf_reader = PyPDF2.PdfReader(uploaded_file)

    text = ""

    for page in pdf_reader.pages:
        text += page.extract_text()

    text = text.lower()

    found_skills = []

    for skill in skills:
        if skill in text:
            found_skills.append(skill)

    score = len(found_skills) * 10

    st.subheader("Skills Found")
    st.write(found_skills)

    st.subheader("Resume Score")
    st.write(score, "/ 100")

    missing_skills = []

    for skill in skills:
        if skill not in found_skills:
            missing_skills.append(skill)

    st.subheader("Missing Skills")
    st.write(missing_skills)

    if score >= 70:
        st.success("Strong Resume")
    else:
        st.warning("Improve Your Resume")
