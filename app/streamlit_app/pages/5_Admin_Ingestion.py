import streamlit as st
from api_client import ingest_pdf

st.header("📥 Ingest Text")

text = st.text_area("Paste textbook content")

if st.button("Ingest"):
    result = ingest_pdf(text)
    st.success(result)
