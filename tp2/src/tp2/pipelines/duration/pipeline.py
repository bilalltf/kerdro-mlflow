"""
This is a boilerplate pipeline 'duration'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import duration

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=duration,
            inputs=["renamed_taxi_data"],
            outputs="duration_data",
            name="duration"
        ),
    ])
