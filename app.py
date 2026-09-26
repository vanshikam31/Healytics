import streamlit as st
import sys
import os
import time


# ============================================================
# HTML HELPERS
# ============================================================

def flatten_html(html):
    lines = html.strip("\n").split("\n")
    return "\n".join(line.lstrip() for line in lines)


def render_html(html):
    st.markdown(
        flatten_html(html),
        unsafe_allow_html=True
    )


# ============================================================
# PATH CONFIGURATION
# ============================================================

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)


# ============================================================
# PREDICTORS
# ============================================================

from src.prediction.diabetes_predictor import predict_diabetes
from src.prediction.heart_disease_predictor import predict_heart_disease


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
# CUSTOM CSS
# ============================================================

render_html(
    """
    <style>

    @import url(
        'https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,380;0,9..144,500;0,9..144,600;1,9..144,420&family=Inter:wght@400;500;600&display=swap'
    );

    :root {
        --ink: #0E211E;
        --ink-2: #15302B;
        --bone: #F1ECE0;
        --bone-dim: #C9C2AE;
        --gold: #D9A441;
        --rose: #C56A52;
        --moss: #7E9A78;
        --line: rgba(241, 236, 224, 0.14);
    }

    html,
    body,
    [data-testid="stAppViewContainer"] {
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
        max-width: 1080px;
        padding-top: 0;
        padding-bottom: 70px;
    }

    .project-name {
        font-family: "Cormorant Garamond", Georgia, serif;
        font-size: 32px;
        font-style: italic;
        color: #e8e3d8;
        text-align: center;
        margin: 30px 0;
        letter-spacing: 1px;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }


    /* ========================================================
       NAVIGATION
       ======================================================== */

    .top-nav {
        height: 68px;
        border-bottom: 1px solid var(--line);

        display: flex;
        align-items: center;
        justify-content: space-between;

        margin-left: -5rem;
        margin-right: -5rem;

        padding-left: 5rem;
        padding-right: 5rem;

        margin-bottom: 80px;
    }

    .brand {
        font-family: 'Fraunces', serif;
        font-size: 22px;
        font-style: italic;
        font-weight: 500;
        color: var(--bone);
    }

    .brand-mark {
        color: var(--gold);
        margin-right: 9px;
        font-size: 16px;
    }

    .nav-links {
        display: flex;
        align-items: center;
        gap: 38px;
        color: var(--bone-dim);
        font-size: 13.5px;
    }

    .nav-signin {
        border: 1px solid var(--line);
        border-radius: 100px;
        padding: 8px 20px;
        color: var(--bone);
        font-size: 13.5px;
    }


    /* ========================================================
       HERO
       ======================================================== */

    .hero {
        position: relative;
        padding: 10px 0 85px 0;
        overflow: hidden;
    }

    .eyebrow {
        font-family: 'Fraunces', serif;
        font-size: 14px;
        font-style: italic;
        color: var(--gold);
        margin-bottom: 18px;
    }

    .hero-title {
        max-width: 640px;

        font-family: 'Fraunces', serif;
        font-size: 56px;
        line-height: 1.06;
        font-weight: 500;
        letter-spacing: -0.3px;

        color: var(--bone);

        margin: 0 0 22px 0;
    }

    .hero-description {
        max-width: 600px;

        color: var(--bone-dim);
        font-size: 16.5px;
        line-height: 1.65;

        margin-bottom: 30px;
    }


    /* ========================================================
       ECG
       ======================================================== */

    .ecg {
        position: absolute;
        left: -8%;
        right: -8%;
        bottom: 35px;

        height: 115px;

        opacity: 0.45;
        pointer-events: none;
    }

    .ecg svg {
        width: 100%;
        height: 100%;
    }

    .ecg polyline {
        fill: none;
        stroke: var(--gold);
        stroke-width: 1.3;
        stroke-linejoin: round;
        stroke-linecap: round;
    }


    /* ========================================================
       DISCLAIMER
       ======================================================== */

    .disclaimer {
        border: 1px solid var(--line);
        background: var(--ink-2);

        padding: 18px 22px;
        margin-bottom: 85px;

        color: var(--bone-dim);
        font-size: 13px;
        line-height: 1.6;
    }

    .disclaimer strong {
        color: var(--gold);
        font-weight: 500;
    }


    /* ========================================================
       SECTION HEADINGS
       ======================================================== */

    .section-eyebrow {
        font-family: 'Fraunces', serif;
        font-style: italic;

        color: var(--gold);
        font-size: 14px;

        margin-bottom: 10px;
    }

    .section-title {
        font-family: 'Fraunces', serif;

        font-size: 30px;
        line-height: 1.1;

        font-weight: 500;

        color: var(--bone);

        margin-bottom: 35px;
    }


    /* ========================================================
       DISEASE INDEX
       ======================================================== */

    .disease-list {
        border-top: 1px solid var(--line);
        margin-bottom: 100px;
    }

    .disease-row {
        display: grid;
        grid-template-columns: 64px 1fr 140px;

        align-items: center;

        min-height: 92px;

        border-bottom: 1px solid var(--line);
    }

    .disease-number {
        font-family: 'Fraunces', serif;
        font-style: italic;
        font-size: 15px;
        color: var(--bone-dim);
    }

    .disease-name {
        font-family: 'Fraunces', serif;
        font-size: 22px;
        font-weight: 500;
        color: var(--bone);

        transition: color 0.15s ease;
    }

    .disease-row:hover .disease-name {
        color: var(--gold);
    }

    .disease-description {
        font-size: 13px;
        color: var(--bone-dim);
        margin-top: 4px;
    }

    .disease-meta {
        text-align: right;
        color: var(--bone-dim);
        font-size: 12.5px;
        line-height: 1.5;
    }

    .available {
        color: var(--moss);
        font-weight: 500;
    }


    /* ========================================================
       SELECTOR
       ======================================================== */

    .select-label {
        color: var(--bone-dim);
        font-size: 13px;
        margin-bottom: 8px;
    }


    /* ========================================================
       PREDICTION MODULE
       ======================================================== */

    .prediction-section {
        margin-top: 10px;
        margin-bottom: 50px;
    }

    .module-label {
        font-family: 'Fraunces', serif;
        font-style: italic;

        color: var(--gold);
        font-size: 14px;

        margin-bottom: 6px;
    }

    .module-title {
        font-family: 'Fraunces', serif;

        font-size: 24px;
        font-weight: 500;

        color: var(--bone);

        margin-bottom: 6px;
    }

    .module-description {
        color: var(--bone-dim);
        font-size: 13.5px;
        margin-bottom: 30px;
    }


    /* ========================================================
       PIPELINE
       ======================================================== */

    .pipeline-strip {
        display: flex;
        align-items: stretch;

        margin-bottom: 34px;

        border: 1px solid var(--line);
    }

    .pstep {
        flex: 1;

        display: flex;
        align-items: center;

        gap: 10px;

        padding: 14px 16px;

        border-right: 1px solid var(--line);

        font-size: 12.5px;
        color: var(--bone-dim);

        transition:
            background 0.3s ease,
            color 0.3s ease;
    }

    .pstep:last-child {
        border-right: none;
    }

    .pstep-no {
        width: 20px;
        height: 20px;

        flex: none;

        border-radius: 50%;

        border: 1px solid var(--line);

        display: flex;
        align-items: center;
        justify-content: center;

        font-family: 'Fraunces', serif;
        font-size: 11px;
    }

    .pstep.active .pstep-no {
        background: var(--gold);
        border-color: var(--gold);
        color: var(--ink);
    }

    .pstep.active {
        color: var(--bone);
    }

    .pstep.done .pstep-no {
        background: var(--moss);
        border-color: var(--moss);
        color: var(--ink);
    }


    /* ========================================================
       INPUTS
       ======================================================== */

    div[data-baseweb="input"] {
        background-color: transparent;
        border: none;
        border-bottom: 1px solid var(--line);
        border-radius: 0;
    }

    div[data-baseweb="input"]:focus-within {
        border-bottom: 1px solid var(--gold);
    }

    input {
        color: var(--bone) !important;
        background-color: transparent !important;

        font-family: 'Fraunces', serif !important;
        font-size: 16px !important;
    }

    label {
        color: var(--bone-dim) !important;
        font-size: 12px !important;
    }

    div[data-testid="stNumberInput"] {
        margin-bottom: 15px;
    }


    /* ========================================================
       SELECTBOX
       ======================================================== */

    div[data-baseweb="select"] > div {
        background-color: var(--ink-2);
        border: 1px solid var(--line);
        border-radius: 0;
    }

    div[data-baseweb="select"] span {
        color: var(--bone);
    }


    /* ========================================================
       BUTTON
       ======================================================== */

    div.stButton > button {
        background-color: var(--gold);

        color: var(--ink);

        border: none;
        border-radius: 100px;

        padding: 12px 26px;

        font-family: 'Inter', sans-serif;
        font-size: 14.5px;
        font-weight: 600;

        transition: all 0.2s ease;
    }

    div.stButton > button:hover {
        background-color: #e8bb58;
        color: var(--ink);
        border: none;
    }


    /* ========================================================
       RESULT CARD
       ======================================================== */

    .result-card {
        background-color: var(--ink-2);
        border: 1px solid var(--line);

        padding: 34px;

        min-height: 420px;

        margin-top: 5px;
    }

    .result-top {
        display: flex;
        justify-content: space-between;

        color: var(--bone-dim);
        font-size: 12.5px;

        margin-bottom: 26px;
    }

    .result-probability {
        font-family: 'Fraunces', serif;

        font-size: 64px;
        line-height: 1;

        font-weight: 500;

        color: var(--bone);

        margin-bottom: 6px;
    }

    .result-label {
        color: var(--bone-dim);
        font-size: 13px;
    }

    .gauge-bar {
        height: 3px;
        background: var(--line);

        margin: 24px 0 26px;

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

        font-size: 17px;
        font-style: italic;

        margin-bottom: 22px;
    }

    .status-high {
        color: var(--rose);
    }

    .status-low {
        color: var(--moss);
    }

    .factor {
        display: flex;
        justify-content: space-between;

        padding: 11px 0;

        border-top: 1px solid var(--line);

        font-size: 13.5px;
    }

    .factor:last-of-type {
        border-bottom: 1px solid var(--line);
    }

    .factor span:last-child {
        color: var(--bone-dim);
    }

    .flag-high {
        color: var(--rose) !important;
    }

    .flag-ok {
        color: var(--moss) !important;
    }

    .result-note {
        color: var(--bone-dim);

        font-size: 11.5px;
        font-style: italic;

        font-family: 'Fraunces', serif;

        line-height: 1.6;

        margin-top: 22px;
    }


    /* ========================================================
       COMING SOON
       ======================================================== */

    .coming-soon {
        border: 1px solid var(--line);
        background: var(--ink-2);

        padding: 30px;

        margin-top: 20px;

        color: var(--bone-dim);
    }

    .coming-soon-title {
        font-family: 'Fraunces', serif;

        font-size: 26px;
        font-weight: 500;

        color: var(--bone);

        margin-bottom: 8px;
    }


    /* ========================================================
       FOOTER
       ======================================================== */

    .footer {
        border-top: 1px solid var(--line);

        padding-top: 25px;

        color: var(--bone-dim);

        font-size: 12px;
        line-height: 1.6;
    }

    .footer strong {
        color: var(--bone);
    }


    /* ========================================================
       MOBILE
       ======================================================== */

    @media (max-width: 768px) {

        .block-container {
            padding-left: 25px;
            padding-right: 25px;
        }

        .top-nav {
            margin-left: -25px;
            margin-right: -25px;

            padding-left: 25px;
            padding-right: 25px;
        }

        .nav-links {
            display: none;
        }

        .hero-title {
            font-size: 40px;
        }

        .disease-row {
            grid-template-columns: 40px 1fr;
            padding: 18px 0;
        }

        .disease-meta {
            display: none;
        }

        .result-card {
            margin-top: 30px;
        }

        .pipeline-strip {
            flex-direction: column;
        }

        .pstep {
            border-right: none;
            border-bottom: 1px solid var(--line);
        }

        .pstep:last-child {
            border-bottom: none;
        }
    }

    </style>
    """
)


# ============================================================
# TOP NAVIGATION
# ============================================================

render_html(
    """
    <div class="top-nav">

        <div class="brand">
            <span class="brand-mark">⌁</span>
            Healytics
        </div>

        <div class="nav-links">
            <span>Screenings</span>
            <span>Assess</span>
            <span>Model insights</span>
            <span class="nav-signin">Project demo</span>
        </div>

    </div>
    """
)


# ============================================================
# HERO
# ============================================================

render_html(
    """
    <section class="hero">

        <div class="eyebrow">
            A screening companion, not a diagnosis
        </div>

        <h1 class="hero-title">
            Multi-disease risk prediction,<br>
            in a single workspace
        </h1>

        <p class="hero-description">
            Healytics uses machine learning models to estimate disease risk
            from structured health-related inputs and present the result in a
            clear, interpretable format — surfacing what is worth a
            conversation with your doctor.
        </p>

        <div class="ecg">
            <svg viewBox="0 0 1200 120"
                 preserveAspectRatio="none">

                <polyline points="
                    0,75
                    35,75
                    50,60
                    68,75
                    95,75
                    108,112
                    126,15
                    145,105
                    164,75
                    215,75
                    235,52
                    260,75
                    300,75
                    330,75
                    350,60
                    370,75
                    405,75
                    420,112
                    438,15
                    457,105
                    476,75
                    530,75
                    550,55
                    575,75
                    620,75
                    650,75
                    670,60
                    690,75
                    725,75
                    740,112
                    758,15
                    777,105
                    796,75
                    850,75
                    870,52
                    895,75
                    940,75
                    970,75
                    990,60
                    1010,75
                    1045,75
                    1060,112
                    1078,15
                    1097,105
                    1116,75
                    1200,75
                " />

            </svg>
        </div>

    </section>
    """
)


# ============================================================
# DISCLAIMER
# ============================================================

render_html(
    """
    <div class="disclaimer">
        <strong>Medical Disclaimer</strong><br>
        Healytics is intended for educational and decision-support purposes
        only. Predictions are not medical diagnoses and should not replace
        professional medical advice.
    </div>
    """
)


# ============================================================
# DISEASE INDEX
# ============================================================

render_html(
    """
    <div class="section-eyebrow">
        The index
    </div>

    <div class="section-title">
        Two conditions, one prediction workspace
    </div>
    """
)


render_html(
    """
    <div class="disease-list">

        <div class="disease-row">

            <div class="disease-number">01</div>

            <div>
                <div class="disease-name">
                    Heart Disease
                </div>

                <div class="disease-description">
                    Cardiovascular risk prediction from clinical health features
                </div>
            </div>

            <div class="disease-meta available">
                Available<br>
                13 inputs
            </div>

        </div>


        <div class="disease-row">

            <div class="disease-number">02</div>

            <div>
                <div class="disease-name">
                    Diabetes
                </div>

                <div class="disease-description">
                    Risk prediction using glucose, BMI and related health features
                </div>
            </div>

            <div class="disease-meta available">
                Available<br>
                8 inputs
            </div>

        </div>


        <div class="disease-row">

            <div class="disease-number">03</div>

            <div>
                <div class="disease-name">
                    Liver Disease
                </div>

                <div class="disease-description">
                    Risk prediction from biochemical and demographic features
                </div>
            </div>

            <div class="disease-meta">
                Coming soon<br>
                10 inputs
            </div>

        </div>

    </div>
    """
)


# ============================================================
# DISEASE SELECTOR
# ============================================================

render_html(
    '<div class="select-label">Prediction module</div>'
)

disease = st.selectbox(
    "Select disease",
    [
        "— Select a condition —",
        "Heart Disease",
        "Diabetes",
        "Liver Disease"
    ],
    label_visibility="collapsed"
)


# ============================================================
# COMMON PIPELINE
# ============================================================

PIPELINE_STEPS = [
    "Raw input captured",
    "Missing readings imputed",
    "Features standardized",
    "Model inference",
]


def render_pipeline_strip(
    placeholder,
    active_index=-1,
    done_until=-1
):

    rows = ""

    for i, label in enumerate(PIPELINE_STEPS):

        state = ""

        if i <= done_until:
            state = "done"

        elif i == active_index:
            state = "active"

        rows += (
            f'<div class="pstep {state}">'
            f'<span class="pstep-no">{i + 1}</span>'
            f'<span>{label}</span>'
            f'</div>'
        )

    placeholder.markdown(
        flatten_html(
            f'<div class="pipeline-strip">{rows}</div>'
        ),
        unsafe_allow_html=True
    )


# ============================================================
# HEART DISEASE MODULE
# ============================================================

if disease == "Heart Disease":

    render_html(
        """
        <div class="prediction-section">

            <div class="module-label">
                01 — Heart Disease
            </div>

            <div class="module-title">
                Patient values
            </div>

            <div class="module-description">
                Enter the required clinical values to generate a
                machine learning-based cardiovascular risk estimate.
            </div>

        </div>
        """
    )

    pipeline_placeholder = st.empty()

    render_pipeline_strip(
        pipeline_placeholder
    )

    left_col, right_col = st.columns(
        [1.05, 0.95],
        gap="large"
    )


    # ========================================================
    # HEART INPUTS
    # ========================================================

    with left_col:

        age = st.number_input(
            "Age, years",
            min_value=1,
            max_value=120,
            value=63,
            step=1
        )

        sex_label = st.selectbox(
            "Sex",
            ["Female", "Male"],
            index=1
        )

        # Dataset encoding: Female = 0, Male = 1
        sex = 1 if sex_label == "Male" else 0

        cp_label = st.selectbox(
            "Chest pain type",
            [
                "Typical angina",
                "Atypical angina",
                "Non-anginal pain",
                "Asymptomatic"
            ],
            index=0
        )

        # Cleveland dataset encoding:
        # 1 = Typical angina
        # 2 = Atypical angina
        # 3 = Non-anginal pain
        # 4 = Asymptomatic
        cp = {
            "Typical angina": 1,
            "Atypical angina": 2,
            "Non-anginal pain": 3,
            "Asymptomatic": 4
        }[cp_label]

        trestbps = st.number_input(
            "Resting blood pressure, mmHg",
            min_value=0.0,
            max_value=300.0,
            value=145.0,
            step=1.0
        )

        chol = st.number_input(
            "Cholesterol, mg/dL",
            min_value=0.0,
            max_value=700.0,
            value=233.0,
            step=1.0
        )

        fbs_label = st.selectbox(
            "Fasting blood sugar",
            [
                "≤ 120 mg/dL",
                "> 120 mg/dL"
            ],
            index=1
        )

        # Dataset encoding: 0 = false, 1 = true
        fbs = 1 if fbs_label == "> 120 mg/dL" else 0

        restecg_label = st.selectbox(
            "Resting ECG",
            [
                "Normal",
                "ST-T wave abnormality",
                "Left ventricular hypertrophy"
            ],
            index=2
        )

        # Cleveland dataset encoding: 0, 1, 2
        restecg = {
            "Normal": 0,
            "ST-T wave abnormality": 1,
            "Left ventricular hypertrophy": 2
        }[restecg_label]


    with right_col:

        thalach = st.number_input(
            "Maximum heart rate",
            min_value=0.0,
            max_value=250.0,
            value=150.0,
            step=1.0
        )

        exang_label = st.selectbox(
            "Exercise-induced angina",
            ["No", "Yes"],
            index=0
        )

        # Dataset encoding: 0 = no, 1 = yes
        exang = 1 if exang_label == "Yes" else 0

        oldpeak = st.number_input(
            "ST depression",
            min_value=0.0,
            max_value=10.0,
            value=2.3,
            step=0.1
        )

        slope_label = st.selectbox(
            "Slope of peak exercise ST segment",
            [
                "Upsloping",
                "Flat",
                "Downsloping"
            ],
            index=2
        )

        # Cleveland dataset encoding: 1 = upsloping, 2 = flat, 3 = downsloping
        slope = {
            "Upsloping": 1,
            "Flat": 2,
            "Downsloping": 3
        }[slope_label]

        ca_label = st.selectbox(
            "Major vessels colored by fluoroscopy",
            [
                "0 vessels",
                "1 vessel",
                "2 vessels",
                "3 vessels"
            ],
            index=0
        )

        ca = {
            "0 vessels": 0,
            "1 vessel": 1,
            "2 vessels": 2,
            "3 vessels": 3
        }[ca_label]

        thal_label = st.selectbox(
            "Thalassemia",
            [
                "Normal",
                "Fixed defect",
                "Reversible defect"
            ],
            index=1
        )

        # Cleveland dataset encoding: 3 = normal, 6 = fixed defect, 7 = reversible defect
        thal = {
            "Normal": 3,
            "Fixed defect": 6,
            "Reversible defect": 7
        }[thal_label]


    st.write("")

    predict_button = st.button(
        "Run this screening",
        type="primary"
    )


    # ========================================================
    # HEART PREDICTION
    # ========================================================

    if predict_button:

        input_data = {
            "age": age,
            "sex": sex,
            "cp": cp,
            "trestbps": trestbps,
            "chol": chol,
            "fbs": fbs,
            "restecg": restecg,
            "thalach": thalach,
            "exang": exang,
            "oldpeak": oldpeak,
            "slope": slope,
            "ca": ca,
            "thal": thal
        }

        try:

            # ------------------------------------------------
            # PIPELINE ANIMATION
            # ------------------------------------------------

            for i in range(len(PIPELINE_STEPS)):

                render_pipeline_strip(
                    pipeline_placeholder,
                    active_index=i,
                    done_until=i - 1
                )

                time.sleep(0.25)


            render_pipeline_strip(
                pipeline_placeholder,
                active_index=-1,
                done_until=len(PIPELINE_STEPS) - 1
            )


            # ------------------------------------------------
            # MODEL PREDICTION
            # ------------------------------------------------

            result = predict_heart_disease(
                input_data
            )

            prediction = int(
                result["prediction"]
            )

            probability = float(
                result["probability"]
            )


            # ------------------------------------------------
            # RESULT
            # ------------------------------------------------

            is_high_risk = prediction == 1

            status_text = (
                "Higher predicted heart disease risk estimate"
                if is_high_risk
                else
                "Lower predicted heart disease risk estimate"
            )

            status_class = (
                "status-high"
                if is_high_risk
                else
                "status-low"
            )

            fill_color = (
                "#C56A52"
                if is_high_risk
                else
                "#7E9A78"
            )

            fill_pct = max(
                4,
                min(
                    100,
                    round(probability * 100)
                )
            )


            # ------------------------------------------------
            # FACTOR ROW
            # ------------------------------------------------

            def factor_row(
                label,
                value_text,
                is_flag
            ):

                flag_class = (
                    "flag-high"
                    if is_flag
                    else
                    "flag-ok"
                )

                return f"""
                <div class="factor">
                    <span>{label}</span>
                    <span class="{flag_class}">
                        {value_text}
                    </span>
                </div>
                """


            factors_html = "".join([

                factor_row(
                    "Age",
                    "Higher age range"
                    if age >= 60
                    else "Within lower range",
                    age >= 60
                ),

                factor_row(
                    "Resting blood pressure",
                    "Above typical range"
                    if trestbps >= 140
                    else "Within range",
                    trestbps >= 140
                ),

                factor_row(
                    "Cholesterol",
                    "Elevated"
                    if chol >= 240
                    else "Within range",
                    chol >= 240
                ),

                factor_row(
                    "Maximum heart rate",
                    "Lower observed value"
                    if thalach < 120
                    else "Within observed range",
                    thalach < 120
                ),

                factor_row(
                    "Exercise-induced angina",
                    "Yes"
                    if exang == 1
                    else "No",
                    exang == 1
                ),

            ])


            # ------------------------------------------------
            # RESULT CARD
            # ------------------------------------------------

            render_html(
                f"""
                <div class="result-card">

                    <div class="result-top">
                        <span>
                            Estimated risk
                        </span>

                        <span>
                            Heart Disease pipeline
                        </span>
                    </div>


                    <div class="result-probability">
                        {probability:.2%}
                    </div>


                    <div class="result-label">
                        Model probability for the positive class
                    </div>


                    <div class="gauge-bar">

                        <div
                            class="gauge-fill"
                            style="
                                width:{fill_pct}%;
                                background:{fill_color};
                            "
                        ></div>

                    </div>


                    <div class="result-status {status_class}">
                        {status_text}
                    </div>


                    {factors_html}


                    <div class="result-note">
                        This is a statistical model estimate, not a
                        clinical diagnosis — bring this reading to
                        a qualified healthcare professional.
                    </div>

                </div>
                """
            )


        except Exception as e:

            st.error(
                f"Heart Disease prediction could not be generated: {e}"
            )


# ============================================================
# DIABETES MODULE
# ============================================================

elif disease == "Diabetes":

    render_html(
        """
        <div class="prediction-section">

            <div class="module-label">
                02 — Diabetes
            </div>

            <div class="module-title">
                Patient values
            </div>

            <div class="module-description">
                Enter the required health-related values to generate a
                machine learning-based prediction.
            </div>

        </div>
        """
    )


    pipeline_placeholder = st.empty()

    render_pipeline_strip(
        pipeline_placeholder
    )


    left_col, right_col = st.columns(
        [1.05, 0.95],
        gap="large"
    )


    # ========================================================
    # DIABETES INPUT FORM
    # ========================================================

    with left_col:

        pregnancies = st.number_input(
            "Pregnancies",
            min_value=0,
            max_value=20,
            value=1,
            step=1
        )

        age = st.number_input(
            "Age, years",
            min_value=1,
            max_value=120,
            value=30,
            step=1
        )

        glucose = st.number_input(
            "Glucose",
            min_value=0.0,
            max_value=250.0,
            value=120.0,
            step=1.0
        )

        blood_pressure = st.number_input(
            "Blood Pressure",
            min_value=0.0,
            max_value=150.0,
            value=70.0,
            step=1.0
        )


    with right_col:

        bmi = st.number_input(
            "BMI",
            min_value=0.0,
            max_value=70.0,
            value=30.0,
            step=0.1
        )

        skin_thickness = st.number_input(
            "Skin Thickness",
            min_value=0.0,
            max_value=100.0,
            value=25.0,
            step=1.0
        )

        insulin = st.number_input(
            "Insulin",
            min_value=0.0,
            max_value=900.0,
            value=100.0,
            step=1.0
        )

        diabetes_pedigree = st.number_input(
            "Diabetes Pedigree Function",
            min_value=0.0,
            max_value=3.0,
            value=0.45,
            step=0.01
        )


    st.write("")

    predict_button = st.button(
        "Run this screening",
        type="primary"
    )


    # ========================================================
    # DIABETES PREDICTION
    # ========================================================

    if predict_button:

        invalid_values = []

        if glucose <= 0:
            invalid_values.append("Glucose")

        if blood_pressure <= 0:
            invalid_values.append("Blood Pressure")

        if skin_thickness <= 0:
            invalid_values.append("Skin Thickness")

        if insulin <= 0:
            invalid_values.append("Insulin")

        if bmi <= 0:
            invalid_values.append("BMI")


        if invalid_values:

            st.warning(
                "Please enter valid positive values for: "
                + ", ".join(invalid_values)
            )

        else:

            for i in range(
                len(PIPELINE_STEPS)
            ):

                render_pipeline_strip(
                    pipeline_placeholder,
                    active_index=i,
                    done_until=i - 1
                )

                time.sleep(0.25)


            render_pipeline_strip(
                pipeline_placeholder,
                active_index=-1,
                done_until=len(PIPELINE_STEPS) - 1
            )


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

                result = predict_diabetes(
                    input_data
                )

                prediction = result["prediction"]
                probability = result["probability"]


                is_high_risk = prediction == 1

                status_text = (
                    "Higher predicted diabetes risk estimate"
                    if is_high_risk
                    else
                    "Lower predicted diabetes risk estimate"
                )

                status_class = (
                    "status-high"
                    if is_high_risk
                    else
                    "status-low"
                )

                fill_color = (
                    "#C56A52"
                    if is_high_risk
                    else
                    "#7E9A78"
                )

                fill_pct = max(
                    4,
                    min(
                        100,
                        round(probability * 100)
                    )
                )


                def factor_row(
                    label,
                    value_text,
                    is_flag
                ):

                    flag_class = (
                        "flag-high"
                        if is_flag
                        else
                        "flag-ok"
                    )

                    return f"""
                    <div class="factor">
                        <span>{label}</span>
                        <span class="{flag_class}">
                            {value_text}
                        </span>
                    </div>
                    """


                factors_html = "".join([

                    factor_row(
                        "Glucose",
                        "Above typical range"
                        if glucose >= 140
                        else "Within range",
                        glucose >= 140
                    ),

                    factor_row(
                        "BMI",
                        "Contributing factor"
                        if bmi >= 30
                        else "Within range",
                        bmi >= 30
                    ),

                    factor_row(
                        "Blood Pressure",
                        "Above typical range"
                        if blood_pressure >= 90
                        else "Within range",
                        blood_pressure >= 90
                    ),

                    factor_row(
                        "Diabetes Pedigree",
                        "Elevated"
                        if diabetes_pedigree >= 0.5
                        else "Within range",
                        diabetes_pedigree >= 0.5
                    ),

                ])


                render_html(
                    f"""
                    <div class="result-card">

                        <div class="result-top">
                            <span>
                                Estimated risk
                            </span>

                            <span>
                                Diabetes pipeline
                            </span>
                        </div>


                        <div class="result-probability">
                            {probability:.2%}
                        </div>


                        <div class="result-label">
                            Model probability for the positive class
                        </div>


                        <div class="gauge-bar">

                            <div
                                class="gauge-fill"
                                style="
                                    width:{fill_pct}%;
                                    background:{fill_color};
                                "
                            ></div>

                        </div>


                        <div class="result-status {status_class}">
                            {status_text}
                        </div>


                        {factors_html}


                        <div class="result-note">
                            This is a statistical model estimate, not a
                            clinical diagnosis — bring this reading to
                            a qualified healthcare professional.
                        </div>

                    </div>
                    """
                )


            except Exception as e:

                st.error(
                    f"Diabetes prediction could not be generated: {e}"
                )


# ============================================================
# LIVER DISEASE
# ============================================================

elif disease == "Liver Disease":

    render_html(
        """
        <div class="coming-soon">

            <div class="coming-soon-title">
                Liver Disease
            </div>

            <div>
                Risk prediction using biochemical and demographic
                features.
            </div>

            <br>

            <div style="color:#D9A441;">
                Prediction module coming soon.
            </div>

        </div>
        """
    )


# ============================================================
# NO DISEASE SELECTED
# ============================================================

else:

    render_html(
        """
        <div class="coming-soon">

            <div class="coming-soon-title">
                Select a condition
            </div>

            <div>
                Choose a screening module above to begin.
            </div>

        </div>
        """
    )


# ============================================================
# FOOTER
# ============================================================

render_html(
    """
    <div class="footer">

        <strong>Healytics</strong> —
        AI-Based Multi-Disease Risk Prediction System.

        <br><br>

        Built for educational and decision-support purposes.
        Model outputs are not medical diagnoses.

    </div>
    """
)