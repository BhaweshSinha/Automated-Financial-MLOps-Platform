# Problem Statement

Financial markets generate large volumes of time-series data that can be leveraged for predictive modeling. However, accurately forecasting exact stock prices is highly challenging due to market volatility and noise. A more robust and practical approach is to predict the direction of price movement (i.e., whether a stock will go up or down).

Building such a system requires more than just model development—it demands a scalable and reproducible pipeline for data ingestion, processing, training, deployment, and monitoring.

This project aims to design and implement an end-to-end MLOps platform for predicting stock price movement (binary classification) for selected Nifty-50 companies.

## Objectives
- Build a scalable pipeline for stock data ingestion using yFinance
- Perform data preprocessing and feature engineering on historical stock data
- Train machine learning models to predict stock price direction (up/down)
- Evaluate models using classification metrics such as Accuracy, Precision, Recall, F1-score, and ROC-AUC
- Deploy the trained model as a REST API for real-time inference
- Implement monitoring to track model performance and detect data drift over time

## System Type
- Batch-based machine learning system
- Supervised learning (binary classification)
- Cloud-native deployment using AWS

## Scope
- Historical data-based prediction (not high-frequency trading)
- Focus on directional prediction rather than exact price forecasting
- Emphasis on system design, reproducibility, and monitoring