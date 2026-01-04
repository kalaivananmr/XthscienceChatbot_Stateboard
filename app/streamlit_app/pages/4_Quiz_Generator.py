import streamlit as st
from api_client import ask_question

st.header("📝 Quiz Generator")

chapter = st.text_input("Chapter Name")
qtype = st.selectbox(
    "Question Type",
    ["MCQ", "Fill in the Blanks", "Short Answer"]
)

if st.button("Generate Quiz"):
    prompt = f"Generate {qtype} questions from chapter {chapter}"
    result = ask_question(prompt)

    st.write(result["answer"])
