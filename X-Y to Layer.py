#X-Y-to-Layer.py
#Purpose: To create point feature class using (lat/long) data from csvin a workspace.
#Input: X, Y column data .csv.
#Example input: "c:/temp/"
#Output: Line Feature class creation with database and dataset
#Author: Sagar Chougule / sagar4gis@gmail.com / 16/02/2020

import arcpy, os, sys

arcpy.env.workspace = arcpy.GetParameterAsText(0)


tables = arcpy.ListTables('*23-11*')

arcpy.env.overwriteOutput = True

outdir = arcpy.GetParameterAsText(1)


if not os.path.exists(outdir):
    os.mkdir(outdir)

temppoints = 'temppoints'

    
for table in tables:
    linefile = outdir+ os.path.splitext(table) [0] + 'Line'
    arcpy.MakeXYEventLayer_management(table, 'Y', 'X', temppoints)
    arcpy.PointsToLine_management(temppoints, linefile)
    print('\t {0} / {1} created '.format(arcpy.env.workspace,linefile))
    

    

