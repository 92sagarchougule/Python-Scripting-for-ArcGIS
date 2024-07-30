
import arcpy

# Create a Describe object from the shapefile
#

fc = arcpy.GetParameterAsText(0)

desc = arcpy.Describe(fc)

# Print dataset properties
#

print('\n')
arcpy.AddMessage("Dataset Type: {0}".format(desc.datasetType))

print('\n')

arcpy.AddMessage("Extent:\n  XMin: {0}, XMax: {1}, \n YMin: {2}, YMax: {3}".format(
    desc.extent.XMin, desc.extent.XMax, desc.extent.YMin, desc.extent.YMax))

print('\n')

arcpy.AddMessage("MExtent: {0}".format(desc.MExtent))

print('\n')
arcpy.AddMessage("ZExtent: {0}".format(desc.ZExtent))

print('\n')
arcpy.AddMessage("Spatial reference name: {0}:".format(desc.spatialReference.name))


