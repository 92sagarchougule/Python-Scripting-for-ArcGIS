import arcpy
import os

# Input variables
input_dataset = arcpy.GetParameterAsText(0) #r"C:\MyProjects\MyProject.gdb\fds" - FeatureDataset
topo_name = arcpy.GetParameterAsText(1) #"Topology" - Stream
cluster_tol = 0.001
input_fc = arcpy.GetParameterAsText(2) #r"C:\MyProjects\MyProject.gdb\fds\fc1 1 1;C:\MyProjects\MyProject.gdb\fds\fc2 1 1"
rules = r"'Must Not Overlap (Area)' C:\MyProjects\MyProject.gdb\fds\fc1 # C:\MyProjects\MyProject.gdb\fds\fc1 #;'Must Be Covered By Feature Class Of (Area-Area)' C:\MyProjects\MyProject.gdb\fds\fc1 # C:\MyProjects\MyProject.gdb\fds\fc2 #"
validate = "true"

# Create the topology
out_topo = arcpy.CreateTopology_management(input_dataset, topo_name, cluster_tol)
print("Created topology.")

# Loop through the list of feature classes and add them to the topology
input_fcL = input_fc.split(";")
for fc in input_fcL:
    param = fc.rsplit(" ", 2)
    in_fc = param[0]
    xy_rank = param[1]
    z_rank = param[2]
    arcpy.AddFeatureClassToTopology_management(out_topo, in_fc, xy_rank, z_rank)
    print(arcpy.GetMessages())
    
# Loop through the list of rules and add rules to the topology
rulesL = rules.split(";")
for rule in rulesL:
    r = rule.rsplit(" ", 4)
    rule_type = r[0].replace("'","")
    in_fc1 = r[1]
    subtype1 = r[2]
    in_fc2 = r[3]
    subtype2 = r[4]
    arcpy.AddRuleToTopology_management(out_topo, rule_type, in_fc1, subtype1, in_fc2, subtype2)
    print(arcpy.GetMessages())
    
# Validate the topology
if validate == "true":
    try:
        arcpy.ValidateTopology_management(out_topo)
    except:
        print(arcpy.GetMessages())
print("Finished.")
