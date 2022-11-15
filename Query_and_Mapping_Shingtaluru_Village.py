#Query_and_Mapping.py
#Purpose: To create property maps using query.
#Input: feature class.
#Output: Create Map Book.
#Author: Sagar Chougule / 92chougulesagar@gmail.com / 8148470091 / 10/11/2021

import arcpy
from arcpy import env
#Workspace
env.workspace = r'D:\tmep'

#Shapefile for query
shp = 'Propertie'
a = arcpy.GetCount_management(shp)

b = str(a)

count = int(b)

finalpdf_filename = 'D:/DataforArcObject/kml/'+'SHINGTALURU.pdf'
finalPdf = arcpy.mapping.PDFDocumentCreate(finalpdf_filename)

for prNo in range(1,444):
    arcpy.SelectLayerByAttribute_management(shp, "CLEAR_SELECTION")
    proName = 'Property : ' + str(prNo)
    prop = str(prNo)
    query = "PropertyNo = '{0}'".format(prop)
    arcpy.SelectLayerByAttribute_management(shp,"ADD_TO_SELECTION",query)
    mxd = arcpy.mapping.MapDocument('Current')
    df = arcpy.mapping.ListDataFrames(mxd)[0]
    df.scale = 1000            
    df.zoomToSelectedFeatures()
    mxd.title = proName
    mxd.author = "Sagar Chougule"
    mxd.credits = "KSRDPRU"
    mxd.activeView = "Page_Layout"
    mxd.description = "Map for property data and roads"
    arcpy.AddMessage("\n\nFilled all Information of Properties\n\n")
    arcpy.mapping.ExportToPDF(mxd,'D:/DataforArcObject/kml/'+ str(proName))
    Location = 'D:/DataforArcObject/kml/'+ str(proName)+'.pdf'
    finalPdf.appendPages(Location)
    arcpy.RefreshTOC()
finalPdf.saveAndClose()
del finalPdf
del mxd
    
