import joblib
import pandas as pd
from pathlib import Path


# Project root
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Model path
MODEL_PATH = PROJECT_ROOT / "models" / "liver_disease_pipeline.joblib"


# Load trained pipeline
liver_model = joblib.load(MODEL_PATH)


def predict_liver_disease(
    age,
    gender,
    total_bilirubin,
    direct_bilirubin,
    alkaline_phosphotase,
    alamine_aminotransferase,
    aspartate_aminotransferase,
    total_proteins,
    albumin,
    albumin_and_globulin_ratio
):
    input_data = pd.DataFrame([{
        "Age": age,
        "Gender": gender,
        "Total_Bilirubin": total_bilirubin,
        "Direct_Bilirubin": direct_bilirubin,
        "Alkaline_Phosphotase": alkaline_phosphotase,
        "Alamine_Aminotransferase": alamine_aminotransferase,
        "Aspartate_Aminotransferase": aspartate_aminotransferase,
        "Total_Proteins": total_proteins,
        "Albumin": albumin,
        "Albumin_and_Globulin_Ratio": albumin_and_globulin_ratio
    }])

    prediction = liver_model.predict(input_data)[0]

    probabilities = liver_model.predict_proba(input_data)[0]

    # Probability corresponding to the predicted class
    predicted_class_index = list(liver_model.classes_).index(prediction)

    predicted_probability = probabilities[predicted_class_index]

    if prediction == 1:
        result = "Liver Disease"
    else:
        result = "No Liver Disease"

    return {
        "prediction": int(prediction),
        "result": result,
        "risk_probability": float(predicted_probability)
    }