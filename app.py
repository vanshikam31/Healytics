import streamlit as st
import sys
import os

# ============================================================
# HELPER FOR SAFE HTML RENDERING
# ============================================================

def render_html(html_code: str):
    """Renders pure HTML without Streamlit parsing issues."""
    st.html(html_code)


# ============================================================
# PATH CONFIGURATION
# ============================================================

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


from src.prediction.diabetes_predictor import predict_diabetes


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Healytics",
    page_icon="💓",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# CUSTOM CSS — Matches Exact Reference Images
# ============================================================

st.html("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,380;0,9..144,500;0,9..144,600;1,9..144,420&family=Inter:wght@300;400;500;600&display=swap');

:root {
    --ink: #0B1917;
    --ink-card: #081211;
    --bone: #F1ECE0;
    --bone-dim: #98A5A0;
    --gold: #D9A441;
    --rose: #C56A52;
    --moss: #7E9A78;
    --line: rgba(241, 236, 224, 0.12);
}

html, body, [data-testid="stAppViewContainer"] {
    background-color: var(--ink);
    color: var(--bone);
    font-family: 'Inter', sans-serif;
}

[data-testid="stHeader"] {
    background-color: var(--ink);
}

[data-testid="stToolbar"] {
    display: none;
}

.block-container {
    max-width: 1100px;
    padding-top: 0;
    padding-bottom: 70px;
}

#MainMenu, footer {
    visibility: hidden;
}

/* TOP NAV */
.top-nav {
    height: 70px;
    border-bottom: 1px solid var(--line);
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-left: -5rem;
    margin-right: -5rem;
    padding-left: 5rem;
    padding-right: 5rem;
    margin-bottom: 70px;
}

.brand {
    font-family: 'Fraunces', serif;
    font-size: 22px;
    font-style: italic;
    font-weight: 500;
    color: var(--bone);
    display: flex;
    align-items: center;
    gap: 8px;
}

.brand-mark {
    color: var(--gold);
    font-size: 16px;
}

.nav-links {
    display: flex;
    align-items: center;
    gap: 32px;
    color: var(--bone);
    font-size: 14px;
    font-weight: 400;
}

.nav-signin {
    border: 1px solid var(--line);
    border-radius: 100px;
    padding: 7px 20px;
    color: var(--bone);
    font-size: 13.5px;
}

/* HERO */
.hero {
    position: relative;
    padding: 20px 0 90px 0;
}

.eyebrow {
    font-family: 'Fraunces', serif;
    font-size: 15px;
    font-style: italic;
    color: var(--gold);
    margin-bottom: 24px;
}

.hero-title {
    max-width: 680px;
    font-family: 'Fraunces', serif;
    font-size: 58px;
    line-height: 1.08;
    font-weight: 500;
    letter-spacing: -0.5px;
    color: var(--bone);
    margin: 0 0 24px 0;
}

.hero-description {
    max-width: 580px;
    color: var(--bone-dim);
    font-size: 15.5px;
    line-height: 1.65;
    margin-bottom: 36px;
}

.hero-cta-group {
    display: flex;
    align-items: center;
    gap: 24px;
}

.hero-btn {
    background-color: var(--gold);
    color: var(--ink);
    padding: 12px 28px;
    border-radius: 100px;
    font-weight: 600;
    font-size: 14px;
    text-decoration: none;
    display: inline-block;
}

.hero-link {
    color: var(--bone-dim);
    font-size: 13.5px;
    text-decoration: underline;
    text-underline-offset: 4px;
}

.ecg {
    position: absolute;
    left: -10%;
    right: -10%;
    bottom: 50px;
    height: 110px;
    opacity: 0.25;
    pointer-events: none;
    z-index: 0;
}

.ecg svg {
    width: 100%;
    height: 100%;
}

.ecg polyline {
    fill: none;
    stroke: var(--gold);
    stroke-width: 1.2;
}

/* INDEX */
.index-section {
    margin-top: 60px;
    margin-bottom: 100px;
}

.section-eyebrow {
    font-family: 'Fraunces', serif;
    font-style: italic;
    color: var(--gold);
    font-size: 14px;
    margin-bottom: 10px;
}

.section-title {
    font-family: 'Fraunces', serif;
    font-size: 32px;
    font-weight: 500;
    color: var(--bone);
    margin-bottom: 40px;
}

.disease-list {
    border-top: 1px solid var(--line);
}

.disease-row {
    display: grid;
    grid-template-columns: 60px 1fr 140px;
    align-items: center;
    padding: 24px 0;
    border-bottom: 1px solid var(--line);
}

.disease-number {
    font-family: 'Fraunces', serif;
    font-style: italic;
    font-size: 16px;
    color: var(--bone-dim);
}

.disease-name {
    font-family: 'Fraunces', serif;
    font-size: 24px;
    font-weight: 500;
    color: var(--bone);
    margin-bottom: 4px;
}

.disease-description {
    font-size: 13.5px;
    color: var(--bone-dim);
}

.disease-meta {
    text-align: right;
    color: var(--bone-dim);
    font-size: 13px;
    line-height: 1.4;
}

/* INPUT FORM & RESULT CARD SECTION */
.module-header {
    margin-bottom: 30px;
}

.module-label {
    font-family: 'Fraunces', serif;
    font-style: italic;
    color: var(--gold);
    font-size: 14px;
    margin-bottom: 8px;
}

.module-title {
    font-family: 'Fraunces', serif;
    font-size: 28px;
    font-weight: 500;
    color: var(--bone);
    margin-bottom: 6px;
}

.module-sub {
    color: var(--bone-dim);
    font-size: 14px;
}

/* INPUT STYLES */
div[data-baseweb="input"] {
    background-color: transparent !important;
    border: none !important;
    border-bottom: 1px solid var(--line) !important;
    border-radius: 0 !important;
}

div[data-baseweb="input"]:focus-within {
    border-bottom: 1px solid var(--gold) !important;
}

input {
    color: var(--bone) !important;
    background-color: transparent !important;
    font-family: 'Fraunces', serif !important;
    font-size: 18px !important;
    padding-left: 0 !important;
}

label {
    color: var(--bone-dim) !important;
    font-size: 12px !important;
    font-weight: 400 !important;
}

div[data-testid="stNumberInput"] {
    margin-bottom: 20px;
}

/* BUTTON */
div.stButton > button {
    background-color: var(--gold) !important;
    color: var(--ink) !important;
    border: none !important;
    border-radius: 100px !important;
    padding: 12px 28px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 14px !important;
    font-weight: 600 !important;
    margin-top: 15px;
}

div.stButton > button:hover {
    background-color: #e8bb58 !important;
    color: var(--ink) !important;
}

/* RESULT CARD */
.result-card {
    background-color: var(--ink-card);
    border: 1px solid var(--line);
    padding: 36px;
    border-radius: 2px;
}

.result-top {
    display: flex;
    justify-content: space-between;
    color: var(--bone-dim);
    font-size: 13px;
    margin-bottom: 24px;
}

.result-probability {
    font-family: 'Fraunces', serif;
    font-size: 72px;
    line-height: 1;
    font-weight: 500;
    color: var(--bone);
    margin-bottom: 8px;
}

.result-label {
    color: var(--bone-dim);
    font-size: 13px;
    margin-bottom: 24px;
}

.gauge-bar {
    height: 2px;
    background: var(--line);
    margin-bottom: 24px;
    position: relative;
}

.gauge-fill {
    position: absolute;
    top: 0;
    left: 0;
    height: 100%;
}

.result-status {
    font-family: 'Fraunces', serif;
    font-size: 16px;
    font-style: italic;
    margin-bottom: 28px;
}

.status-high { color: var(--rose); }
.status-low { color: var(--moss); }

.factor {
    display: flex;
    justify-content: space-between;
    padding: 12px 0;
    border-top: 1px solid var(--line);
    font-size: 13.5px;
}

.factor:last-of-type {
    border-bottom: 1px solid var(--line);
    margin-bottom: 28px;
}

.factor-name { color: var(--bone); }
.flag-high { color: var(--rose); }
.flag-ok { color: var(--bone-dim); }

.result-note {
    color: var(--bone-dim);
    font-size: 12px;
    font-style: italic;
    font-family: 'Fraunces', serif;
    line-height: 1.5;
}
</style>
""")


# ============================================================
# TOP NAVIGATION
# ============================================================

render_html("""
<div class="top-nav">
    <div class="brand">
        <span class="brand-mark">∿</span> Healytics
    </div>
    <div class="nav-links">
        <span>Screenings</span>
        <span>Assess</span>
        <span>Clinician view</span>
        <span class="nav-signin">Sign in</span>
    </div>
</div>
""")


# ============================================================
# HERO SECTION (Image 1)
# ============================================================

render_html("""
<section class="hero">
    <div class="eyebrow">A screening companion, not a diagnosis</div>
    <h1 class="hero-title">Four readings of one body, in a single sitting</h1>
    <p class="hero-description">
        Enter values from a routine panel and Healytics runs them through four clinically-grounded models — diabetes to breast cancer — surfacing what's worth a conversation with your doctor.
    </p>
    <div class="hero-cta-group">
        <a href="#assessment" class="hero-btn">Begin an assessment</a>
        <a href="#index" class="hero-link">See all four models</a>
    </div>
    <div class="ecg">
        <svg viewBox="0 0 1200 120" preserveAspectRatio="none">
            <polyline points="0,75 35,75 50,60 68,75 95,75 108,112 126,15 145,105 164,75 215,75 235,52 260,75 300,75 330,75 350,60 370,75 405,75 420,112 438,15 457,105 476,75 530,75 550,55 575,75 620,75 650,75 670,60 690,75 725,75 740,112 758,15 777,105 796,75 850,75 870,52 895,75 940,75 970,75 990,60 1010,75 1045,75 1060,112 1078,15 1097,105 1116,75 1200,75" />
        </svg>
    </div>
</section>
""")


# ============================================================
# INDEX SECTION (Image 2)
# ============================================================

render_html("""
<div id="index" class="index-section">
    <div class="section-eyebrow">The index</div>
    <div class="section-title">Four conditions, one intake</div>
    <div class="disease-list">
        <div class="disease-row">
            <div class="disease-number">01</div>
            <div>
                <div class="disease-name">Diabetes</div>
                <div class="disease-description">Type 2 risk from glucose, BMI, and family history</div>
            </div>
            <div class="disease-meta">2 min<br>8 values</div>
        </div>
        <div class="disease-row">
            <div class="disease-number">02</div>
            <div>
                <div class="disease-name">Heart disease</div>
                <div class="disease-description">Coronary risk from ECG, cholesterol, chest pain type</div>
            </div>
            <div class="disease-meta">4 min<br>13 values</div>
        </div>
        <div class="disease-row">
            <div class="disease-number">03</div>
            <div>
                <div class="disease-name">Parkinson's</div>
                <div class="disease-description">Early motor signs from voice frequency measures</div>
            </div>
            <div class="disease-meta">1 min<br>voice sample</div>
        </div>
        <div class="disease-row">
            <div class="disease-number">04</div>
            <div>
                <div class="disease-name">Breast cancer</div>
                <div class="disease-description">Malignancy likelihood from cell nuclei measurements</div>
            </div>
            <div class="disease-meta">lab upload<br>30 values</div>
        </div>
    </div>
</div>
""")


# ============================================================
# INTAKE & PREDICTION CARD (Image 3)
# ============================================================

render_html("""
<div id="assessment" class="module-header">
    <div class="module-label">01 — Diabetes</div>
    <div class="module-title">Patient values</div>
    <div class="module-sub">From a recent basic metabolic panel and a home cuff reading.</div>
</div>
""")

left_col, right_col = st.columns([1.05, 0.95], gap="large")

with left_col:
    p_col1, p_col2 = st.columns(2)
    with p_col1:
        pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=2, step=1)
        glucose = st.number_input("Glucose, mg/dL", min_value=0.0, max_value=300.0, value=142.0, step=1.0)
        bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=29.4, step=0.1)
        insulin = st.number_input("Insulin, µU/mL", min_value=0.0, max_value=900.0, value=118.0, step=1.0)

    with p_col2:
        age = st.number_input("Age, years", min_value=1, max_value=120, value=41, step=1)
        blood_pressure = st.number_input("Blood pressure, mmHg", min_value=0.0, max_value=200.0, value=86.0, step=1.0)
        skin_thickness = st.number_input("Skin thickness, mm", min_value=0.0, max_value=100.0, value=24.0, step=1.0)
        diabetes_pedigree = st.number_input("Family history score", min_value=0.0, max_value=3.0, value=0.52, step=0.01)

    predict_button = st.button("Run this screening")

with right_col:
    # Default values or dynamic upon button click
    input_data = {
        "Pregnancies": pregnancies,
        "Glucose": glucose,
        "BloodPressure": blood_pressure,
        "SkinThickness": skin_thickness,
        "Insulin": insulin,
        "BMI": bmi,
        "DiabetesPedigreeFunction": diabetes_pedigree,
        "Age": age
    }

    try:
        if predict_button:
            result = predict_diabetes(input_data)
            probability = result["probability"]
            prediction = result["prediction"]
        else:
            # Default preview matching Image 3 (34%)
            probability = 0.34
            prediction = 0

        is_high_risk = probability >= 0.5 or prediction == 1
        pct = int(probability * 100)
        fill_color = "#C56A52" if is_high_risk else "#C56A52" # Match Image 3 muted rose bar

        status_text = "Moderate — worth a follow-up" if 0.3 <= probability < 0.6 else ("Elevated risk — follow-up advised" if probability >= 0.6 else "Low risk — within expected range")
        status_class = "status-high" if probability >= 0.3 else "status-low"

        factors_html = f"""
        <div class="factor">
            <span class="factor-name">Glucose</span>
            <span class="{"flag-high" if glucose >= 140 else "flag-ok"}">{"Above typical range" if glucose >= 140 else "Within range"}</span>
        </div>
        <div class="factor">
            <span class="factor-name">BMI</span>
            <span class="{"flag-high" if bmi >= 25 else "flag-ok"}">{"Contributing factor" if bmi >= 25 else "Within range"}</span>
        </div>
        <div class="factor">
            <span class="factor-name">Family history</span>
            <span class="{"flag-high" if diabetes_pedigree >= 0.5 else "flag-ok"}">{"Elevated" if diabetes_pedigree >= 0.5 else "Within range"}</span>
        </div>
        <div class="factor">
            <span class="factor-name">Blood pressure</span>
            <span class="{"flag-high" if blood_pressure >= 90 else "flag-ok"}">{"Above typical range" if blood_pressure >= 90 else "Within range"}</span>
        </div>
        """

        render_html(f"""
        <div class="result-card">
            <div class="result-top">
                <span>Estimated risk</span>
                <span>Model v2.3</span>
            </div>
            <div class="result-probability">{pct}%</div>
            <div class="result-label">likelihood, relative to baseline population</div>
            <div class="gauge-bar">
                <div class="gauge-fill" style="width:{pct}%; background:{fill_color};"></div>
            </div>
            <div class="result-status {status_class}">{status_text}</div>
            {factors_html}
            <div class="result-note">
                A statistical estimate, not a diagnosis — bring this reading to a clinician.
            </div>
        </div>
        """)

    except Exception as e:
        st.error(f"Prediction error: {e}")