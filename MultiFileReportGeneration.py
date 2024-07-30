#Developer Name: Sagar Chougule
#Email: 92chougulesagar@gmail.com

import arcpy
from arcpy import env
env.workspace = r'E:\5. KRSRDPU\Projects\New University Site Project\GIS Project\Shapefiles'

a = 1
for i in fclist:
    numb = arcpy.GetCount_management(i)
    a+=1
    Tfile.writelines('{0}\t : {1}\t : \t{2}\n\n'.format(a,i,numb))
    
Tfile.close()

