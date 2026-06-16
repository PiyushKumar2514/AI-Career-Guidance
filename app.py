import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("🎓 AI Career Guidance System")

name = st.text_input("Name")

branch = st.selectbox(
    "Branch",
    ["CSE","IT","ECE","EE","ME","Civil"]
)

year = st.selectbox(
    "Current Year",
    [1,2,3,4]
)

skills = st.text_area(
    "Your Skills",
    placeholder="Python, C++, HTML"
)

interests = st.text_area(
    "Your Interests",
    placeholder="AI, Web Development"
)

resume = st.text_area(
    "Paste Resume (Optional)"
)

if st.button("Analyze Career"):

    prompt = f"""
    You are an expert AI Career Counselor.

    Student:

    Name: {name}

    Branch: {branch}

    Year: {year}

    Skills:
    {skills}

    Interests:
    {interests}

    Resume:
    {resume}

    Provide:

    1. Best Career Recommendations

    2. Skill Gap Analysis

    3. 6 Month Learning Roadmap

    4. Resume Feedback

    5. Interview Questions

    Give clean headings and bullet points.
    """

    with st.spinner("Analyzing..."):

        response = model.generate_content(prompt)

        st.markdown(response.text)