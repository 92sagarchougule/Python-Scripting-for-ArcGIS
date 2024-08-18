#Author: Sagar Chougule / sagar4gis@gmail.com 

# Import the required modules
import os
import arcpy

# Allow overwriting of output
arcpy.env.overwriteOutput = True

# Set current workspace
arcpy.env.workspace = r'D:\TmpGIS'

# Get a list of shapefiles in folder
fcs = arcpy.ListFeatureClasses()

# Find the total count of shapefiles in list
fc_count = len(fcs)

# Set the progressor
arcpy.SetProgressor("step", "Copying shapefiles to geodatabase...",
                    0, fc_count, 1)

# Create a file gdb to contain new feature classes
arcpy.CreateFileGDB_management(arcpy.env.workspace, "fgdb.gdb")

# For each shapefile, copy to a file geodatabase
for shp in fcs:
    # Trim the '.shp' extension
    fc = os.path.splitext(shp)[0]

    # Update the progressor label for current shapefile
    arcpy.SetProgressorLabel("Loading {0}...".format(shp))

    # Copy the data
    arcpy.CopyFeatures_management(shp, os.path.join("fgdb.gdb", fc))

    # Update the progressor position
    arcpy.SetProgressorPosition()

arcpy.ResetProgressor()

