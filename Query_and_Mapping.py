import arcpy
from arcpy import env

env.workspace = r'D:\tmep'

shp = arcpy.GetParameterAsText(0)

query = arcpy.GetParameterAsText(1)

mapName = arcpy.GetParameterAsText(2)

arcpy.SelectLayerByAttribute_management(shp,"ADD_TO_SELECTION",query)

mxd = arcpy.mapping.MapDocument('Current')
df = arcpy.mapping.ListDataFrames(mxd)[0]
        # Call the zoomToSelectedFeatures() method of the data frame class
        #mxd.findAndReplaceWorkspacePaths(r'D:\DataforArcObject',r'D:\tmep')
        #mxd.saveACopy(r'D:\tmep\newones')
df.scale = 1000            
df.zoomToSelectedFeatures()
mxd.title = mapName
mxd.author = "Sagar Chougule"
mxd.credits = "KSRDPRU"
mxd.activeView = "Page_Layout"
mxd.description = "Map for property data and roads"


arcpy.AddMessage("\n\nFilled all Information of Properties\n\n")
arcpy.mapping.ExportToPDF(mxd,'D:/DataforArcObject/kml/'+ str(mapName))
arcpy.RefreshTOC()        
del mxd

