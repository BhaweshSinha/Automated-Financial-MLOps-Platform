"""
Target Engineering Module.
Creates target variables required for supervised learning tasks.
"""
import pandas as pd
def create_target(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create binary classification target variable.
    Target is defined as:
    - 1 if next period return is positive
    - 0 otherwise
    Args:
        df (pd.DataFrame): Input dataset with 'Returns' column.
    Returns:
        pd.DataFrame: Dataset with target column added.
    """
    df = df.copy()
    df["target"] = (df["Returns"].shift(-1) > 0).astype(int)
    df = df.dropna()
    return df