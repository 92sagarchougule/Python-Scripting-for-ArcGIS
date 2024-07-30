import arcpy
from arcpy import env
env.workspace = r"C:\Users\DeepOcean\Desktop\mxd"
import os
a = 0

for mxd in arcpy.ListFiles('*mxd'):
	print(a, mxd)
	mxd_path = os.path.join(arcpy.env.workspace,mxd)
	mxd = arcpy.mapping.MapDocument(mxd_path)
	layer_list = arcpy.mapping.ListLayers(mxd)
	if(len(layer_list)==3):
		del mxd
		print(mxd_path)
		time.sleep(5)
		os.remove(mxd_path)


