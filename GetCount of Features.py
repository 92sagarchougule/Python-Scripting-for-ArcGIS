#GetCount.py
#Purpose: to calculate number of feature are available in feature layer or class
#Input: Workspace containing feature classes.
#Example input: "c:/temp/"
#Output: A list of basic information about feature class.
#Author: Sagar Chougule / sagar4gis@gmail.com / 12/11/2018

import arcpy

#GET the input workspace from the use.

#GET a list of the feature classes.
fc = arcpy.GetParameterAsText(0)


desc = arcpy.GetCount_management(fc)


#PRINT basic information about each feature class in the folder.

#add the output to message box.
arcpy.AddMessage('-------------------')
arcpy.AddMessage('Total Count is:')
arcpy.AddMessage(desc)
arcpy.AddMessage('-------------------')
                
