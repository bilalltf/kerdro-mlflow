"""
This is a boilerplate pipeline 'trip_ratio'
generated using Kedro 0.18.3
"""
import pandas as pd
import numpy as np

def add_tip_ratio_level(data: pd.DataFrame) -> pd.DataFrame:
    data["tipRatio"] = 100 * data["tipAmount"] / (data["totalAmount"] - data["tipAmount"])
    data['bins'] = pd.cut(x=data['tipRatio'], bins=np.array([-0.001, 15.0, 20.0, 25.0, np.Inf]))
    data.head()
    return data
