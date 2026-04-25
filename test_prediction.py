"""
Prediction Pipeline Test Script.
Creates a sample input, runs it through the prediction pipeline,
and prints the predicted output and probability of the stock price.
"""
from pipeline.prediction_pipeline import PredictionPipeline
import pandas as pd

pipeline = PredictionPipeline()
sample = {
    "Close": 150.0,
    "High": 152.0,
    "Low": 148.0,
    "Open": 149.5,
    "Volume": 1000000,
    "Returns": 0.01,
    "Ma_7": 148.5,
    "Ma_30": 145.0,
    "Volatility": 0.02,
    "Lag_1": 0.005
}

df = pd.DataFrame([sample])

preds, probs = pipeline.predict(df)

print("Prediction:", preds)
print("Probability:", probs)
