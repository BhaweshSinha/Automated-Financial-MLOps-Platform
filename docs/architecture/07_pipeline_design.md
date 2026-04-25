# Pipeline Design

The system follows a modular pipeline:

## Stage 1: Data Ingestion
- Fetch data using yFinance

## Stage 2: Data Validation
- Check schema, missing values

## Stage 3: Data Processing
- Feature engineering and cleaning

## Stage 4: Model Training
- Train models on processed data

## Stage 5: Model Evaluation
- Evaluate using RMSE, MAE
Evaluate using:
- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC

## Stage 6: Model Deployment
- Deploy best model as API

## Stage 7: Monitoring
- Track performance and drift

## Orchestration
- Pipeline can be automated using :contentReference[oaicite:21]{index=21}