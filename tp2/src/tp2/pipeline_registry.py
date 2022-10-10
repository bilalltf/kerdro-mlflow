"""Project pipelines."""
from typing import Dict

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from .pipelines import data_engineering_pipeline as de, data_science_pipeline as ds, duration, trip_ratio




def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    data_engineering = de.create_pipeline()
    data_science = ds.create_pipeline()
    dur = duration.create_pipeline()
    ratios = trip_ratio.create_pipeline()
    return {"de":data_engineering, "ds":data_science, "duration":dur,"ratio_level":ratios, "__default__":data_engineering+data_science+dur+ratios}
