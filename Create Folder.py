#Create Folder.py
#Purpose: To Create folder.
#Input: Workspace and Name for folder.
#Output: Folder
#Author: Sagar Chougule / sagar4gis@gmail.com / 06/12/2021

#import modules
import arcpy

#add workspace
folder = arcpy.GetParameterAsText(0)

#add folder name
FileName = arcpy.GetParameterAsText(1)

#Create Folder
arcpy.CreateFolder_management(folder, FileName)

