#34.DEM to Streams.py
#Purpose: To Extract stream lines from DEM data
#Input: DEM data.
#Example input: "DEM.tiff"
#Output: Stream in polyline features.
#Author: Sagar Chougule / 92chougulesagar@gmail.com / 8148470091 / 11/12/2020

#import module
import arcpy

#import environment
from arcpy import env
arcpy.env.overwriteOutput = True


#import spatial module using *
from arcpy.sa import *

#add workspace
arcpy.env.workspace = arcpy.GetParameterAsText(0)

#add DEM data
elvRaster = arcpy.GetParameterAsText(1)


#output polyline
polyfile = arcpy.GetParameterAsText(2)


#stream order method of
strOrder = 'Strahler'

#fill raster
fillRaster = Fill(elvRaster)


#flow direction analysis
flowdirs = FlowDirection(fillRaster)

#flow accumulation analysis
flowaccurast = FlowAccumulation(flowdirs)


threshold = 2000

#query for stream analysis

myQuery = 'Value < 2000'
chanRaster = SetNull(flowaccurast,"1",myQuery)


#stream analysis
strRaster = StreamOrder(chanRaster,flowdirs,strOrder)


#conversion from raster to polyline feature
arcpy.RasterToPolyline_conversion(strRaster,polyfile)
arcpy.GetMessages()

