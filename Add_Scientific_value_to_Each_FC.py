import pandas as pd
import arcpy

# Path to the CSV file
csv_file_path = "C:\\Users\\DELL\\Desktop\\Sagar\\Species_Lists.csv"

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file_path)

# Convert the DataFrame to a dictionary
data_dict = df.set_index("Scientific_name").to_dict(orient="index")

# Print the dictionary
print(data_dict)

arcpy.env.workspace = "C:\\Users\\DELL\\Desktop\\Sagar\\Correct_Data\\Birds.gdb"
fclist = arcpy.ListFeatureClasses()

field_to_update = "calc"

# List to store feature class names without corresponding scientific names
feature_classes_without_scientific_name = []

for feature_class in fclist:
    # Extract the scientific name from the feature class name and convert to lowercase
    scientific_name = feature_class.replace("_shp", "").split("_")[0].lower()

    # Convert all scientific names to lowercase for a case-insensitive comparison
    data_dict_lower = {key.lower(): value for key, value in data_dict.items()}

    if scientific_name not in data_dict_lower:
        feature_classes_without_scientific_name.append(feature_class)

# Print the feature classes without corresponding scientific names
if feature_classes_without_scientific_name:
    print("Feature classes without corresponding scientific names:")
    for fc in feature_classes_without_scientific_name:
        print(fc)
else:
    print("All feature classes have corresponding scientific names.")

len(fc)
