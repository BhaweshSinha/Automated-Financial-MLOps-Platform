"""
General Utilities Module.
Provides helper functions for loading and saving datasets.
"""
import pandas as pd
import os
def load_data(path: str) -> pd.DataFrame:
    """
    Load dataset from a CSV file.
    Args:
        path (str): Path to the CSV file.
    Returns:
        pd.DataFrame: Loaded dataset.
    Raises:
        FileNotFoundError: If the file does not exist.
    """
    if not os.path.exists(path):
        raise FileNotFoundError(f"{path} not found!")
    return pd.read_csv(path)
def save_data(df: pd.DataFrame, path: str):
    """
    Save dataset to a CSV file.
    Creates directories if they do not exist.
    Args:
        df (pd.DataFrame): Dataset to save.
        path (str): Destination file path.
    Returns:
        None
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    df.to_csv(path, index=False)