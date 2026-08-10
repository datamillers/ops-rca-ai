import streamlit as st

st.set_page_config(
    page_title="OpsRCA AI",
    page_icon="🔎",
    layout="wide"
)

st.title("🔎 OpsRCA AI")
st.subheader("AI-Assisted Root Cause Analysis")

st.write(
    "Turn operational incident information into a structured "
    "root cause analysis and corrective-action plan."
)

st.info(
    "This demonstration uses synthetic operational scenarios only. "
    "Do not enter confidential or sensitive information."
)

st.divider()

st.header("Incident Information")

incident = st.text_area(
    "Incident description",
    placeholder="Describe what happened...",
    height=150
)

metrics = st.text_area(
    "Relevant metrics or observations",
    placeholder="Enter relevant measurements, trends, timestamps, or observations..."
)

factors = st.text_area(
    "Known contributing factors",
    placeholder="Enter any factors already identified..."
)

actions = st.text_area(
    "Immediate actions taken",
    placeholder="Describe actions already taken to contain or address the issue..."
)

analyze = st.button("Generate RCA", type="primary")
