"""
Data Validation Module.
Performs basic validation checks on datasets to ensure data
quality and consistency before further processing.
"""
import pandas as pd
def validate_data(df: pd.DataFrame):
    """
    Validate dataset integrity.
    Checks for:
    - Missing values
    - Required columns
    - Invalid data ranges
    Args:
        df (pd.DataFrame): Dataset to validate.
    Returns:
        None
    Raises:
        ValueError: If validation checks fail.
    """
    if df.isnull().sum().sum() != 0:
        raise ValueError("Missing values found in dataset")
    if 'Close' not in df.columns:
        raise ValueError("'Close' column missing")
    
    if df['Close'].min() < -10:
        raise ValueError("Invalid price detected")
