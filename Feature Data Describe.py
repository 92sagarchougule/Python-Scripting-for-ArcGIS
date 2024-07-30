#Feature Data Describe.py
# Purpose: Print basic information about each feature class in a workspace.
#Input: Workspace containing feature classes.
#Example input: "c:/temp/"
#Output: A list of basic information about feature class.
#Author: Sagar Chougule /  sagar4gis@gmail.com / 7/20/2023

import arcpy

#GET the input workspace from the use.

#GET a list of the feature classes.
fc = arcpy.GetParameterAsText(0)


desc = arcpy.Describe(fc)


#PRINT basic information about each feature class in the folder.

print("Data Type         {0}".format(desc.DataType));
print("Data class:        {0}".format(desc.DataSetType));
print("Type:                 {0}".format(desc.FeatureType));
print("Shape type        {0}".format(desc.ShapeType));
print("Has M:                {0}".format(desc.HasM));
print("Has z:                  {0}".format(desc.HasZ));
print("\n");

#add the output to message box.
arcpy.AddMessage('-----------------------')
arcpy.AddMessage(desc.DataType)
arcpy.AddMessage(desc.DataSetType)
arcpy.AddMessage(desc.FeatureType)
arcpy.AddMessage(desc.ShapeType)
arcpy.AddMessage(desc.DataType)
arcpy.AddMessage(desc.HasM)
arcpy.AddMessage(desc.HasZ)
arcpy.AddMessage('-----------------------')

                
