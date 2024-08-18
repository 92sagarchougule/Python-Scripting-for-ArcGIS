
#Author: Sagar Chougule / sagar4gis@gmail.com 


import arcpy

from arcpy import env

ecs = env.workspace = r'D:\General\Professional\1. Ph.D\Agrani\GIS data\Vector Data\Shapefiles'

row = arcpy.da.SearchCursor(r'E:\5. KRSRDPU\Nagavi Mapping\Styles\LuLc.shp',['FID','Shape','Name','Area'])

#files = open(r'D:\consumer.txt','w');
g = 0
b =0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
j = 0
q = 0
k = 0
l = 0
m = 0
n = 0
o = 0
p = 0
for i in row:
    a = str(i[0])+' : '+ str(i[1]) + ' : '+ str(i[2]) +' : '+ str(i[3]) +'\n'
    #a = ('ID : ',str(i[0]),'Shape Lenth :',str(i[1]),'FID :',str(i[2]),'FId Stream :', str(i[3]),'Grid code : ',str(i[4]))
    #files.writelines(a);
    
    if(row[2] == 'Agriculture'):
        b+=1
        Agriculture = b
        
        #print(a)
    elif(row[2] == 'Hill/OpenLand'):
        c+=1
        OpenLand = c

    elif(row[2] == 'Fallow Land'):
        d+=1
        Fallow = d

    elif(row[2] == 'Openland'):
        e+=1
        Openland = e

    elif(row[2] == 'Settlment'):
        f+=1
        Settlment = f

    elif(row[2] == 'Plantation'):
        h+=1
        Plantation = h

    elif(row[2] == 'Fram Pond'):
        q += 1
        Fram = q

    elif(row[2] == 'Road'):
        j+=1
        Road = j

    elif(row[2] == 'Vegetation'):
        k+=1
        Vegetation = k

    elif(row[2] == 'IFL'):
        l+=1
        IFL = l

    elif(row[2] == 'Mining'):
        m+=1
        Mining = m

    elif(row[2] == 'Stream'):
        n+=1
        Stream = n

    elif(row[2] == 'Lake'):
        o+=1
        Lake = o

    elif(row[2] == 'Water body'):
        p+=1
        Water = p

    else:
        #print(a)
        pass

print('Agriculture Count is :',Agriculture)
print('OpenLand Count is :',OpenLand)
print('Fallow Count is :',Fallow)
print('Openland Count is :',Openland)
print('Settlment Count is :',Settlment)
print('Plantation Count is :',Plantation)
print('Fram Count is :',Fram)
print('Road Count is :',Road)
print('Vegetation Count is :',Vegetation)
print('Mining Count is :',Mining)
print('Stream Count is :',Stream)
print('Lake Count is :',Lake)
print('Water Count is :',Water)
print('IFL Count is :',IFL)


    
#print(g)
#files.close()



#print('hi')