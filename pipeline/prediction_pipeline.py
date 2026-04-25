"""
Prediction Pipeline.
Handles loading of the trained model and feature schema,
preprocessing of incoming data, and generating predictions
for inference requests.
"""
import joblib
import pandas as pd
import json
import os


class PredictionPipeline:
    """
    End-to-end prediction pipeline for model inference.
    Loads the trained model and required feature schema,
    preprocesses input data, and generates predictions
    along with optional probabilities.
    """
    def __init__(self):
        """
    Initialize the prediction pipeline.
    Loads the trained model and feature configuration from disk.
    Raises:
        FileNotFoundError: If model or feature files are not found.
    """
        print("Loading model and features...")

        model_path = os.path.join("models", "final_pipeline.pkl")
        features_path = os.path.join("models", "features.json")

        if not os.path.exists(model_path):
            raise FileNotFoundError("Model file not found")

        if not os.path.exists(features_path):
            raise FileNotFoundError("Features file not found")

        self.model = joblib.load(model_path)

        with open(features_path, "r") as f:
            self.features = json.load(f)

        print("Model loaded successfully")

    def preprocess(self, data: pd.DataFrame):
        """
    Preprocess input data for prediction.
    Selects and orders features based on the trained model's
    expected input schema.
    Args:
        data (pd.DataFrame): Raw input data.
    Returns:
        pd.DataFrame: Preprocessed data ready for prediction.
    """
        df = data.copy()
        df = df[self.features]

        return df

    def predict(self, data: pd.DataFrame):
        """
    Generate predictions using the trained model.
    Applies preprocessing and returns predictions along with
    class probabilities (if supported by the model).
    Args:
        data (pd.DataFrame): Input data for prediction.
    Returns:
        tuple:
            - preds (array-like): Predicted labels.
            - probs (array-like or None): Prediction probabilities if available.
    """
        df = self.preprocess(data)

        preds = self.model.predict(df)

        if hasattr(self.model, "predict_proba"):
            probs = self.model.predict_proba(df)[:, 1]
        else:
            probs = None

        return preds, probs