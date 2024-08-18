#Author: Sagar Chougule / sagar4gis@gmail.com 

#import modules
import arcpy

from arcpy import env

workspace = arcpy.GetParameterAsText(0)

fc = arcpy.GetParameterAsText(1)

CleanfileName = arcpy.GetParameterAsText(2)



fillgap = arcpy.FeatureclassToCoverage_conversion(fc,'outfile2')


clnfile = arcpy.Dissolve_management(r"outfile2\polygon", CleanfileName)

