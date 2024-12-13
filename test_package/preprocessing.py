import numpy as np
import pandas as pd


def preprocessing_data(df: pd.DataFrame):
    df["SPS"] = df["Total Revenue"] / df["Number Of Shares"]
    df["Market Cap"] = df["Number Of Shares"] * df["close"]
    df["시가총액"] = pd.to_numeric(df["상장주식수"] * df["종가"])  # 2022-11-24 수정
    df["fcf_rank"] = df["재무항목0"] / df["시가총액"]
    # FCF(QSUM) 이 0보다 큰 회사만 남은 상태에서 시가총액이 큰 회사를 고름
    df["rank1"] = df.groupby(by="date")["fcf_rank"].rank(ascending=True, method="first")

    # 최종적으로 회사의 시총이 크면서 FCF(QSUM) 도 큰 회사를 뽑음
    df["total_rankvalue"] = df["rank1"]
    df["total_rank"] = df.groupby(by="date")["total_rankvalue"].rank(
        ascending=True, method="first"
    )

    # Wrong ATR(Average True Range) Example
    df["previous_close"] = df["close"].shift(1)
    df["high_low"] = df["high"] - df["low"]
    df["high_pc"] = np.abs(df["high"] - df["previous_close"])
    df["low_pc"] = np.abs(df["low"] - df["previous_close"])
    df["TR"] = df[["high_low", "high_pc", "low_pc"]].max(axis=1)
    df["ATR"] = df["TR"].rolling(window=10).mean()
    return df
