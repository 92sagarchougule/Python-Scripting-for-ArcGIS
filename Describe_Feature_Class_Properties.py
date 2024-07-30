#describe.py
#Purpose: to know what are the feature class in a workspace.
#Input: Workspace
#Example input: "c:/temp/"
#Output: name of feature class.
#Author: Sagar Chougule / sagar4gis@gmail.com / 12/11/2018

#import modules system and arcpy
import sys, arcpy

#GET the input workspace from the use
arcpy.env.workspace = arcpy.GetParameterAsText(0)

#GET a list of the feature classes in the workspace.
fcs = arcpy.ListFeatureClasses()

#PRINT list of feature class from the folder.
print("Feature classes in folder {0}".format(arcpy.env.workspace));

for fc in fcs:
                print(fc)
                #add the output to message box.
                arcpy.AddMessage(fc)
                #add the output to message box.
		arcpy.AddMessage('-------------------')
print("Feature class list complete");
                
