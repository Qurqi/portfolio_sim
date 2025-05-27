import pandas as pd

def moving_average(prices: pd.Series, window: int = 20):
    return prices.rolling(window=window).mean()

def rsi(prices: pd.Series, window: int = 14):
    print("Calculating RSI (placeholder)")
    return pd.Series([50] * len(prices), index=prices.index)
