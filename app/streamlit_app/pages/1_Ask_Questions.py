import streamlit as st
from api_client import ask_question

st.header("🧠 Ask Textbook Questions")

question = st.text_input(
    "Ask a question from the textbook",
    placeholder="What is the chemical formula of water?"
)

if st.button("Ask"):
    with st.spinner("Thinking..."):
        result = ask_question(question)

    if "options" in result:
        st.warning(result["message"])
    else:
        st.success(result["answer"])

        st.caption(f"Confidence: {result.get('confidence', 'N/A')}")
        st.caption(f"Source: {result.get('source', 'Textbook')}")
