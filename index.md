# The Use of the Mixed Layer Depth as a Proxy for the Strength of the Atlantic Meridional Overturning Circulation in a Preindustrial Control Simulation

## Jon Martin  


### Introduction:
The Atlantic Meridional Overturning Circulation (AMOC) is an ocean current that sea moves water between the northern and southren oceans. Starting in the Southern Ocean around Antarctica, water upwelled near the ocean surface from the deep ocean moves northward along the east coast of South America and up the east coast of North America as the Gulf Stream. After leaving the Gulf stream to form the North Atlantic current near Greenland, the water will separate into the Larbrador Sea and the Nordic seas where it is forced to sink toward the ocean floor and move back to the Southern Sea along the East coast of North and South America. The mixed-layer depth (MLD) is defined as the depth from the surface of the ocean where density is relatively similar. In observations, the MLD in the North Atlantic is deepest in the winter around both the Labrador and Nordic seas, which overlaps with the regions where the AMOC moves water from the surface to the deep ocean. Because of that, the MLD can be considerd to play a role in the deepwater formation essential to the flow of the AMOC. The aim of this project is to see the effectiveness of the MLD as a proxy of the AMOC in a 100 year sample of a long Community Earth System Model (CESM) preindustrial simulation.


### Data Sets

This analysis examines the MLD and AMOC taken from a sample of a 3000 year long preindustrial control simulation. The data has been taken between years 2645 and 2744 of the simulation based on the behaivor of ocean temperatures in the Northern Atlantic found in a prior set of analyses.   
- MLD: The original MLD data from the simulation files was on an irregular grid and had to be interpolated to a regular 1˚x1˚ grid and saved on a separate netCDF before any analysis could take place. Because the AMOC is confined to the Atlantic and the MLD associated with deepwater formation is close to the North Pole, the MLD between 80˚W-0˚ Longitude and 0˚-75N˚ will be examined in greater detail.
- AMOC: The AMOC examined as an index based off of a paper written by McCarthy et al (2014) where, using the RAPID mooring array located across the Atlantic at 26.5˚N, the AMOC index was defined as the maximum zonal mean current at a given latitude. Although that study used 26.5˚N as the latitude to define the index for this analysis is going to be 30˚N.


### Analysis/Results:
The analysis is conducted and documented in the notebook in the link below. It includes a helper function in a file utils.py that isolates a specific season of the MLD. The deepest MLD in the Spring (March-April-May) is compared to the annual means of the maximum AMOC for the 100 year run.
[Results](https://github.com/jmar91/CLIM680/blob/master/Project.ipynb)

### Summary

The greatest MLD occurs during the spring (MAM) around the Iceland Basin. In years where the AMOC is above average, the MLD around this region is significantly deeper than in years where the strength of the AMOC is below the mean. The correlation map shows a slight positive correlation around this region, which is further supported by both linear regression and tests for statistical significance that show a strong positive relationship between the max AMOC and the MLD around the Iceland Basin.  What can be gathered from these results is that, while the MLD is not perfectly related to the AMOC in the Northern Atlantic, it does function as a useful proxy for deepwater formation in this simulation. Two technical challenges that had to be overcome in this process were to figure out how to get means of the data for each year and for a season, and to specify and area of interest in cartopy, in this case the North Atlantic.