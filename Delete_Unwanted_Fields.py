#Author: Sagar Chougule / sagar4gis@gmail.com 

import arcpy

arcpy.env.workspace = "C:\\Users\\DELL\\Desktop\\Sagar\\Sample"
fclist = arcpy.ListFeatureClasses()

for fc in fclist:
    print(f"Processing {fc}:")

    # Use a generator expression to get all field names except 'sci_name' and the default geometry fields
    fields_to_delete = [field.name for field in arcpy.ListFields(fc) if field.name not in ['sci_name', 'Shape', 'SHAPE', 'FID', 'OID']]

    if fields_to_delete:
        # Delete all fields except 'sci_name'
        arcpy.DeleteField_management(fc, fields_to_delete)
        print(f"Fields deleted: {', '.join(fields_to_delete)}")
    else:
        print("No fields to delete.")

    # Add a new field named 'calc' with a float data type
    arcpy.AddField_management(fc, 'calc', 'FLOAT')

    print(f"Field 'calc' added.")

    print("=" * 50)
