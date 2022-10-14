"""
This is a boilerplate pipeline 'data_science_pipeline'
generated using Kedro 0.18.3
"""

from kedro.pipeline import Pipeline, node, pipeline
from .nodes import encode_categorical_data, select_features, split_train_test_data, elasticnet_regresion, decision_tree_classification, regression_cv

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            func=encode_categorical_data,
            inputs="explored_data",
            outputs="encoded_data",
            name="encode_categorical_data"
        ),
        node(
            func=select_features,
            inputs="encoded_data",
            outputs="selected_features",
            name="select_features"
        ),
        node(
            func=split_train_test_data,
            inputs="selected_features",
            outputs=["train_data", "test_data"],
            name="split_train_test_data"
        ),
        node(
            func=elasticnet_regresion,
            inputs=["train_data", "test_data", "params:elas_reg_params"],
            outputs="elasticnet_regresion_model",
            name="elasticnet_regresion"
        ),
        node(
            func=decision_tree_classification,
            inputs=["train_data", "test_data"],
            outputs="decision_tree_classification_model",
            name="decision_tree_classification"
        
        ),
        node(
            func=regression_cv,
            inputs=["train_data", "params:regression_cv_params"],
            outputs="None",
            name="regression_cv_model"
        )

        ])