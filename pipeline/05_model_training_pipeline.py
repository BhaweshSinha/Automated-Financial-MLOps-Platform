"""
Model Training and Selection Pipeline.
Trains multiple machine learning models using configured hyperparameters,
evaluates their performance, selects the best-performing model based on
evaluation metrics, and saves both the model and experiment results.
"""
import pandas as pd
import yaml
import pickle
import json

from src.model_trainer import get_model, train_model
from src.model_evaluator import evaluate_model
from src.utils_model import load_scaler, apply_scaler
from src.target_engineering import create_target

TRAIN_PATH = "data/splits/train.csv"
TEST_PATH = "data/splits/test.csv"


def run():
    """
    Execute the model training and selection pipeline.
    This function performs the following steps:
    - Loads configuration parameters
    - Reads training and testing datasets
    - Applies target engineering
    - Prepares feature matrices and target variables
    - Applies feature scaling using a pre-fitted scaler
    - Iterates through multiple models defined in the config
    - Trains and evaluates each model
    - Selects the best model based on F1 score
    - Saves the best model and experiment results
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
    best_score = 0
    best_model = None
    best_model_name = None
    results = {}
    for name, params in config["models"].items():
        print(f"\nTraining: {name}")
        model = get_model(name, params)
        model = train_model(model, X_train, y_train)
        metrics = evaluate_model(model, X_test, y_test)
        results[name] = metrics
        print(f"{name} Metrics:", metrics)
        if metrics["f1_score"] > best_score:
            best_score = metrics["f1_score"]
            best_model = model
            best_model_name = name
    with open(config["model_save_path"], "wb") as f:
        pickle.dump(best_model, f)
    results["best_model"] = best_model_name
    results["best_f1_score"] = best_score
    with open(config["experiment_results_path"], "w") as f:
        json.dump(results, f, indent=4)
    print("\nBest Model:", best_model_name)
    print("Best F1 Score:", best_score)
if __name__ == "__main__":
    run()