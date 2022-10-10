"""
This is a boilerplate pipeline 'data_science_pipeline'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import rename_column

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=rename_column,
            inputs=["limit_taxi_data"],
            outputs="renamed_taxi_data",
            name="rename_column"
        ),
    ])
