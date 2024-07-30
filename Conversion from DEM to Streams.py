#34.DEM to Streams.py
#Purpose: To Extract stream lines from DEM data
#Input: DEM data.
#Example input: "DEM.tiff"
#Output: Stream in polyline features.
#Author: Sagar Chougule / sagar4gis@gmail.com / 11/12/2020

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
arcpy.AddMessage('\n\n')
arcpy.AddMessage('1). Done Raster Fill')



#flow direction analysis
flowdirs = FlowDirection(fillRaster)
arcpy.AddMessage('\n\n')
arcpy.AddMessage('2). Done Flow Direction Analysis')

#flow accumulation analysis
flowaccurast = FlowAccumulation(flowdirs)
arcpy.AddMessage('\n\n')
arcpy.AddMessage('3). Done Flow Accumulation')


threshold = 2000

#query for stream analysis

myQuery = 'Value < 2000'
chanRaster = SetNull(flowaccurast,"1",myQuery)
arcpy.AddMessage('\n\n')
arcpy.AddMessage('4). Done Stream Analysis')


#stream analysis
strRaster = StreamOrder(chanRaster,flowdirs,strOrder)
arcpy.AddMessage('\n\n')
arcpy.AddMessage('5). Done Stream Order Analysis')


#conversion from raster to polyline feature
arcpy.RasterToPolyline_conversion(strRaster,polyfile)
arcpy.AddMessage('\n\n')
arcpy.AddMessage('6). Done Polyline Analysis')

