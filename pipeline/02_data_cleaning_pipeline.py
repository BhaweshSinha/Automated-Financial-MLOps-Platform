"""
Data Cleaning and Preprocessing Pipeline.
Loads raw data, performs cleaning, feature engineering, preprocessing,
and validation, then saves the final processed dataset for downstream use.
"""
import warnings
warnings.filterwarnings('ignore')
from src.utils import load_data, save_data
from src.data_cleaning import clean_data
from src.feature_engineering import engineer_features
from src.preprocessing import preprocess_data
from src.validation import validate_data
def run_data_cleaning_pipeline():
    """
    Execute the data cleaning and preprocessing pipeline.
    This function performs the following steps:
    - Loads raw dataset
    - Cleans and handles missing/inconsistent data
    - Engineers features
    - Applies preprocessing transformations
    - Validates the processed data
    - Saves the final dataset
    Returns:
        None
    """
    print("Starting Data Cleaning & Preprocessing Pipeline...")
    df = load_data("data/combined_dataset/combined_data.csv")
    df = clean_data(df)
    df = engineer_features(df)
    df = preprocess_data(df)
    validate_data(df)
    save_data(df, "data/processed/final_data.csv")
if __name__ == "__main__":
    run_data_cleaning_pipeline()