import streamlit as st
from api_client import get_study_plan

st.header("📅 Study Plan Generator")

if st.button("Generate Study Plan"):
    plan = get_study_plan()

    st.subheader("June – March Plan")
    for month, items in plan["plan"].items():
        st.markdown(f"### {month}")
        for item in items:
            st.write(item)
