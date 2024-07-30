import arcpy
from arcpy import env
env.workspace = r'D:\Other\Practice'
mxd = arcpy.mapping.MapDocument('Current')
mxd.author = "Sagar Chougule"
mxd.title = "Electricity Mapping"
mxd.description = "The Python programming for analysis and mapping"
mxd.summary = "Python and ArcGIS"
mxd.credits = "KSRDPR University"
mxd.tags = "ArcGIS, QGIS, Python, ArcPy, Geospatial"
mxd.hyperlinkBase = "https://github.com/92sagarchougule"
mxd.save()
mxd.relativePaths = True
mxd.makeThumbnail()
datesave = mxd.dateSaved
type(datesave)
datesave.date()
datesave.day
datesave.date
datesave.time
dataFrame = mxd.activeDataFrame
arcpy.RefreshTOC()
