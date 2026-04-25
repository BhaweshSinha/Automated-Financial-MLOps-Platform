# Architecture Diagram

## High-Level Architecture

The system consists of the following major components:

1. Data Source
   - yFinance API

2. Data Ingestion Layer
   - Scheduled ingestion script / AWS Lambda

3. Data Storage
   - :contentReference[oaicite:5]{index=5} (raw and processed data)

4. Data Processing
   - Feature engineering and preprocessing on :contentReference[oaicite:6]{index=6}

5. Model Training
   - Training using :contentReference[oaicite:7]{index=7} or EC2

6. Experiment Tracking
   - :contentReference[oaicite:8]{index=8}

7. Model Deployment
   - FastAPI service hosted on EC2

8. Monitoring & Logging
   - :contentReference[oaicite:9]{index=9}

## Flow

yFinance → Ingestion → S3 → Processing → Training → MLflow → Deployment → Monitoring

## Note
A visual diagram (draw.io recommended) should be added here for better clarity.

## Architecture Explanation

This system is a batch-based MLOps pipeline for stock price movement prediction.

Data is ingested from the yFinance API using a scheduled ingestion mechanism and stored in Amazon S3 as raw data. The raw data is then processed on AWS EC2, where cleaning and feature engineering are performed. The processed data is stored back in S3.

Model training is performed using Gradient Boosting as the primary model and XGBoost as a secondary model. Experiment tracking and model versioning are handled using MLflow.

The trained model is stored in S3 and deployed using a FastAPI service hosted on EC2. Clients can send requests to the API to receive predictions on stock price movement (up/down).

Monitoring is implemented using Evidently AI for data drift and model performance tracking, and Amazon CloudWatch for logging, metrics, and system monitoring.
## Architecture Diagram

![Architecture Diagram](diagram_image.png)