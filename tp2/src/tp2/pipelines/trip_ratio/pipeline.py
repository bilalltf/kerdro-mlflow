"""
This is a boilerplate pipeline 'trip_ratio'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import add_tip_ratio_level


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=add_tip_ratio_level,
            inputs=["duration_data"],
            outputs="ratio_level_data",
            name="ratio_level"
        ),
    ])
