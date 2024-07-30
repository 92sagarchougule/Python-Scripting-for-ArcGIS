#Add Table to Point feature Class 
#Purpose: To add table to point feature class.
#Input: table name and feature class.

#Author: Sagar Chougule / sagar4gis@gmail.com / 08/12/2021

import arcpy
inputPointfc = arcpy.GetParameterAsText(0)
inputTable = arcpy.GetParameterAsText(1)
outfc = arcpy.GetParameterAsText(2)



arcpy.AddMessage('Input Feature Class :'+ inputPointfc)
arcpy.AddMessage('Input Table:' + inputTable)
arcpy.AddMessage('Output Feature Class:'+outfc)

