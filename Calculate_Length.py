#Calculate_Area.py
#Author: Sagar Chougule / sagar4gis@gmail.com 
#Tool to calculate Area

import arcpy

shp = arcpy.GetParameterAsText(0)

field = arcpy.GetParameterAsText(1)

query = '!shape.length!'

arcpy.CalculateField_management(shp, field, query,"PYTHON")

arcpy.AddMessage('\n')
arcpy.AddMessage('Done')
arcpy.AddMessage('\n')


