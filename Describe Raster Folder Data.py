#Describe Raster Folder Data.py
#Purpose: Print basic information about each feature class in a workspace.
#Input: Workspace containing Raster dataset
#Example input: "c:/temp/"
#Output: A list of basic information about feature class.
#Author: Sagar Chougule / sagar4gis@gmail.com / 12/01/2019


#import modules system and arcpy
import sys, arcpy


#GET the input workspace from the use
arcpy.env.workspace = arcpy.GetParameterAsText(0)

#GET a list of the Raster files in the workspace.
fcs = arcpy.ListRasters()

#PRINT basic information about each Raster files in the folder.
print("Feature classes in folder {0}".format(arcpy.env.workspace));

for fc in fcs:
                print(fc)
                #add the output to message box.
                arcpy.AddMessage(fc)
                #add the output to message box.
		arcpy.AddMessage('----------------')
print("Feature class list complete");


                
