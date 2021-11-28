#Find JPEG File.py
#Purpose: To find jpeg files in a workspace.
#Input: Workspace containing .jpeg files.
#Example input: "c:/temp/"
#Output: A list of .jpeg files in containing workspace.
#Author: Sagar Chougule / 92chougulesagar@gmail.com / 8148470091 / 12/11/2018

import arcpy, os

#GET the input workspace from the use.

#GET a list of the feature classes.
folder = arcpy.GetParameterAsText(0)

filelist = os.listdir(folder)

for i in filelist:
    if i.endswith('.jpeg'):
        print(i)
        #add the output to message box.
        arcpy.AddMessage('-------------------')
        arcpy.AddMessage(i)

                
