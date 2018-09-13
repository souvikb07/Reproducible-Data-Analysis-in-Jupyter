# Import the data download library
from jupyterworkflow.data import get_fremont_data
import pandas as pd

# create a function to do all these things
def test_fremont_data():
    data = get_fremont_data()
    assert all(data.columns == ['West', 'East', 'Total'])
    assert isinstance(data.index, pd.DatetimeIndex)
