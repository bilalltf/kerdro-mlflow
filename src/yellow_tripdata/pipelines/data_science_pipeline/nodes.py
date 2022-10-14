"""
This is a boilerplate pipeline 'data_science_pipeline'
generated using Kedro 0.18.3
"""

from re import A
import pandas as pd
from sklearn import metrics
from sklearn.linear_model import ElasticNet
from typing import Dict, List
import mlflow
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier
# create a function that encodes the categorical data tip_ratio_level


def encode_categorical_data(data : pd.DataFrame) -> pd.DataFrame:
    scale_mapper = {"low":1, "medium":2, "high":3, "very_high":4}
    data["tip_ratio_level"] = data["tip_ratio_level"].replace(scale_mapper)
    # data = pd.get_dummies(data, columns=["tip_ratio_level"])
    return data


# create a function that applies the PCA 
def apply_pca(X_train : pd.DataFrame, X_test : pd.DataFrame) -> pd.DataFrame:
    #apply the PCA
    from sklearn.decomposition import PCA
    pca = PCA(n_components=2)
    X_train = pca.fit_transform(X_train)
    X_test = pca.transform(X_test)
    return X_train, X_test

# select the features to train the model



def select_features(data : pd.DataFrame) -> pd.DataFrame:
    #select the features
    features = ["passenger_count", "fare_amount", "trip_duration", "extra",	"mta_tax", "tip_amount","tolls_amount", "trip_distance", "tip_ratio_level", "total_amount"]
    return data[features]

# split train and test data
def split_train_test_data(data : pd.DataFrame) -> pd.DataFrame:
    from sklearn.model_selection import train_test_split
    train_data, test_data = train_test_split(data, test_size=0.2)
    return train_data, test_data
    

def elasticnet_regresion(train_df: pd.DataFrame, test_df: pd.DataFrame, params: Dict[str, float]):
    """
    Fit and test a Regression model using ElasticNet, compute and display the Mean Absolute Error metric of this model.

    Args:
        train_df: the split dataset use to train the model
        test_df: the split dataset use to test the model
        params: dictionary containing the alpha and l1_ratio parameters (ex : {'alpha': 0.8, 'l1_ratio': 0.2})

    Returns: scikit-learn ElasticNet linear model
    target = "FareAmount"
    """
    # Write your code
    target = "fare_amount"
    X_train = train_df.drop(target, axis=1)
    y_train = train_df[target]
    X_test = test_df.drop(target, axis=1)
    y_test = test_df[target]

    model = ElasticNet(**params)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mae = metrics.mean_absolute_error(y_test, y_pred)
    # log the mae in mlflow
    mlflow.log_metric("mae", mae)
    print("Mean Absolute Error: {}".format(mae))
    return model


def decision_tree_classification(train_data: pd.DataFrame, test_data: pd.DataFrame):
    """
    Fit and return a decision tree. Compute and display model accuracy.
    """
    target = "tip_ratio_level"
    # Write your code
    X_train = train_data.drop(target, axis=1)
    y_train = train_data[target]
    X_test = test_data.drop(target, axis=1)
    y_test = test_data[target]
    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    accuracy = metrics.accuracy_score(y_test, y_pred)
    # log the accuracy in mlflow
    mlflow.log_metric("accuracy", accuracy)
    print("Accuracy: {}".format(accuracy))
    return model

def regression_cv(train_df: pd.DataFrame, cv_params: Dict[str, List[float]]):
    """
    Compute a Cross Validation of ElasticNet regression.

    Args:
        train_df: (pandas.DataFrame) Training data to use to fit the model.
        cv_params: Dictionary with list of values for each model parameters.
        

    Returns:
        Best model obtained by the cross validation.
    """
    target = "fare_amount"
    scores = ["neg_mean_squared_error", 'neg_root_mean_squared_error', 'neg_mean_absolute_error']

    # Write your code
    X_train = train_df.drop(target, axis=1)
    y_train = train_df[target]
    model = ElasticNet()
    grid = GridSearchCV(model, cv_params, cv=5, scoring=scores, refit='neg_mean_squared_error')
    grid.fit(X_train, y_train)
    print(grid.best_params_)
    print(grid.best_score_)
    # log the best parameters and the best score in mlflow
    mlflow.log_metric("best_param alpha", grid.best_params_['alpha'])
    mlflow.log_metric("best_param l1_ratio", grid.best_params_['l1_ratio'])
    mlflow.log_metric("best_score_", str(grid.best_score_))
    return grid.best_estimator_