import unittest

from src.prediction.heart_disease_predictor import predict_heart_disease


class TestHeartDiseasePredictor(unittest.TestCase):

    def setUp(self):

        self.valid_input = {
            "age": 63,
            "sex": 1,
            "cp": 1,
            "trestbps": 145,
            "chol": 233,
            "fbs": 1,
            "restecg": 2,
            "thalach": 150,
            "exang": 0,
            "oldpeak": 2.3,
            "slope": 3,
            "ca": 0,
            "thal": 6
        }

    def test_valid_prediction(self):

        result = predict_heart_disease(self.valid_input)

        self.assertIn("prediction", result)
        self.assertIn("probability", result)

        self.assertIn(result["prediction"], [0, 1])

        self.assertGreaterEqual(
            result["probability"],
            0.0
        )

        self.assertLessEqual(
            result["probability"],
            1.0
        )

    def test_missing_features(self):

        invalid_input = {
            "age": 63,
            "sex": 1,
            "cp": 1,
            "trestbps": 145
        }

        with self.assertRaises(ValueError):
            predict_heart_disease(invalid_input)


if __name__ == "__main__":
    unittest.main()