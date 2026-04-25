"""
Final Model Training Module.
Builds a complete training pipeline including preprocessing and model,
trains it on the dataset, and saves the pipeline along with feature metadata.
"""
import pandas as pd
import joblib
import os
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import GradientBoostingClassifier
def create_target(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create binary classification target variable.
    Args:
        df (pd.DataFrame): Input dataset.
    Returns:
        pd.DataFrame: Dataset with target column.
    Create binary classification target:
    1 → Next return is positive
    0 → Next return is negative
    """
    df = df.copy()
    df["target"] = (df["Returns"].shift(-1) > 0).astype(int)
    df = df.dropna()

    return df

def preprocess_features(df: pd.DataFrame):
    """
    Prepare feature matrix and target variable.
    Removes non-numeric or irrelevant columns and separates
    features (X) and target (y).
    Args:
        df (pd.DataFrame): Input dataset.
    Returns:
        tuple: (X, y)
    Prepare feature matrix X and target y
    """
    drop_cols = ["Date", "Ticker"]  # non-numeric columns

    X = df.drop("target", axis=1)
    X = X.drop(columns=drop_cols, errors="ignore")
    y = df["target"]
    return X, y
def train_and_save(df: pd.DataFrame):
    """
    Train model pipeline and save artifacts.
    Performs the following steps:
    - Creates target variable
    - Prepares features and labels
    - Trains a pipeline (scaler + model)
    - Saves trained pipeline and feature list
    Args:
        df (pd.DataFrame): Training dataset.
    Returns:
        None
    """
    print("Training started...")
    df = create_target(df)
    X, y = preprocess_features(df)
    print("Data Shape:", X.shape)
    print("Features Used:", list(X.columns))
    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("model", GradientBoostingClassifier())
    ])
    pipeline.fit(X, y)
    os.makedirs("models", exist_ok=True)
    model_path = os.path.join("models", "final_pipeline.pkl")
    joblib.dump(pipeline, model_path)

    print(f"Model saved at: {model_path}")
    feature_path = os.path.join("models", "features.json")
    import json
    with open(feature_path, "w") as f:
        json.dump(list(X.columns), f)

    print(f"Features saved at: {feature_path}")


if __name__ == "__main__":
    print("Loading data...")
    data_path = "data/splits/train.csv"
    if not os.path.exists(data_path):
        raise FileNotFoundError(f"File not found: {data_path}")
    df = pd.read_csv(data_path)
    train_and_save(df)