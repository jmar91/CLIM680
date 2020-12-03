# The Ability of the Mixed Layer Depth to be used as a proxy for the Atlantic Meridional Overturning Circulation in a preindustrial model simulation

## Jon Martin 


### Introduction:
The Atlantic Meridional Overturning Circulation (AMOC) is an ocean current that moves water northward near the ocean surface from the Southern Sea around Antarctica, along the east coast of South America, up North America as the Gulf Stream, and into the Larbrador Sea and the Nordic seas where water sinks toward the ocean floor and moves back to the Southern Sea. The mixed-layer depth (MLD) is defined as the depth in the ocean where density is similar to the density at the ocean surface and can be used as a basic proxy describing the strength of the MLD (although this is debated). The aim of this project is to see the effectiveness of the MLD as a descriptor of the AMOC in a 100 year sample of a Community Earth System Model (CESM) preindustrial simulation.


### Data Sets

The analysis conducted looks at the MLD and AMOC from a 3000 year long preindustrial control simulation. The data has been taken between years 2645 and 2744 of the simulation for simplicity. 
- MLD: This is fairly straightforward to gather as it is offered as a variable in the original netCDF files of the simulation's output. The only catch is that the data is originally on an irregular grid and had to be interpolated to a regular 1˚x1˚ grid before any analysis could take place. Because the AMOC is confined to the Atlantic and MLD is greatest around the Iceland Basin and the Labrador Sea, MLD between 80˚W-0˚ Longitude and 0˚-75N˚ will be examined in greater detail. located as /scratch/jmarti91/cesm_mld.nc
- AMOC: The AMOC examined as an index based off of the results of McCarthy et al (2014) where, using the RAPID mooring array located across the Atlantic at 26.5˚N, the AMOC index was defined as the maximum zonal mean current at a given latitude. Although that study used 26.5˚N as the latitude to define the index for this analysis. Located at /scratch/jmarti91/cesm_maxAMOC.nc


### Analysis/Results: 
[Results](https://github.com/jmar91/CLIM680/blob/master/Project.ipynb)

### Summary

This analysis shows that the greatest MLD occurs during the spring, particularly around the Iceland Basin. In years where the AMOC is above average, the MLD around this region is significantly deeper than in years where the strength of the AMOC is below the mean. The correlation map shows a slight positive correlation around this region, which is further bolstered by both linear regression and tests for statistical significance. In addition, the regression analysis and correlation map show an anticorrelation between the AMOC index and the MLD between 25˚N and 35˚N in the Atlantic. Overall, the MLD does appear to serve as a generally useful proxy for the strength for the AMOC. One caveat with these results is the low MLD elsewhere in the Subtropical Atlantic, in particular the labrador sea.
