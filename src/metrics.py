"""
Evaluation Metrics Module.
Provides utility functions to compute classification performance
metrics for model evaluation.
"""
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

def evaluate_classification(y_true, y_pred, y_prob=None):
    """
    Compute classification evaluation metrics.

    Calculates accuracy, precision, recall, and F1 score.
    Optionally computes ROC-AUC if probability scores are provided.

    Args:
        y_true (array-like): Ground truth labels.
        y_pred (array-like): Predicted labels.
        y_prob (array-like, optional): Predicted probabilities for the positive class.

    Returns:
        dict: Dictionary containing evaluation metrics.
    """
    metrics = {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred),
        "recall": recall_score(y_true, y_pred),
        "f1_score": f1_score(y_true, y_pred),
    }

    if y_prob is not None:
        metrics["roc_auc"] = roc_auc_score(y_true, y_prob)

    return metrics