#Create Database & Dataset.py
#Purpose: To Create Database & Dataset in a workspace.
#Input: Workspace containing feature classes.
#Example input: "c:/temp/"
#Output: Creation of Database and Dataset.
#Author: Sagar Chougule / sagar4gis@gmail.com / 12/11/2018

import arcpy

#GET the input workspace from the use.

#Set Workspace.
Workspace = arcpy.GetParameterAsText(0)


#Enter Database name.
Fc = arcpy.GetParameterAsText(1)

database = arcpy.CreateFileGDB_management(Workspace,Fc)

#Enter Dataset name.
namedataset = arcpy.GetParameterAsText(2)

dataset = arcpy.CreateFeatureDataset_management(database,namedataset, 'WGS 1984')


                
