# ⚙️ Usage Guide  
## Automated Financial MLOps Platform – Multi-Asset Stock Direction Prediction

---

## 1. 📦 Overview

This guide explains how to use the system after completing setup.

The platform enables:

- Prediction of next-day stock price direction (up/down)  
- Use of engineered financial features  
- Integration with a modular prediction pipeline  

---

## 2. 🔮 Running Predictions

The system uses a `PredictionPipeline` to generate predictions.

### Example Usage:

```python
from pipeline.prediction_pipeline import PredictionPipeline
import pandas as pd

pipeline = PredictionPipeline()

sample = {
    "Close": 150.0,
    "High": 152.0,
    "Low": 148.0,
    "Open": 149.5,
    "Volume": 1000000,
    "Returns": 0.01,
    "Ma_7": 148.5,
    "Ma_30": 145.0,
    "Volatility": 0.02,
    "Lag_1": 0.005
}

df = pd.DataFrame([sample])

preds, probs = pipeline.predict(df)

print("Prediction:", preds)
print("Probability:", probs)