#Create Point Feature.py
#Purpose: To create database, dataset and Point feature class in a workspace.
#Input: Workspace containing feature classes.
#Example input: "c:/temp/"
#Output: Point Feature class creation with database and dataset
#Author: Sagar Chougule / sagar4gis@gmail.com / 26/11/2021

import arcpy

#GET the input workspace from the use.

#Set workspace.
Workspace = arcpy.GetParameterAsText(0)


#Input name of database
Fc = arcpy.GetParameterAsText(1)

database = arcpy.CreateFileGDB_management(Workspace,Fc)

#Input name of dataset
namedataset = arcpy.GetParameterAsText(2)

dataset = arcpy.CreateFeatureDataset_management(database,namedataset,'WGS 1984')

#Input name of point feature class
FeatureName = arcpy.GetParameterAsText(3)

feature = arcpy.CreateFeatureclass_management(dataset,FeatureName,"POINT")
                
