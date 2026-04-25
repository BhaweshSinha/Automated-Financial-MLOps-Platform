# Data Flow

The system follows a structured data pipeline:

1. Data Ingestion
   - Historical stock data is fetched using the yFinance API

2. Raw Data Storage
   - Data is stored in :contentReference[oaicite:10]{index=10} under the "raw" layer

3. Data Preprocessing
   - Missing values handled
   - Feature engineering (returns, moving averages, etc.)

4. Processed Data Storage
   - Cleaned data stored in S3 under "processed" layer

5. Model Training
   - Processed data used to train ML models

6. Model Storage
   - Trained models saved and versioned

7. Prediction
   - API receives input → model returns prediction

8. Logging & Monitoring
   - Predictions and metrics logged for analysis