import streamlit as st
from openai import OpenAI
from prompts import SYSTEM_PROMPT, build_rca_prompt
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
if analyze:
    if not incident.strip():
        st.warning("Please enter an incident description before generating an RCA.")
    else:
        try:
            client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

            user_prompt = build_rca_prompt(
                incident,
                metrics,
                factors,
                actions
            )

            with st.spinner("Analyzing incident..."):
                response = client.responses.create(
                    model="gpt-5-mini",
                    instructions=SYSTEM_PROMPT,
                    input=user_prompt
                )

            st.divider()
            st.header("RCA Analysis")
            st.markdown(response.output_text)

        except Exception as e:
            st.error(
                "Unable to generate the RCA. "
                "Please verify that the application is configured correctly."
            )
