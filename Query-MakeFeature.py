#Query Make Feature.py
#Purpose: To create feature class using query.
#Input: Workspace containing feature classe.
#Example input: "c:/temp/"
#Output: Create new feature class.
#Author: Sagar Chougule / sagar4gis@gmail.com / 10/11/2021

import arcpy
from arcpy import env



Fc = arcpy.GetParameterAsText(0)

Fcout = arcpy.GetParameterAsText(1)


query = '"Shape_Area" >= 5000'



arcpy.MakeFeatureLayer_management(Fc, Fcout, query)
