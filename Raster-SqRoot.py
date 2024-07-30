#GetCount.py
#Purpose: To Raster Square Root calculation
#Input: Selected Raster.
#Example input: "c:/temp/"
#Output: Raster file.
#Author: Sagar Chougule / sagar4gis@gmail.com / 12/11/2018

import arcpy

from arcpy import env


Rast = arcpy.GetParameterAsText(0)

arcpy.CheckExtension('3d')


arcpy.CheckInExtension('Spatial')


arcpy.sa.SquareRoot(Rast)

