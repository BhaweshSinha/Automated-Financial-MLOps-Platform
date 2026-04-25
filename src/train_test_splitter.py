"""
Train-Test Split Module.
Splits dataset into training and testing sets based on
a configurable ratio while preserving temporal order.
"""
import pandas as pd
from src.config_loader import load_config
def split_data(df: pd.DataFrame, config_path: str = "configs/split.yaml"):
    """
    Split dataset into training and testing sets.
    Uses a split ratio from configuration and ensures time-based
    ordering if a date column is present.
    Args:
        df (pd.DataFrame): Input dataset.
        config_path (str): Path to split configuration file.
    Returns:
        tuple: (train_df, test_df)
    """
    config = load_config(config_path)
    split_ratio = config["split_ratio"]
    if "Date" in df.columns:
        df = df.sort_values("Date")
    split_index = int(len(df) * split_ratio)
    train_df = df.iloc[:split_index]
    test_df = df.iloc[split_index:]
    return train_df, test_df