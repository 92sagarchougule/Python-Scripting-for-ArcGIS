
#Author: Sagar Chougule / sagar4gis@gmail.com 

help(arcpy)

arcpy.env.workspace = r'D:\Delete Data'
fclist = arcpy.ListFeatureClasses()
for i in fclist:
    print(i)
    
for s in fclist:
    arcpy.DeleteFeatures_management(s)
    
for s in fclist:
    print(s)
    
for k in fclist:
    arcpy.Delete_management(k)
    
rslist = arcpy.ListRasters()
for rsl in rslist:
    print(rsl)
    
len(rslist)
for rl in rslist:
    arcpy.Delete_management(rl)
    

