# Design Decisions

## Why Batch Pipeline?
Stock data is historical and does not require real-time streaming, making batch processing efficient and simpler.

## Why Classification Instead of Regression?
Predicting exact stock prices is noisy and unstable. Predicting direction (up/down) provides more robust and actionable insights.

## Why Gradient Boosting?
It provided the best balance of performance across evaluation metrics such as F1-score and ROC-AUC.

## Why AWS S3?
Provides scalable and cost-effective storage for raw, processed, and model data.

## Why FastAPI?
Lightweight and efficient for serving ML models as REST APIs.

## Why MLflow?
Enables experiment tracking, reproducibility, and model versioning.