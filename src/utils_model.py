"""
Model Utilities Module.
Provides helper functions for loading and applying preprocessing
artifacts such as scalers during training and inference.
"""
import joblib

def load_scaler(path):
    """
    Load a saved scaler from disk.
    Args:
        path (str): Path to the saved scaler file.
    Returns:
        object: Loaded scaler instance.
    """
    return joblib.load(path)

def apply_scaler(scaler, X):
    """
    Apply a fitted scaler to feature data.
    Args:
        scaler: Fitted scaler object.
        X (array-like or pd.DataFrame): Feature data to transform.
    Returns:
        array-like: Scaled feature data.
    """
    return scaler.transform(X)