import os
import joblib


# ============================================================
# MODEL PATH
# ============================================================

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

MODEL_PATH = (
    PROJECT_ROOT
    / "models"
    / "heart_disease_pipeline.joblib"
)

print("Heart model path:", MODEL_PATH)
print("Heart model exists:", MODEL_PATH.exists())


# ============================================================
# REQUIRED FEATURES
# ============================================================

REQUIRED_FEATURES = [
    "age",
    "sex",
    "cp",
    "trestbps",
    "chol",
    "fbs",
    "restecg",
    "thalach",
    "exang",
    "oldpeak",
    "slope",
    "ca",
    "thal"
]


# ============================================================
# LOAD MODEL
# ============================================================

heart_disease_pipeline = joblib.load(MODEL_PATH)


# ============================================================
# PREDICTION FUNCTION
# ============================================================

def predict_heart_disease(input_data):
    """
    Predict heart disease risk.

    Parameters
    ----------
    input_data : dict
        Dictionary containing all required heart disease features.

    Returns
    -------
    dict
        Prediction and probability.
    """

    # --------------------------------------------------------
    # Validate input
    # --------------------------------------------------------

    missing_features = [
        feature
        for feature in REQUIRED_FEATURES
        if feature not in input_data
    ]

    if missing_features:
        raise ValueError(
            f"Missing required features: {missing_features}"
        )

    # --------------------------------------------------------
    # Keep only expected features and preserve order
    # --------------------------------------------------------

    ordered_data = {
        feature: input_data[feature]
        for feature in REQUIRED_FEATURES
    }

    # --------------------------------------------------------
    # Convert dictionary to DataFrame
    # --------------------------------------------------------

    import pandas as pd

    input_df = pd.DataFrame([ordered_data])

    # --------------------------------------------------------
    # Prediction
    # --------------------------------------------------------

    prediction = heart_disease_pipeline.predict(input_df)[0]

    probability = (
        heart_disease_pipeline
        .predict_proba(input_df)[0][1]
    )

    return {
        "prediction": int(prediction),
        "probability": float(probability)
    }