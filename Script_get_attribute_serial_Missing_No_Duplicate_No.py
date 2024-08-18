#Author: Sagar Chougule / sagar4gis@gmail.com 

#import arcpy library
import arcpy


# Select Fc or Shapefile
fc = arcpy.GetParameterAsText(0) 

# Select Field
#fieldName =  arcpy.GetParameterAsText(1)


    

cursor = arcpy.da.SearchCursor(fc,['CHALTA_NO'])  #Field_No
a = []
for row in cursor:
    a.append(row[0])
    

def findMissingNumbers(a):
    numbers = set(a)
    length = len(a)
    output = []
    for i in range(1, a[-1]):
        if i not in numbers:
            output.append(i)
    return output

arcpy.AddMessage('\n')

arcpy.AddMessage('--------MISSING NUMBERS--------')

    
arcpy.AddMessage(findMissingNumbers(a))

arcpy.AddMessage('\n')



mylist = a 
newlist = [] 
duplist = [] 
for i in mylist:
    if i not in newlist:
        newlist.append(i)
    else:
        duplist.append(i) 

print("List of duplicates", duplist)
print("Unique Item List", newlist) # pr

arcpy.AddMessage('--------DUPLICATE NUMBERS--------')
arcpy.AddMessage(duplist)


arcpy.AddMessage('\n')

