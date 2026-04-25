"""
Prediction Pipeline API.
This module defines the main API endpoints for handling requests,
including health checks and prediction inference.
"""

from fastapi import FastAPI
import pandas as pd
from pipeline.prediction_pipeline import PredictionPipeline
from api.schemas import InputData
app = FastAPI(title="Financial ML API")
pipeline = PredictionPipeline()
@app.get("/")
def home():
    """
    Root endpoint for the API.
    Returns:
        dict: A welcome message indicating that the API is running.
    """
    return {"message": "Financial ML API is running"}

@app.get("/health")
def health():
    """
    Health check endpoint.
    Used to verify that the API service is up and running.
    Returns:
        dict: Status message confirming service availability.
    """
    return {"status": "ok"}


@app.post("/predict")
def predict(data: InputData):
    """
    Prediction endpoint for the pipeline.
    Accepts input data, processes it through the trained model,
    and returns prediction results.
    Returns:
        dict: Model predictions along with any relevant metadata.
    Raises:
        ValueError: If input data is invalid or missing.
        Exception: If prediction pipeline fails during execution.
    """
    df = pd.DataFrame([data.dict()])
    preds, probs = pipeline.predict(df)
    return {
        "prediction": int(preds[0]),
        "probability": float(probs[0]) if probs is not None else None
    }