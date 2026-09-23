import unittest

from src.prediction.diabetes_predictor import predict_diabetes


class TestDiabetesPredictor(unittest.TestCase):

    def setUp(self):
        self.valid_input = {
            "Pregnancies": 2,
            "Glucose": 120,
            "BloodPressure": 70,
            "SkinThickness": 25,
            "Insulin": 100,
            "BMI": 30.5,
            "DiabetesPedigreeFunction": 0.45,
            "Age": 30
        }

    def test_valid_prediction(self):
        result = predict_diabetes(self.valid_input)

        self.assertIn("prediction", result)
        self.assertIn("probability", result)

        self.assertIn(result["prediction"], [0, 1])
        self.assertGreaterEqual(result["probability"], 0)
        self.assertLessEqual(result["probability"], 1)

    def test_missing_features(self):
        incomplete_input = {
            "Pregnancies": 2,
            "Glucose": 120
        }

        with self.assertRaises(ValueError):
            predict_diabetes(incomplete_input)


if __name__ == "__main__":
    unittest.main()