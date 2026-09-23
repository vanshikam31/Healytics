import os
import joblib
import pandas as pd


MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "..",
    "..",
    "models",
    "diabetes_pipeline.joblib"
)


FEATURE_NAMES = [
    "Pregnancies",
    "Glucose",
    "BloodPressure",
    "SkinThickness",
    "Insulin",
    "BMI",
    "DiabetesPedigreeFunction",
    "Age"
]


def load_model():
    """
    Load the saved Diabetes prediction pipeline.
    """
    return joblib.load(MODEL_PATH)


def predict_diabetes(input_data):
    """
    Generate a Diabetes prediction and probability.

    Parameters
    ----------
    input_data : dict
        Dictionary containing all required Diabetes features.

    Returns
    -------
    dict
        Prediction and probability.
    """

    missing_features = [
        feature
        for feature in FEATURE_NAMES
        if feature not in input_data
    ]

    if missing_features:
        raise ValueError(
            f"Missing required features: {missing_features}"
        )

    input_df = pd.DataFrame(
        [input_data],
        columns=FEATURE_NAMES
    )

    model = load_model()

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0, 1]

    return {
        "prediction": int(prediction),
        "probability": float(probability)
    }