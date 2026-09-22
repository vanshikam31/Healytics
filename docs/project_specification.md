# Healytics — Project Specification

## 1. Project Title
**Healytics: An AI-Based Multi-Disease Risk Prediction System**

## 2. Problem Statement
Healytics aims to provide an educational machine-learning-based system that analyzes disease-specific health parameters and produces a model-based risk/classification prediction through a unified application.

## 3. Proposed Solution
Users select a disease and enter the parameters required by that disease's trained model. The system validates the input, applies the corresponding preprocessing pipeline, generates a prediction, and presents the result with appropriate model-level explanation.

Each disease uses an independent model because datasets, features, and preprocessing requirements differ.

## 4. Initial Diseases
1. Diabetes
2. Heart Disease
3. Liver Disease
4. Parkinson's Disease

## 5. Objectives
- Collect and document suitable datasets.
- Clean and preprocess disease-specific data.
- Perform exploratory data analysis.
- Compare multiple classification algorithms.
- Tune and validate selected models.
- Save models and preprocessing artifacts.
- Build a unified Streamlit application.
- Add explainability where appropriate.
- Deploy and document the system.

## 6. Scope
### Included
- Multi-disease classification
- Data preprocessing
- EDA
- Feature engineering where justified
- Model comparison
- Hyperparameter tuning
- Evaluation
- Model serialization
- Web interface
- Input validation
- Explainability
- Deployment

### Excluded
- Medical diagnosis
- Prescription generation
- Treatment recommendations
- Emergency decision-making
- Replacement of professional medical assessment

## 7. Core Features
- Disease selection
- Disease-specific dynamic input forms
- Input validation
- Disease-specific model loading
- Prediction
- Probability display where appropriate
- Model explainability
- Educational disease information
- Safety/medical-use disclaimer

## 8. Functional Requirements
- FR1: User can select a disease.
- FR2: System displays disease-specific inputs.
- FR3: System validates inputs.
- FR4: System loads the appropriate model.
- FR5: System applies the correct preprocessing.
- FR6: System generates a prediction.
- FR7: System displays the prediction.
- FR8: System can display model probability where appropriate.
- FR9: System can display model explanations.
- FR10: System handles invalid input without crashing.

## 9. Non-Functional Requirements
- Fast prediction response.
- Reliable input validation and error handling.
- Independent maintainability of disease modules.
- Extensible architecture for additional diseases.
- Reproducible ML workflow.
- Simple user interface.

## 10. Technology Stack
- Python 3.x
- Pandas
- NumPy
- Scikit-learn
- XGBoost where justified
- Matplotlib
- Seaborn
- Plotly
- SHAP
- Streamlit
- Git/GitHub

## 11. ML Workflow
Dataset → Data Understanding → Cleaning → EDA → Train/Test Split → Preprocessing → Baseline Models → Model Comparison → Hyperparameter Tuning → Cross-validation → Final Evaluation → Model Saving → Application Integration

Accuracy will not be the only evaluation criterion. Precision, recall, F1-score, ROC-AUC, confusion matrix, class distribution, and cross-validation results will also be considered.

## 12. System Architecture
User → Streamlit Interface → Input Validation → Disease-Specific Preprocessor → Disease-Specific Model → Prediction → Explanation/Result

## 13. Repository Structure
See the root README for the current repository structure.

## 14. Development Rule
Every completed milestone must be tested, documented, committed, and pushed to GitHub before the next milestone begins.
