#RandomPoint : create a rondom point feature class and save X , Y data in Text file
#Purpose: To Create folder.
#Input: Workspace and link of Txt file.
#Output: Point feature class with attributes
#Author: Sagar Chougule / sagar4gis@gmail.com / 08/12/2021

import os

out1 = open(arcpy.GetParameterAsText(0),'w')


#import arcpy module
import arcpy
from arcpy import env
env.workspace = arcpy.GetParameterAsText(1)
myPath = env.workspace
print('workspace',myPath)



#overwrite of output files
arcpy.env.overwriteOutput = True



out = arcpy.GetParameterAsText(2)
#Create point feature class
fcfile = arcpy.CreateFeatureclass_management(myPath,out,"POINT")



#get message of output feature and write in text file
out1.write(arcpy.GetMessages())



#write code to next line
out1.write('\n\n')


#create fields
arcpy.AddField_management(fcfile,'Rn_ID',"SHORT")



#get message of output feature field and write in text file
out1.write(arcpy.GetMessages())



#write code to next line
out1.write('\n\n')



print('Creating a feature')

#import random module
import random
pointRows = arcpy.da.InsertCursor(fcfile,['Rn_ID','Shape'])
for pt in range(1,101):
    X = random.random() - 148.0
    Y = random.random() + 64.0
    pointRows.insertRow([pt,[X,Y]])
    


del pointRows

#close txt file
out1.close()

