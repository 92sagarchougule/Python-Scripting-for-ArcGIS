#Write Note.py
#Purpose: To write a note or save a code in txt file
#Input: txt file.
#Example input: "c:/temp/temp.txt"
#Output: note in notepad.
#Author: Sagar Chougule / sagar4gis@gmail.com / 30/11/2021

import arcpy
from arcpy import env



txtfile = arcpy.GetParameterAsText(0)

            
file = open(txtfile, 'w')

            
file.write(arcpy.GetParameterAsText(1))
`





