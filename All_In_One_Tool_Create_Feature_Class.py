#Author: Sagar Chougule / sagar4gis@gmail.com 


import arcpy
>>> import arcpy
... arcpy.env.addOutputsToMap = True
... 
... 
... class Toolbox(object):
...     def __init__(self):
...         """Define the toolbox (the name of the toolbox is the name of the
...         .pyt file)."""
...         self.label = "Toolbox"
...         self.alias = ""
... 
...         # List of tool classes associated with this toolbox
...         self.tools = [Tool]
... 
... 
... class Tool(object):
...     def __init__(self):
...         """Define the tool (tool name is the name of the class)."""
...         self.label = "Create Feature Class"
...         self.description = "Tool for Create database"
...         self.canRunInBackground = False
... 
...     def getParameterInfo(self):
...         """Define parameter definitions"""
...     #Parameter 0st for Database type selection
...         params0 = arcpy.Parameter()
...         params0.datatype = "String"
...         params0.direction = "Input"
...         params0.type = "Required"
...         params0.name = "Type of Database"
...         params0.displayName = "Select Type of Database"
...         params0.filter.type = "ValueList"  #'Value List'
...         params0.filter.list = ['PERSONAL DATABASE','FILE DATABASE'] #[2,5,87]
... 
...     #Parameter 1nd for workspace of database
...         params1 = arcpy.Parameter()
...         params1.datatype = "workspace"
...         params1.direction = "Input"
...         params1.type = "Required"
...         params1.name = "typedb"
...         params1.displayName = "Select Workspace"
...         
...         
...     #Parameter 2nd for Name of database
...         params2 = arcpy.Parameter()
...         params2.datatype = "String"
...         params2.direction = "Input"
...         params2.type = "Required"
...         params2.name = "nameofdatabase"
...         params2.displayName = "Name of Database"
...         
...     #Parameter 3rd for Name of Datafeatureset
...         params3 = arcpy.Parameter()
...         params3.datatype = "String"
...         params3.direction = "Input"
...         params3.type = "Required"
...         params3.name = "nameof_FC_dataset"
...         params3.displayName = "Name of Feature dataset"
... 
...         params4 = arcpy.Parameter()
...         params4.datatype = "Coordinate System"
...         params4.direction = "Input"
...         params4.type = "Required"
...         params4.name = "nameof_SR"
...         params4.displayName = "Choose Coordinate System"
...         
...         
...     #Parameter 4th for Type of Feature Class
...         params5 = arcpy.Parameter()
...         params5.datatype = "String"
...         params5.direction = "Input"
...         params5.type = "Required"
...         params5.name = "nameofdataset"
...         params5.displayName = "Select Feature Class"
...         params5.filter.type = "ValueList"  #'Value List'
...         params5.filter.list = ['POINT','POLYLINE','POLYGON']
... 
...         
...         
... 
...     #Parameter 4th for Name of Feature Class
...         params6 = arcpy.Parameter()
...         params6.datatype = "String"
...         params6.direction = "Input"
...         params6.type = "Required"
...         params6.name = "nameof_FC"
...         params6.displayName = "Add Name of Feature Class"
...     #params2.enabled = False
... 
...         
...         
... 
...         
...         return [params0, params1, params2, params3, params4, params5,params6]
... 
...     def isLicensed(self):
...         """Set whether tool is licensed to execute."""
...         return True
... 
...     def updateParameters(self, parameters):
...         """Modify the values and properties of parameters before internal
...         validation is performed.  This method is called whenever a parameter
...         has been changed."""
...         return
... 
...     def updateMessages(self, parameters):
...         """Modify the messages created by internal validation for each tool
...         parameter.  This method is called after internal validation."""
...         return
... 
...     def execute(self, parameters, messages):
...         """The source code of the tool."""
...         typDatabase = parameters[0].valueAsText #To select Type of Database
...         
...         dworkspace = parameters[1].valueAsText   #To select Workspace for Database
...         dbase = parameters[2].valueAsText    # To select Name of Database
...         fDbname = parameters[3].valueAsText  #Name of Feature Dataset
...         cooRdi = parameters[4].valueAsText   #Type of Coordiante
...         fcType = parameters[5].valueAsText    #Select Type of Feature Class
...         fcName = parameters[6].valueAsText    #Name OF Feature Class
...             
...         
... 
...         #sr = arcpy.SpatialReference(cooRdi)
...         #coords = sr.factoryCode
...         messages.addMessage('\nType of Coordinate = ' + cooRdi)
...         messages.addMessage('\nSelected Type of Database = ' + typDatabase)
...         messages.addMessage('\nSelected Workspace = ' + dworkspace)
...         messages.addMessage('\nName of Database = ' + dbase)
...         messages.addMessage('\nName of Feature Dataset = ' + fDbname)
...         messages.addMessage('\nSelected Type of Feature Class = ' + fcType)
...         messages.addMessage('\nName of Feature Class = ' + fcName)
... 
...         
... 
...         
...         if(parameters[0].value == "PERSONAL DATABASE"):
...             pDb = arcpy.CreatePersonalGDB_management(dworkspace,dbase)
...             messages.addMessage('\nDatabase created')
...             fdSet = arcpy.CreateFeatureDataset_management(pDb,fDbname,cooRdi)
...             messages.addMessage('\nFeature Dataset Created')
...             
... 
...             
... 
...             
...         if(parameters[0].value == "FILE DATABASE"):
...             pDb = arcpy.CreateFileGDB_management(dworkspace,dbase)
...             messages.addMessage('\nDatabase created')
...             fdSet = arcpy.CreateFeatureDataset_management(pDb,fDbname,cooRdi)
...             messages.addMessage('\nFeature Dataset Created')
... 
... 
...         if(fcType=='POINT'):
...             arcpy.CreateFeatureclass_management(fdSet,fcName,"POINT")
...             messages.addMessage('\nPoint Feature Class Created')
...         if(fcType=='POLYGON'):
...             arcpy.CreateFeatureclass_management(fdSet,fcName,"POLYGON")
...             messages.addMessage('\nPolygon Feature Class Created')
...         if(fcType=='POLYLINE'):
...             arcpy.CreateFeatureclass_management(fdSet,fcName,"POLYLINE")
...             messages.addMessage('\nLine Feature Class Created')
... 
...             #parameters[1].filter.list=["UTM43","UTM44"]
... 
...         return
...     
...         
...         
... 
... ##        messages.addMessage('Workspace = ' + workspace)
... ##
... ##        messages.addMessage('Database Name = ' + dBname)
... ##        
... ##        arcpy.CreatePersonalGDB_management(workspace,dBname)
...         
