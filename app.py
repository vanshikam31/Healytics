"""Healytics application entry point.

Milestone 1: project initialization.
The prediction interface will be implemented in a later milestone.
"""

import streamlit as st

st.set_page_config(
    page_title="Healytics",
    page_icon="🩺",
    layout="wide",
)

st.title("Healytics")
st.subheader("An AI-Based Multi-Disease Risk Prediction System")

st.info(
    "Project initialized. Disease-specific prediction modules will be added "
    "in later milestones."
)

st.warning(
    "Healytics is an educational/decision-support project and is not a medical "
    "diagnostic tool."
)
