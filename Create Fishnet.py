# Tool Name : fishnet
#Description:
#Author:

import arcpy

from arcpy import env

env.workspace = r'E:\1. M.Sc. Geoinformatics\1. Class\1st Year\1. SEMESTER-2\1. Subjects\GI 2.7 Advanced GIS Practicals\Lab\Lab-7\CityOfOleander.mdb'
outFeatureClass = arcpy.GetParameterAsText(0)
ordinCoordinate = '2397370 6989659'
yAxisCoordinate = '2397370 6989669'
cellSizeWidth = '528'
cellSizeHeight = '528'
numRows = '35'
numColumn = '25'
oppositCorner = '#'
labels = 'true'
templateExtent = 'City_Limit'
gemoteryType = 'POLYGON'

arcpy.CreateFishnet_management(outFeatureClass,ordinCoordinate,yAxisCoordinate,cellSizeWidth,cellSizeHeight,numRows,numColumn,oppositCorner,labels,templateExtent)

