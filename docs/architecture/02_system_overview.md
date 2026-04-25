# System Overview

The system is an end-to-end MLOps pipeline designed to automate the lifecycle of a stock price prediction model.

The pipeline begins with data ingestion from the yFinance API, followed by data storage in :contentReference[oaicite:0]{index=0}. The raw data is then processed and transformed into features suitable for model training.

Model training is performed using scalable compute resources such as :contentReference[oaicite:1]{index=1} or :contentReference[oaicite:2]{index=2}. Experiment tracking and model versioning are handled using :contentReference[oaicite:3]{index=3}.

The trained model is deployed as a REST API using FastAPI, enabling real-time predictions. Monitoring mechanisms are integrated using :contentReference[oaicite:4]{index=4} to track performance, logs, and system health.

The entire pipeline is designed to be automated and reproducible, ensuring scalability and maintainability.