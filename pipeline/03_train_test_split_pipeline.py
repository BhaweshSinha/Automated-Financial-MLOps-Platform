"""
Train-Test Split Pipeline.
Loads processed data, splits it into training and testing sets,
and saves the resulting datasets for model development.
"""

from src.utils import load_data, save_data
from src.train_test_splitter import split_data
from src.config_loader import load_config


def run_split_pipeline():
    """
    Execute the train-test split pipeline.
    This function performs the following steps:
    - Loads configuration settings
    - Loads the processed dataset
    - Splits the data into training and testing sets
    - Saves the split datasets to specified paths
    Handles exceptions and reports pipeline execution status.
    Returns:
        None
    """
    try:
        print("Starting Train-Test Split Pipeline...\n")
        data_config = load_config("configs/data.yaml")
        df = load_data(data_config["processed_data_path"])
        print("Data loaded")
        print(f"Shape: {df.shape}\n")
        train_df, test_df = split_data(df)
        print("Data split completed")
        save_data(train_df, data_config["train_data_path"])
        save_data(test_df, data_config["test_data_path"])
        print("Train/Test saved")
        print("\n Pipeline Completed Successfully!")
    except Exception as e:
        print("Pipeline Failed!")
        print(e)
if __name__ == "__main__":
    run_split_pipeline()