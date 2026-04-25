"""
Preprocessing Module.
Applies feature scaling to selected numerical features and
saves the fitted scaler for reuse in inference.
"""
import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib
import os

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Preprocess the dataset by scaling numerical features.
    Fits a StandardScaler on selected features, transforms them,
    and saves the scaler for later use.
    Args:
        df (pd.DataFrame): Input dataset.
    Returns:
        pd.DataFrame: Preprocessed dataset with scaled features.
    """
    features = ['Close', 'Ma_7', 'Ma_30', 'Volatility']
    scaler = StandardScaler()
    df[features] = scaler.fit_transform(df[features])
    os.makedirs("models", exist_ok=True)
    joblib.dump(scaler, "models/scaler.pkl")

    return df