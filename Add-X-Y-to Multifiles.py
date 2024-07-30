#Add-X-Y-to Multifiles.py
#Purpose: To Raster Square Root calculation
#Input: Selected Raster.
#Example input: "c:/temp/"
#Output: Raster file.
#Author: Sagar Chougule / sagar4gis@gmail.com / 02/12/2021


#import modules
import arcpy
from arcpy import env

#add workspace where point feature class is available
env.workspace = arcpy.GetParameterAsText(0)

#select point feature class
fc = arcpy.ListFeatureClasses('*','Point')


#add x,y coordinates using for loop
for fcl in fc:
    arcpy.AddXY_management(fcl)

    

