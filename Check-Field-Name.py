#Check-Field-Name.py
#Purpose: To check field is available to feature class.
#Input: Workspace containing feature classes.
#Example input: "c:/temp/"
#Output: Line Feature class creation with database and dataset
#Author: Sagar Chougule / sagar4gis@gmail.com / 10/06/2021

import arcpy

from arcpy import env

fc = arcpy.GetParameterAsText(0)

fcfield = arcpy.ListFields(fc)

fname = arcpy.GetParameterAsText(1)


found = False


for fcd in fcfield:
    if fcd.name.lower() == fname.lower():
        print('Field {0} Found'.format(fname))
        arcpy.AddMessage(fname)
        arcpy.AddMessage('Found')
        found = True
    else:
        print('Field {0} Not Found'.format(fname))
        found = False
        arcpy.AddMessage(fname)
        arcpy.AddMessage('Not Found')
        

