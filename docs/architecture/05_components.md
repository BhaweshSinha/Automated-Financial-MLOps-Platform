# System Components

## 1. Data Ingestion
- Fetches stock data from yFinance
- Output: Raw CSV files

## 2. Data Storage
- Stores raw and processed data in :contentReference[oaicite:11]{index=11}

## 3. Data Processing
- Cleans and transforms data
- Generates features for modeling

## 4. Model Training
- Trains classification models to predict stock movement direction
- Primary model: Gradient Boosting
- Secondary model: XGBoost

## 5. Model Registry
- Tracks experiments and model versions using :contentReference[oaicite:12]{index=12}

## 6. Model Serving
- Exposes prediction API using FastAPI

## 7. Monitoring
- Tracks performance metrics
- Logs system behavior
- Uses :contentReference[oaicite:13]{index=13}