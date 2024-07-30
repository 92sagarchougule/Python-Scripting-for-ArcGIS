#Buffer.py
#Purpose: To Buffer all feature class in a workspace.
#Input: Workspace containing feature classes.
#Example input: "c:/temp/"
#Output: Buffer to feature class.
#Author: Sagar Chougule / sagar4gis@gmail.com / 28/10/2020

import arcpy, os

#GET the input workspace from the use.

#GET a list of the feature classes.
fc = arcpy.GetParameterAsText(0)

fcout = arcpy.GetParameterAsText(1)

add = arcpy.GetParameterAsText(2)

#number to string
test = str(add)

#string to '10 Meters;
distance = test + ' Meters'

#buffer analysis
buff = arcpy.Buffer_analysis(fc, fcout, distance)

                
