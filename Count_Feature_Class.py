import arcpy

arcpy.env.workspace = "C:\\Users\\DELL\\Desktop\\Sagar\\Correct_Data\\Birds.gdb"
fclist = arcpy.ListFeatureClasses()
folder = "C:\\Users\\DELL\\Desktop\\Sagar\\Correct_Data\\All_Data.gdb"
output_fc_name = "Intersect_Bird_"

# Full path to the output feature class in the output geodatabase
new_fc_path = arcpy.os.path.join(folder, output_fc_name)

# Check if there are at least two feature classes to intersect
if len(fclist) < 2:
    print("At least two feature classes are required for intersection.")
else:
    # Check if any of the input feature classes is empty
    empty_feature_classes = [fc for fc in fclist if arcpy.management.GetCount(fc) == 0]

    if empty_feature_classes:
        print(
            f"Warning: The following feature classes are empty: {', '.join(empty_feature_classes)}"
        )
    else:
        # Check if the input feature classes have the same spatial reference
        spatial_references = set(
            [arcpy.Describe(fc).spatialReference.name for fc in fclist]
        )

        if len(spatial_references) > 1:
            print("Warning: Input feature classes have different spatial references.")
        else:
            # Perform intersection only if there are no issues
            arcpy.analysis.Intersect(fclist, new_fc_path)

            # Check if the output feature class is not empty
            output_count = int(arcpy.management.GetCount(new_fc_path).getOutput(0))
            input_count = sum(
                [int(arcpy.management.GetCount(fc).getOutput(0)) for fc in fclist]
            )

            if output_count == 0:
                print("Warning: Empty output generated during intersection.")
            elif output_count < 0.5 * input_count:
                print(
                    "Warning: Output feature count is significantly lower than expected."
                )
            else:
                print(f"Intersection result saved to {new_fc_path}")
