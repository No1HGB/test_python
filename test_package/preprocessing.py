import numpy as np
import pandas as pd


def preprocessing_data(df: pd.DataFrame):
    def calculate_average_price(row):
        return (row["close"] + row["open"]) / 2

    df["SPS"] = df["Total Revenue"] / df["Number Of Shares"]
    df["avg_price"] = df.apply(calculate_average_price, axis=1)
    df["Market Cap"] = df["Number Of Shares"] * df["close"]

    # ATR(Average True Range)
    df["previous_close"] = df["close"].shift(1)
    df["high_low"] = df["high"] - df["low"]
    df["high_pc"] = np.abs(df["high"] - df["previous_close"])
    df["low_pc"] = np.abs(df["low"] - df["previous_close"])
    df["TR"] = df[["high_low", "high_pc", "low_pc"]].max(axis=1)
    df["ATR"] = df["TR"].rolling(window=10).mean()

    df.dropna(axis=0, inplace=True, how="any")
    df.reset_index(drop=True, inplace=True)

    return df
