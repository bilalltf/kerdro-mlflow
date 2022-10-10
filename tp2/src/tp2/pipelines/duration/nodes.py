"""
This is a boilerplate pipeline 'duration'
generated using Kedro 0.18.3
"""
import pandas as pd


def duration(data: pd.DataFrame):
    data["duration"] = pd.DatetimeIndex(data["tpepDropoffDatetime"]) - pd.DatetimeIndex(data["tpepPickupDatetime"])
    return data