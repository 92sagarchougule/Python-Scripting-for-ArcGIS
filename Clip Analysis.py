#Clip Analysis.py
#Purpose: To clip feature layers
#Input: Workspace containing feature classes.
#Example input: "c:/temp/"
#Output: Clip feature class.
#Author: Sagar Chougule / sagar4gis@gmail.com / 09/03/2021      
 
import arcpy

#GET the input workspace from the use.

#GET a list of the feature classes.
fc = arcpy.GetParameterAsText(0)

#Input Feature Class
clipfc = arcpy.GetParameterAsText(1)

fcout = arcpy.GetParameterAsText(2)

#Clip feature class 
arcpy.Clip_analysis(fc, clipfc, fcout)              
