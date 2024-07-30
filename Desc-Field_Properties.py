#Desc-Field.py
#Purpose: To describe fields of selected feature class.
#Input: Select feature classes.
#Example input: "c:/temp/"
#Output: will get list of fields and properties of field
#Author: Sagar Chougule / sagar4gis@gmail.com / 27/11/2021


#import module
import arcpy

#select desire feature class
fc = arcpy.GetParameterAsText(0)

#tool for feature fields
fca = arcpy.ListFields(fc)

for i in fca:
    b = i.name, i.length, i.baseName, i.precision, i.type, i.editable, i.required
    a.append(b)

for j in a:
    print(j)
    #add message
    arcpy.AddMessage('----------------------------------------------------')
    arcpy.AddMessage(j)
