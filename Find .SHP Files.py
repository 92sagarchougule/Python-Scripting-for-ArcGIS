# Find.SHP Files.py
#Purpose: To find .shp files in a workspace.
#Input: Workspace containing feature classes.
#Example input: "c:/temp/"
#Output: Display a list of contining feature class.
#Author: Sagar Chougule / sagar4gis@gmail.com / 12/10/2020

import arcpy, os

#GET the input workspace from the use.

#GET a list of the feature classes.
folder = arcpy.GetParameterAsText(0)

filelist = os.listdir(folder)

for i in filelist:
    if i.endswith('.shp'):
        print(i)
        #add the output to message box.
        arcpy.AddMessage('-------------------')
        arcpy.AddMessage(i)

                
