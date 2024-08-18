#Code for Select Mxd filder and get each mxd layers
#Author: Sagar Chougule / sagar4gis@gmail.com 

import arcpy
import os

from arcpy import env
env.workspace = r"C:\Users\DeepOcean\Desktop\mxd"

a= 0

for mxd in arcpy.ListFiles('*mxd'):
	a +=1
	print(a, mxd)
	mxd_path = os.path.join(arcpy.env.workspace,mxd)
	mxd = arcpy.mapping.MapDocument(mxd_path)
	layer_list = arcpy.mapping.ListLayers(mxd)
	for ins in layer_list:
		print('layer : {0}'.format(ins))


