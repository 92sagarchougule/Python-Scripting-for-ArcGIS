import arcpy, numpy
arcpy.env.workspace = r'D:\DataforArcObject'
fc = 'Building'
d = {}
sc = arcpy.da.SearchCursor(fc, ['AgeBuilding', 'PolyArea'])
for row in sc:
    cover = row[0]
    area = row[1]
    if d.has_key(cover):
        d[cover].append(area)
    else:
        d[cover] = [area]
        
del sc
for k, v in d.items():
    median = numpy.median(v)
    print '''Polygons with cover '{0}' have \
 median area {1}'''.format(k, median)
 

for k, v in d.items():
...     median = numpy.sum(v)
...     print '''Polygons with cover '{0}' have Total area {1}'''.format(k, median)
