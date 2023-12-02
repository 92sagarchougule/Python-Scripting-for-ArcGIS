import arcpy

# Set the workspace environment
arcpy.env.workspace = r"C:\Users\DELL\Desktop\Sagar\Output\dbs.gdb"

# Set the input feature class or table
input_table = r"C:\Users\DELL\Desktop\Sagar\Output\dbs.gdb\OutPut"

# field list
fld_list = r"C:\Users\DELL\Desktop\Sagar\Output\dbs.gdb\OutPut"

# List of fields to be added
fields_to_add = arcpy.ListFields(fld_list, "*calc*")


# Field containing the result
result_field = "All_Total"

# Use the SearchCursor to iterate through rows and calculate the result
with arcpy.da.UpdateCursor(input_table, fields_to_add + [result_field]) as cursor:
    for row in cursor:
        # Sum values from each field and update the result field
        row[-1] = sum(row[:-1])
        cursor.updateRow(row)

print("Field calculation completed.")
