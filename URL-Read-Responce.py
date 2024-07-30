#URL-Read-Responce.py
#Purpose: To Extract website source code from given web link
#Input: Workspace containing feature classes.
#Example input: "c:/temp/"
#Output: Source code of Website in Message box.
#Author: Sagar Chougule / sagar4gis@gmail.com / 09/12/2020

import urllib2

url = arcpy.GetParameterAsText(0)

responce = urllib2.urlopen(url)
for line in responce.readlines():
    print(line)
    arcpy.AddMessage(line)
    
responce.close()
