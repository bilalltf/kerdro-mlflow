"""
This is a boilerplate pipeline 'data_engineering_pipeline'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import limit_data_size

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=limit_data_size,
            inputs=["Trajectories","params:limit_size"],
            outputs="limit_taxi_data",
            name="limit_data_size"
        ),
    ])
