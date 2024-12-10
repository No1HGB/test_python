import pandas as pd


def preprocessing_data(df: pd.DataFrame):
    df["SPS"] = df["Total Revenue"] / df["Number Of Shares"]
    df["Market Cap"] = df["Number Of Shares"] * df["close"]

    return df
