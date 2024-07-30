#Create-Point-Feature-Attribute.py
#Purpose: To Create Point Feature and drow some points using xy.
#Output: Point feature class with some attribute and x, y coordinate data.
#Author: Sagar Chougule / sagar4gis@gmail.com / 01/12/2021

#import modules
import arcpy
from arcpy import env

#import workspace
workspace = arcpy.GetParameterAsText(0)

fc = arcpy.GetParameterAsText(1)

#create point future using below object
fclc = arcpy.CreateFeatureclass_management(workspace, fc ,"POINT")

#update attribute using insert cursor
editpoint = arcpy.da.InsertCursor(fclc ,"*")
editpoint.fields
count = 0

#for loop for fill attributes 
for x in [0,20]:
    for y in [0,20]:
        point_obj = arcpy.Point(x, y)
        row = [count, point_obj]
        editpoint.insertRow(row)
        print(count, x, y)
        count = count + 1
        
del row
del editpoint

#update x, y coordinates to point
arcpy.AddXY_management("points")

