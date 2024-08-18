#Author: Sagar Chougule / sagar4gis@gmail.com 

import arcpy
from arcpy import env
env.workspace = r'D:\Villages'
flist = arcpy.ListFeatureClasses()
docm = arcpy.mapping.MapDocument('Current')
dfram = arcpy.mapping.ListDataFrames(docm)[0]
dfram
for out in flist:
    lyr = arcpy.mapping.Layer(out)
    adlyr = arcpy.mapping.AddLayer(dfram,lyr)
    arcpy.RefreshTOC()
    arcpy.RefreshActiveView()


