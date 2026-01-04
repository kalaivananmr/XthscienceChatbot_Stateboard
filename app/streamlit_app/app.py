import streamlit as st

st.set_page_config(
    page_title="Teacher Dashboard – Science RAG",
    layout="wide"
)

st.title("📘 Class 10 Science – Teacher Dashboard")

st.markdown("""
**Hybrid RAG System**
- Vector + Knowledge Graph
- Zero hallucination
- Exam-aligned answers
""")

st.sidebar.success("Select a module from the left")
