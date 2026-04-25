"""
Model Trainer Module.
Provides utilities to initialize and train machine learning models
based on configuration settings.
"""
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from xgboost import XGBClassifier

def get_model(name, params):
    """
    Initialize a machine learning model based on its name.
    Supports multiple model types with configurable parameters.
    Args:
        name (str): Name of the model.
        params (dict): Hyperparameters for the model.
    Returns:
        object: Initialized model instance.
    Raises:
        ValueError: If the model name is not recognized.
    """
    if name == "logistic_regression":
        return LogisticRegression(**params)

    elif name == "random_forest":
        return RandomForestClassifier(**params)

    elif name == "gradient_boosting":
        return GradientBoostingClassifier(**params)

    elif name == "xgboost":
        return XGBClassifier(**params)

    else:
        raise ValueError(f"Unknown model: {name}")

def train_model(model, X_train, y_train):
    """
    Train a machine learning model.
    Fits the model on the provided training data.
    Args:
        model: Machine learning model instance.
        X_train (array-like or pd.DataFrame): Training features.
        y_train (array-like or pd.Series): Training labels.
    Returns:
        object: Trained model.
    """
    model.fit(X_train, y_train)
    return model