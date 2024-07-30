#RasterToASCII.py
#Purpose: To create database, dataset and Line feature class in a workspace.
#Input: Workspace containing Raster data.
#Example input: "c:/temp/"
#Output: Raster file to ASCII/Text file
#Author: Sagar Chougule / sagar4gis@gmail.com / 27/11/2021

import arcpy

from arcpy import env

env.workspace = r'D:\Temp'

arcpy.CheckInExtension('Spatial')



arcpy.env.overwriteOutput = 'True'


fcdir = arcpy.GetParameterAsText(0)


fcdirout = arcpy.GetParameterAsText(1)



arcpy.RasterToASCII_conversion(fcdir,fcdirout)

