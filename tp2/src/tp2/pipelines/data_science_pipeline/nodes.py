"""
This is a boilerplate pipeline 'data_science_pipeline'
generated using Kedro 0.18.3
"""
import pandas as pd

def to_camel_case(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

def rename_column(data:pd.DataFrame):
    data.columns = [to_camel_case(x) for x in data.columns]
    return data