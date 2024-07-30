#Create-Multiple-Fields : create table and add multiple fields
#Purpose: To Create at a time multiple fields.
#Input: table name and table name.
#Output: create table and fields
#Author: Sagar Chougule / sagar4gis@gmail.com / 08/12/2021


#import modules
import os, arcpy

#add workspace
workspace = arcpy.GetParameterAsText(0)


filename = arcpy.GetParameterAsText(1)
 #create table
myTable = arcpy.CreateTable_management(workspace, filename)

#number of tables
numtable = arcpy.GetParameterAsText(2)

#for loop for table name
for i in range(1,int(numtable)):
    i+=1
    arcpy.AddField_management(myTable,'field'+ str(i),"TEXT")
    #arcpy.GetMessages(a)
    
    

