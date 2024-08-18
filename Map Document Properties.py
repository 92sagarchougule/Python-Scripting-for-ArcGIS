#Author: Sagar Chougule / sagar4gis@gmail.com 

import arcpy

myMxd = arcpy.mapping.MapDocument('Current')

myMxd.author = arcpy.GetParameterAsText(0) #'Sagar Chougule'

myMxd.title = arcpy.GetParameterAsText(1) #'Stream Map'

myMxd.description = arcpy.GetParameterAsText(2) #'This map will display stream and DEM data behind'

myMxd.summary = arcpy.GetParameterAsText(3) #'take it all'

myMxd.credits = arcpy.GetParameterAsText(4) #'ESRI'

myMxd.tags = arcpy.GetParameterAsText(5) #'ESRI, GIS, ArcGIS, Streams, DEM'

myMxd.hyperlinkBase = arcpy.GetParameterAsText(6) #'https:/link/sagar'

myMxd.save()

myMxd.relativePaths = True

myMxd.makeThumbnail()

dataSaved = myMxd.dateSaved




arcpy.AddMessage(dataSaved.date())
