"""
Baseline Model Utilities.
Provides functions to train a simple baseline model and save it
for benchmarking and comparison purposes.
"""
import pickle
from sklearn.linear_model import LogisticRegression

def train_baseline(X_train, y_train):
    """
    Train a baseline Logistic Regression model.
    Args:
        X_train (array-like or pd.DataFrame): Training feature matrix.
        y_train (array-like or pd.Series): Training target values.
    Returns:
        LogisticRegression: Trained baseline model.
    """
    model = LogisticRegression(max_iter=200)
    model.fit(X_train, y_train)
    return model

def save_model(model, path):
    """
    Save a trained model to directory.
    Args:
        model: Trained machine learning model.
        path (str): File path to save the model.
    Returns:
        None
    """
    with open(path, "wb") as f:
        pickle.dump(model, f)