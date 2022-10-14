"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.3
"""

import pandas as pd
import logging
def limit_data_size(data : pd.DataFrame, limit_size : int) -> pd.DataFrame:
    """
    Limit the size of the data to the limit_size
    args :
        data : pd.DataFrame
        limit_size : int
    returns :
        pd.DataFrame
    """
    if limit_size is None:
        logging.warning("No limit size")
        return data
    return data.head(limit_size)

def rename_columns(data : pd.DataFrame ) -> pd.DataFrame:
    """
    rename the original columns into camelcase
    Args:
        data (pd.DataFrame): the original inconsistent col name dataset
    Returns:
        pd.DataFrame: camelCase col name dataset
        """
    data.columns = [col.lower().replace(" ", "_") for col in data.columns]
    return data

#a function that explores the data , gives a description and a statistics,and cleans the data
def explore_data(data : pd.DataFrame):
    #explore the data
    print(data.head())
    #describe the data
    print(data.describe())
    #get the statistics of the data
    print(data.info())
    #clean the data
    data.dropna(inplace=True)
    return data

import pandas as pd
import numpy as np
import logging

logger = logging.getLogger(__name__)


def compute_trip_duration(data: pd.DataFrame) -> pd.DataFrame:
    data["trip_duration"] = (pd.to_datetime(data["tpep_dropoff_datetime"]) - pd.to_datetime(data["tpep_pickup_datetime"])) / pd.Timedelta(
        minutes=60)
    return data


def compute_tip_ratio(data: pd.DataFrame) -> pd.DataFrame:
    """
    Add feature compute tip ratio
    :param data: pd.DataFrame: the original inconsistent col name dataset
    :return: dataframe
    """
    data["tip_ratio"] = 100 * data["tip_amount"] / (data["total_amount"] - data["tip_amount"])
    return data


def bucketize_tip_ratio(data: pd.DataFrame) -> pd.DataFrame:
    bins = np.array([-0.001, 15.0, 20.0, 25.0, np.Inf])
    data["tip_ratio_level"] = pd.cut(data["tip_ratio"], bins=bins, labels=["low", "medium", "high", "very_high"])
    return data

def add_trip_ratio_level(data: pd.DataFrame) -> pd.DataFrame:
    data = compute_tip_ratio(data)
    return bucketize_tip_ratio(data)


