"""
This is a boilerplate pipeline 'data_engineering'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import add_trip_ratio_level, limit_data_size, rename_columns, explore_data, compute_trip_duration

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=limit_data_size,
            inputs=["Trajectories", "params:limit_size"],
            outputs="limit_taxi_data",
            name="limit_data_size"
        ),
        node(
            func=rename_columns,
            inputs="limit_taxi_data",
            outputs="rename_taxi_data",
            name="rename_columns"
        ),
        node(
            func=compute_trip_duration,
            inputs="rename_taxi_data",
            outputs="trip_duration_taxi_data",
            name="compute_trip_duration"
        ),
        node(
            func=add_trip_ratio_level,
            inputs="trip_duration_taxi_data",
            outputs="Trajectories_output",
            name="add_tip_ratio_level"
        ),
        node(
            func=explore_data,
            inputs="Trajectories_output",
            outputs='explored_data',
            name="explore_data"
        )
        ])