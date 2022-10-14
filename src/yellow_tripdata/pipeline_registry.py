"""Project pipelines."""
from typing import Dict
from kedro.pipeline import Pipeline
from .pipelines import data_engineering_pipeline as de, data_science_pipeline as ds


def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.
    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    data_engineering = de.create_pipeline()
    data_science = ds.create_pipeline()
    
    return {"de":data_engineering, "ds": data_science, "__default__":data_engineering}
