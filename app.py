import streamlit as st
from triage_ai import classify_feedback
from baseline import baseline_classify

st.set_page_config(page_title="Customer Feedback Triage", layout="centered")

st.title("📩 Customer Feedback Triage System")

st.write("Enter customer feedback below. The system will classify it using:")
st.write("- 🧠 Baseline Rule Logic")
st.write("- 🤖 Azure OpenAI")

feedback = st.text_area("Enter Customer Feedback")

if st.button("Analyze Feedback"):

    if feedback.strip() == "":
        st.warning("Please enter feedback first.")
    else:
        st.subheader("📊 Baseline Output")
        st.success(baseline_classify(feedback))

        st.subheader("🤖 Azure OpenAI Output")
        st.info(classify_feedback(feedback))
