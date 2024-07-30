#CalculateFieldArea.py
#Purpose: To create database, dataset and Line feature class in a workspace.
#Input: Workspace containing feature classes.
#Example input: "c:/temp/"
#Output: Line Feature class creation with database and dataset
#Author: Sagar Chougule / sagar4gis@gmail.com / 27/11/2021


import arcpy

from arcpy import env

env.overwriteOutput = 'True'

expression = '!shape.area!'

fc = arcpy.GetParameterAsText(0)

field = arcpy.GetParameterAsText(1)

out = arcpy.CalculateField_management(fc,field,expression,"PYTHON")

arcpy.AddMessage(out)

