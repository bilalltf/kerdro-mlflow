"""
This is a boilerplate pipeline 'data_engineering_pipeline'
generated using Kedro 0.18.3
"""
import pandas as pd
import logging

def limit_data_size(data:pd.DataFrame, limit_size: int)-> pd.DataFrame:
    if limit_size is None:
        logging.warning("No limit size was provided, full data will be used")
        return data
    return data.head(limit_size)