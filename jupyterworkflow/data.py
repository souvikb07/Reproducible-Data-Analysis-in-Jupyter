# Import the libraries
import os
from urllib.request import urlretrieve

import pandas as pd

FREMONT_URL = 'https://data.seattle.gov/api/views/mdbt-9ykn/rows.csv?accessType=DOWNLOAD'

# create a function to download the data
def get_fremont_data(filename='Fremont.csv', url=FREMONT_URL, force_download=False):
    """ Download and cache the fremont data

	Parameters
	==========
	filename : string(optional)
	   location to save the data
    url : string(optional)
        web location of the data
    force_download : boolean(optional)
        if True, force redownload of data

    returns
    =======
    data : pandas.Dataframe
        The fremont bridge data
    """
    if force_download or not os.path.exists(filename):
        urlretrieve(url, filename)
    data = pd.read_csv('Fremont.csv', index_col = 'Date', parse_dates=True)
    data.columns = ['West', 'East']
    data['Total'] = data['West'] + data['East']

    return data
