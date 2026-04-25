"""
Model Evaluation Module.
Handles model prediction and delegates metric computation
for classification tasks.
"""
from src.metrics import evaluate_classification


def evaluate_model(model, X_test, y_test):
    """
    Evaluate a trained model on test data.
    Generates predictions and computes evaluation metrics.
    Supports probability-based evaluation if the model provides it.
    Args:
        model: Trained machine learning model.
        X_test (array-like or pd.DataFrame): Test feature matrix.
        y_test (array-like or pd.Series): True labels.
    Returns:
        dict: Evaluation metrics.
    """
    y_pred = model.predict(X_test)

    if hasattr(model, "predict_proba"):
        y_prob = model.predict_proba(X_test)[:, 1]
    else:
        y_prob = None

    return evaluate_classification(y_test, y_pred, y_prob)