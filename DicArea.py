# areaMedian.py
#areaMedian.py
import arcpy, numpy
fc = r'D:\DataforArcObject\Delhi.gdb\Dataset\Building'
idField = 'OBJECTID_1'
areaField = 'PolyArea'
areasDict = {}
  # Populate dictionary with id:area items.
sc = arcpy.da.SearchCursor(fc, [idField, areaField])
for row in sc:
    fid = row[0]
    area = row[1]
    areasDict[fid] = area
         
del sc
  
  # Find the median area.
areas = areasDict.values()
medianArea = numpy.median(areas)
print 'Median area: {0}'.format(medianArea)
  # Find the polygons with values close to median.
sqft = 400
print 'Polygons close to median:'
for k, v in areasDict.items():
    if medianArea - sqft < v < medianArea + sqft:
        print '{0}: {1}, {2}: {3}'.format(idField, k, areaField, v) 
    
         
