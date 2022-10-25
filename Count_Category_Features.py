#Count_Category_Features.py
#Developer: Sagar Chougule ,Email:92chougulesagar@gmail.com
#Using this script we can get no of counts per category

import arcpy

data = arcpy.GetParameterAsText(0)

Field = arcpy.GetParameterAsText(1)

rows = arcpy.da.SearchCursor(data,Field)

myDic ={}

for row in rows:
    key = row[0]
    if key in myDic:
        myDic[key] = myDic[key]+1
    else:
        myDic[key]=1
del rows
arcpy.AddMessage('\n')
arcpy.AddMessage('Choosed Field is : '+str(Field)+' and its Feature Count ')
arcpy.AddMessage('\n')
arcpy.AddMessage(myDic)
arcpy.AddMessage('\n')

