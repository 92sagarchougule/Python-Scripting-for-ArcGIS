#Area Calculate in Mtr.py
#Purpose: Calculate area of selcted feature class and create anoterh feature class in a workspace.
#Input: Workspace containing feature classes.
#Example input: "c:/temp/"
#Output: Create new feature class with calcualted area.
#Author: Sagar Chougule / sagar4gis@gmail.com / 10/01/2019

import arcpy

#GET the input workspace from the use.

#GET a list of the feature classes.
fc = arcpy.GetParameterAsText(0)
fcout = arcpy.GetParameterAsText(1)

arcpy.CalculateAreas_stats(fc, fcout)



#PRINT basic information about each feature class in the folder.

arcpy.AddMessage('-------------------')
#arcpy.AddMessage(fc)
arcpy.AddMessage('Area in Sq Meters')
arcpy.AddMessage('-------------------')
                
