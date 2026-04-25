# 📘 Financial MLOps Case Study  
## Automated Multi-Asset Stock Direction Prediction System

---

## 1. Problem Statement

Financial markets are highly dynamic and influenced by multiple factors, making accurate prediction of price movements a complex task. 

This project focuses on predicting the **next-day direction of stock prices (up/down)** for a portfolio of large-cap stocks. The goal is to:

- Predict whether the stock price will increase or decrease the next trading day  
- Transform raw market data into actionable trading signals  
- Build a scalable and automated pipeline for continuous prediction  

This is formulated as a **binary classification problem**, where:

- `1` → Price expected to increase  
- `0` → Price expected to decrease  

---

## 2. Business Context

Predicting short-term price movement is critical for:

- Algorithmic trading systems  
- Quantitative investment strategies  
- Risk-aware portfolio adjustments  

This system can be used by:

- Retail traders for decision support  
- Quantitative analysts for strategy development  
- FinTech platforms for automated trading insights  

By automating this process through an MLOps pipeline, the system ensures:

- Continuous data updates  
- Consistent model retraining  
- Scalable deployment for real-world usage  

---

## 3. Approach

### Data Collection & Ingestion

- Selected a **tradable universe of 30 Nifty-50 stocks**  
- Collected **10 years of daily OHLCV data** using `yfinance`  
- Built a data ingestion pipeline to:
  - Download data per ticker  
  - Store structured CSV files  
  - Maintain a clean data directory  

Final combined dataset:

- **Rows**: ~74,100  
- **Features**: 7 (base + engineered)

---

### Feature Engineering

To capture temporal and statistical patterns, the following features were engineered:

- **Returns** → Percentage price change  
- **Moving Averages**:
  - `Ma_7` (short-term trend)  
  - `Ma_30` (long-term trend)  
- **Volatility** → Rolling standard deviation of returns  
- **Lag Feature (`Lag_1`)** → Previous day price dependency  

These features help the model capture:

- Trend behavior  
- Momentum signals  
- Market volatility  

---

### Target Engineering

The target variable is defined as:

- `target = 1` → Next day return > 0  
- `target = 0` → Next day return ≤ 0  

This converts the problem into a **binary classification task** for predicting market direction.

---

### Modeling

A machine learning classification pipeline was implemented to:

- Train models on engineered features  
- Predict next-day direction  
- Output both:
  - Class prediction  
  - Probability scores  

Evaluation metrics used:

- Accuracy  
- Precision  
- Recall  
- F1-score  
- ROC-AUC  

---

### Prediction Pipeline

A modular prediction pipeline was developed to:

- Accept structured input data  
- Apply preprocessing and feature alignment  
- Generate predictions and probabilities  

Example usage:

```python
preds, probs = pipeline.predict(df)