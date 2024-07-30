#Add Field Table.py
#Purpose: To create table and add field
#Input: Workspace containing table.
#Output: add field to created table.
#Author: Sagar Chougule / sagar4gis@gmail.com / 01/12/2021

#import modules
import arcpy
from arcpy import env


#Add workspace
wopace = env.workspace = arcpy.GetParameterAsText(0)


#Create Tabel using below object

NameTable = arcpy.GetParameterAsText(1)

table = arcpy.CreateTable_management(wopace,NameTable)


NameField = arcpy.GetParameterAsText(2)


#Create a field to above created table
arcpy.AddField_management(table,NameField,"TEXT")
