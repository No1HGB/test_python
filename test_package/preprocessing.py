import pandas as pd


def preprocessing_data(df: pd.DataFrame) -> pd.DataFrame:
    df["SPS"] = df["Total Revenue"] / df["Number Of Shares"]
    df["Market Cap"] = df["Number Of Shares"] * df["close"]
    df["ROIC"] = df["Net Operating Profit After Tax"] / df["Invested Capital"]

    return df


def rank_data(df: pd.DataFrame) -> pd.DataFrame:
    df["PSR_rank"] = df.groupby(by="date")["PSR"].rank(ascending=True, method="first")
    df["ROIC_rank"] = df.groupby(by="date")["ROIC"].rank(
        ascending=False, method="first"
    )

    df["total_rankvalue"] = df["PSR_rank"] + df["ROIC_rank"]
    df["total_rank"] = df.groupby(by="date")["total_rankvalue"].rank(
        ascending=True, method="first"
    )

    return df
