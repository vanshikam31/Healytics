# Healytics — Dataset Documentation

## Dataset Selection

Healytics uses four disease-specific datasets from established public
machine-learning repositories.

| Disease | Dataset | Source |
|---|---|---|
| Diabetes | Pima Indians Diabetes Database | UCI-derived |
| Heart Disease | UCI Heart Disease — Cleveland | UCI Machine Learning Repository |
| Liver Disease | ILPD (Indian Liver Patient Dataset) | UCI Machine Learning Repository |
| Parkinson's Disease | Oxford Parkinson's Disease Detection Dataset | UCI Machine Learning Repository |

---

## 1. Diabetes

### Dataset
Pima Indians Diabetes Database

### Task
Binary classification.

### Features
- Pregnancies
- Glucose
- BloodPressure
- SkinThickness
- Insulin
- BMI
- DiabetesPedigreeFunction
- Age

### Target
`Outcome`

### Dataset Size
768 instances with 8 input features and one target variable.

### Population Limitation
The dataset consists of women aged 21 or older from the Pima Indian population.
This limitation must be considered when interpreting model performance.

### Source
UCI-derived Pima Indians Diabetes Database.

---

## 2. Heart Disease

### Dataset
UCI Heart Disease — Cleveland

### Task
Classification.

### Features
- age
- sex
- cp
- trestbps
- chol
- fbs
- restecg
- thalach
- exang
- oldpeak
- slope
- ca
- thal

### Target
`num`

The original target uses values 0–4. For binary classification, we will
investigate the transformation:

- 0 → absence of heart disease
- 1–4 → presence of heart disease

This transformation will be implemented and documented during preprocessing.

### Dataset Size
303 instances and 13 commonly used input features.

### Source
UCI Machine Learning Repository — Heart Disease dataset.

---

## 3. Liver Disease

### Dataset
ILPD — Indian Liver Patient Dataset

### Task
Binary classification.

### Features
- Age
- Gender
- TB
- DB
- Alkphos
- Sgpt
- Sgot
- TP
- ALB
- A/G Ratio

### Target
`Selector`

### Dataset Size
583 instances and 10 input features.

### Class Distribution
- Liver disease: 416
- No liver disease: 167

### Population Limitation
The dataset was collected from patients in the Northeast of Andhra Pradesh, India.

### Source
UCI Machine Learning Repository.

---

## 4. Parkinson's Disease

### Dataset
Oxford Parkinson's Disease Detection Dataset

### Task
Binary classification.

### Features
Voice-based biomedical measurements including frequency,
jitter, shimmer, noise-to-harmonic ratio, nonlinear measures,
and related voice characteristics.

### Target
`status`

- 0 → healthy
- 1 → Parkinson's disease

### Dataset Structure
The UCI documentation describes voice recordings from 31 people,
with multiple recordings per person.

### Important Validation Consideration
Multiple recordings belong to the same individual. Therefore, a
patient/group-aware train-test split must be considered during model
development to reduce the risk of data leakage.

### Source
UCI Machine Learning Repository.

---

## Dataset Handling Policy

Raw datasets will not be committed to the GitHub repository.

The repository will contain dataset documentation and source information,
while raw data will remain local and be excluded through `.gitignore`.

This keeps the repository lightweight and avoids unnecessarily redistributing
raw datasets.

---

## Next Step

Milestone 3 — Data Preprocessing.

Each dataset will be inspected independently before preprocessing.
No common preprocessing pipeline will be blindly applied to all diseases.