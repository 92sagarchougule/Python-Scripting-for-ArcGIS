#Find Text Files.py
#Purpose: Find ASCII (Text) files in a workspace.
#Input: Workspace containing feature classes.
#Example input: "c:/temp/"
#Output: List of Text file names.
#Author: Sagar Chougule / sagar4gis@gmail.com / 12/01/2020

import arcpy, os

#GET the input workspace from the use.

#GET a list of the feature classes.
folder = arcpy.GetParameterAsText(0)

filelist = os.listdir(folder)

for i in filelist:
    if i.endswith('.txt'):
        print(i)
        #Add output to message box
        arcpy.AddMessage('-------------------')
        arcpy.AddMessage(i)

                
