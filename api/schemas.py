"""
Data schemas for request validation.
Defines the structure of input data required for the prediction
pipeline using Pydantic models.
"""
from pydantic import BaseModel
class InputData(BaseModel):
    Close: float
    High: float
    Low: float
    Open: float
    Volume: float
    Returns: float
    Ma_7: float
    Ma_30: float
    Volatility: float
    Lag_1: float