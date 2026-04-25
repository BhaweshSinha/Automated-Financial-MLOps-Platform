"""
Data Ingestion Module.
Downloads historical stock market data for a predefined set of tickers
and saves them as CSV files for further processing.
"""
import yfinance as yf
import pandas as pd
from pathlib import Path


TICKERS = [
    "RELIANCE.NS","TCS.NS","INFY.NS","HDFCBANK.NS","ICICIBANK.NS",
    "SBIN.NS","LT.NS","HINDUNILVR.NS","ITC.NS","KOTAKBANK.NS",
    "AXISBANK.NS","BAJFINANCE.NS","ASIANPAINT.NS","MARUTI.NS",
    "SUNPHARMA.NS","TITAN.NS","ULTRACEMCO.NS","WIPRO.NS",
    "NESTLEIND.NS","POWERGRID.NS","NTPC.NS","ONGC.NS",
    "BHARTIARTL.NS","HCLTECH.NS","TECHM.NS","ADANIENT.NS",
    "ADANIPORTS.NS","BAJAJFINSV.NS","DRREDDY.NS","EICHERMOT.NS"
]

def download_data(tickers=TICKERS, period="10y"):
    """
    Download historical stock data for given tickers.
    Fetches data using yfinance and stores each ticker's data
    as a CSV file in the raw data directory.
    Args:
        tickers (list): List of stock ticker symbols.
        period (str): Time period for historical data (e.g., '1y', '5y', '10y').
    Returns:
        None
    """
    raw_data_dir = Path("data") / "raw_data"
    raw_data_dir.mkdir(parents=True, exist_ok=True)
    for ticker in tickers:
        df = yf.download(ticker, period=period)
        df.reset_index(inplace=True)
        filename = ticker.replace(".", "_") + ".csv"
        df.to_csv(raw_data_dir / filename, index=False)
if __name__ == "__main__":
    download_data()