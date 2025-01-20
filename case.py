import pandas as pd


def UPPER_CASE(df: pd.DataFrame):
    ALPHA = "a"
    BETA = "b"
    column = ALPHA + BETA

    return df[column]


def lower_case(df: pd.DataFrame):
    alpha = "a"
    beta = "b"
    column = alpha + beta

    return df[column]
