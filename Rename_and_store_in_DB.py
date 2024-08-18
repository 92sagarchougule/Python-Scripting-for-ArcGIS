
#Author: Sagar Chougule / sagar4gis@gmail.com 

import arcpy

arcpy.env.workspace = "C:\\Users\\DELL\\Desktop\\Sagar\\Sample"
fclist = arcpy.ListFeatureClasses()
folder = "C:\\Users\\DELL\\Desktop\\Sagar\\Correct_Data\\Birds.gdb"

for fc in fclist:
    # Remove '_Clip' from the feature class name
    new_fc_name = fc.replace("_Clip", "")

    # Ensure the new feature class name is a valid name
    new_fc_name = arcpy.ValidateTableName(new_fc_name, folder)

    # Full path to the new feature class in the output geodatabase
    new_fc_path = arcpy.os.path.join(folder, new_fc_name)

    # Copy the feature class to the new location
    arcpy.management.CopyFeatures(fc, new_fc_path)

    print(f"Feature class {fc} copied to {new_fc_path}")
