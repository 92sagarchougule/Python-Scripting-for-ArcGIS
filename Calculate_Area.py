#Calculate_Area.py
#Developer: Sagar Chougule
#Tool to calculate Area

import arcpy

shp = arcpy.GetParameterAsText(0)

field = arcpy.GetParameterAsText(1)

query = '!shape.area!'

arcpy.CalculateField_management(shp, field, query,"PYTHON")

arcpy.AddMessage('\n')
arcpy.AddMessage('Done')
arcpy.AddMessage('\n')


