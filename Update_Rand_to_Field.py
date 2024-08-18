#Developer: Sagar Chougule
#Script for adding random values to shp column using update cursor
#Author: Sagar Chougule / sagar4gis@gmail.com 


import random
import arcpy

fc = 'Health_Data'
    
cursor = arcpy.da.UpdateCursor(fc,["Covid_19"])
for row in cursor:
    row[0] = random.randint(10,500)
    cursor.updateRow(row)
    
del cursor
cursor = arcpy.da.UpdateCursor(fc,['Dengue'])
for row in cursor:
    row[0] = random.randint(1,10)
    cursor.updateRow(row)
    
del cursor

