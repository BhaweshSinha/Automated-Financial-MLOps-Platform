"""
Baseline Model Training and Evaluation Pipeline.
Loads training and testing datasets, applies target engineering and feature
scaling, trains a baseline model, evaluates its performance, and saves
the trained model along with evaluation metrics.
"""

import pandas as pd
import yaml
import json

from src.baseline_model import train_baseline, save_model
from src.model_evaluator import evaluate_model
from src.utils_model import load_scaler, apply_scaler
from src.target_engineering import create_target

TRAIN_PATH = "data/splits/train.csv"
TEST_PATH = "data/splits/test.csv"


def run():
    """
    Execute the baseline model pipeline.
    This function performs the following steps:
    - Loads configuration parameters
    - Reads training and testing datasets
    - Applies target engineering
    - Prepares feature matrices and target variables
    - Applies feature scaling using a pre-fitted scaler
    - Trains a baseline model
    - Evaluates model performance on test data
    - Saves the trained model and evaluation metrics
    Returns:
        None
    Raises:
        AssertionError: If training and testing feature columns do not match.
        Exception: If any step in the pipeline fails.
    """
    with open("configs/model.yaml", "r") as f:
        config = yaml.safe_load(f)

    train = pd.read_csv(TRAIN_PATH)
    test = pd.read_csv(TEST_PATH)

    train = create_target(train)
    test = create_target(test)

    drop_cols = ["Date", "Ticker", "Returns", "Lag_1"]

    X_train = train.drop("target", axis=1).drop(columns=drop_cols, errors="ignore")
    y_train = train["target"]

    X_test = test.drop("target", axis=1).drop(columns=drop_cols, errors="ignore")
    y_test = test["target"]
    scaler = load_scaler(config["scaler_path"])
    scale_cols = ['Close', 'Ma_7', 'Ma_30', 'Volatility']
    X_train[scale_cols] = apply_scaler(scaler, X_train[scale_cols])
    X_test[scale_cols] = apply_scaler(scaler, X_test[scale_cols])
    assert list(X_train.columns) == list(X_test.columns), "Feature mismatch!"
    model = train_baseline(X_train, y_train)
    metrics = evaluate_model(model, X_test, y_test)

    save_model(model, config["baseline_model_path"])
    with open(config["baseline_metrics_path"], "w") as f:
        json.dump(metrics, f, indent=4)

    print("\n Baseline Pipeline Completed")
    print("Metrics:", metrics)


if __name__ == "__main__":
    run()