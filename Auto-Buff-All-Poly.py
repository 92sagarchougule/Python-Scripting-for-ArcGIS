#Auto-Buff-All-Poly.py
#Purpose: To do all polygon features in a workspace.
#Input: Workspace containing feature classes.
#Example input: "c:/temp/"
#Output: Tool automatically will select polygon features from workspace and save buffer files
#Author: Sagar Chougule / sagar4gis@gmail.com / 20/11/2021

import arcpy, os, sys
from arcpy import env

env.workspace = arcpy.GetParameterAsText(0)
outfolder = arcpy.GetParameterAsText(1)

fc = arcpy.ListFeatureClasses('*.shp*','Polygon')


for fcs in fc:
    basename = os.path.splitext(fcs) [0]
    output = outfolder + basename + 'Out.shp'
    out = arcpy.Buffer_analysis(fcs, output, '500 Meters')
    arcpy.AddMessage(out)

