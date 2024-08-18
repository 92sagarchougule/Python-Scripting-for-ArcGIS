#Developer: Sagar Chougule
#Author: Sagar Chougule / sagar4gis@gmail.com 

import arcpy


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "TOOLBOX LABEL NAME IS GIVEN"
        self.alias = "TOOLBOX ALIAS NAME IS GIVEN"

        # List of tool classes associated with this toolbox
        self.tools = [Buffer_pts]


class Buffer_pts(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Tool for Buffer"
        self.description = "TOOL FOR BUFFER"
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        params0 = arcpy.Parameter()
        params0.name = "Parameter0"
        params0.displayName = "Inpur Feature Class"
        params0.parameterType = "Required"
        params0.direction = "Input"
        params0.datatype = "Feature Layer"
        params0.filter.list=[]
        

        params1 = arcpy.Parameter()
        params1.name = "Parameter1"
        params1.displayName = "Inpur Buffer Distance"
        params1.parameterType = "Required"
        params1.direction = "Input"
        params1.datatype = "Long"
        return [params0,params1]
##
##    def isLicensed(self):
##        """Set whether tool is licensed to execute."""
##        return True
##
##    def updateParameters(self, parameters):
##        """Modify the values and properties of parameters before internal
##        validation is performed.  This method is called whenever a parameter
##        has been changed."""
##        return
##
##    def updateMessages(self, parameters):
##        """Modify the messages created by internal validation for each tool
##        parameter.  This method is called after internal validation."""
##        return
##
    def execute(self, parameters, messages):
        """The source code of the tool."""
        inputFc = parameters[0].valueAsText
        buffDist = parameters[1].valueAsText

        messages.addMessage('Inpur Feature Class = ' + inputFc)

        messages.addMessage('Inpur Buffer Distance = ' + buffDist)

        import os

        name = arcpy.Describe(inputFc).basename + "_buf" + buffDist
        path = arcpy.Describe(inputFc).path
        
        outputFc = os.path.join(path,name)

        messages.addMessage("Buffering ..." + inputFc + "By" + buffDist)

        arcpy.Buffer_analysis(inputFc,outputFc,buffDist)
        
        
        return
        

