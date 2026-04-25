"""
Feature Engineering Module.
Generates additional features from raw stock data to enhance
model performance.
"""
import pandas as pd
def engineer_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Generate derived features for modeling.
    Creates the following features:
    - Returns (percentage change in closing price)
    - Moving averages (7-day and 30-day)
    - Volatility (rolling standard deviation of returns)
    - Lag feature (previous closing price)
    Args:
        df (pd.DataFrame): Cleaned input data.
    Returns:
        pd.DataFrame: Dataset with engineered features.
    """
    df['Returns'] = df['Close'].pct_change()
    df['Ma_7'] = df['Close'].rolling(7).mean()
    df['Ma_30'] = df['Close'].rolling(30).mean()
    df['Volatility'] = df['Returns'].rolling(7).std()
    df['Lag_1'] = df['Close'].shift(1)
    df = df.dropna()
    return df