"""
Data Cleaning Module.
Provides functionality to clean raw data by removing duplicates,
handling missing values, and ensuring proper date formatting.
"""
import pandas as pd
def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the input dataset.
    Performs the following operations:
    - Removes duplicate rows
    - Fills missing values using forward fill
    - Converts and sorts by date if present
    Args:
        df (pd.DataFrame): Raw input data.
    Returns:
        pd.DataFrame: Cleaned dataset.
    """
    df = df.drop_duplicates()
    df = df.fillna(method="ffill")
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
        df = df.sort_values('Date')
    return df