import numpy as np
import xarray as xr


#Defining a function that will gather the season of a given data set
def selectSeason(ds,seas):
    ds_season = []
    #First, looping through and finding the appropriate season
    for label, group in ds.groupby('time.season'):
        if(label==seas):
            ds_season = group
            break
    #If the right season has been found in the data set, then the mean of that season can be found over the years
    ds_season = ds_season.groupby('time.year').mean('time')
    return ds_season
