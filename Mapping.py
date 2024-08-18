#Author: Sagar Chougule / sagar4gis@gmail.com 


import arcpy
from arcpy import env
env.workspace = r'D:\CityOfOleander.mdb'
mapdoc = arcpy.mapping.MapDocument('Current')
mapdoc.title = 'Property Map'
mapdoc.author = 'KSRDPR University'
mapdoc.description = 'Property Tax Collection Mapping'
mapdoc.makeThumbnail='true'
flist = arcpy.ListFeatureClasses()
df = arcpy.mapping.ListDataFrames(mapdoc)[0]
for i in flist:
    lyr = arcpy.mapping.Layer(i)
    adlyr = arcpy.mapping.AddLayer(df,lyr)
    
map = arcpy.mapping.ExportToPDF(mapdoc,r'D:\TempData\PropertyMap.pdf')

