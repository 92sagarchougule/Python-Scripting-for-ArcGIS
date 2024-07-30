#Create Polygon Feature.py
#Purpose: To create database, dataset and Polygon feature class in a workspace.
#Input: Workspace containing feature classes.
#Example input: "c:/temp/"
#Output: Polygon Feature class creation with database and dataset
#Author: Sagar Chougule / sagar4gis@gmail.com / 25/11/2021

import arcpy

#GET the input workspace from the use.

#Set Environment
Workspace = arcpy.GetParameterAsText(0)

#Input database name
Fc = arcpy.GetParameterAsText(1)

database = arcpy.CreateFileGDB_management(Workspace,Fc)

#Input dataset name
namedataset = arcpy.GetParameterAsText(2)

dataset = arcpy.CreateFeatureDataset_management(database,namedataset,'WGS 1984')

#Input feature class name
FeatureName = arcpy.GetParameterAsText(3)

feature = arcpy.CreateFeatureclass_management(dataset,FeatureName,"POLYGON")
                
