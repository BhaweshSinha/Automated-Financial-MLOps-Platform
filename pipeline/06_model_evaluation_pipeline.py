"""
Model Evaluation Pipeline.
Loads the trained model and test dataset, applies preprocessing,
evaluates model performance, and saves the final evaluation metrics.
"""
import pandas as pd
import yaml
import pickle
import json

from src.model_evaluator import evaluate_model
from src.utils_model import load_scaler, apply_scaler
from src.target_engineering import create_target

TEST_PATH = "data/splits/test.csv"


def run():
    """
    Execute the model evaluation pipeline.
    This function performs the following steps:
    - Loads configuration parameters
    - Reads the test dataset
    - Applies target engineering
    - Prepares feature matrix and target variable
    - Applies feature scaling using a pre-fitted scaler
    - Loads the trained model
    - Evaluates model performance on test data
    - Saves evaluation metrics to a file
    Returns:
        None
    Raises:
        Exception: If model loading, preprocessing, or evaluation fails.
    """
    with open("configs/model.yaml", "r") as f:
        config = yaml.safe_load(f)
    test = pd.read_csv(TEST_PATH)
    test = create_target(test)
    drop_cols = ["Date", "Ticker", "Returns", "Lag_1"]

    X_test = test.drop("target", axis=1).drop(columns=drop_cols, errors="ignore")
    y_test = test["target"]
    scaler = load_scaler(config["scaler_path"])

    scale_cols = ['Close', 'Ma_7', 'Ma_30', 'Volatility']

    X_test[scale_cols] = apply_scaler(scaler, X_test[scale_cols])
    with open(config["model_save_path"], "rb") as f:
        model = pickle.load(f)
    metrics = evaluate_model(model, X_test, y_test)
    with open(config["metrics_path"], "w") as f:
        json.dump(metrics, f, indent=4)

    print("Final Metrics:", metrics)

if __name__ == "__main__":
    run()