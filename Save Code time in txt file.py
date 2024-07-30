#GetCount.py
#Purpose: To store tool execution time and date
#Input: txt file.
#Example input: "c:/temp.txt/"
#Output: Time and Date in txt file.
#Author: Sagar Chougule / sagar4gis@gmail.com / 08/12/2021

#import os and arcpy module
import os, arcpy
    
    
#example tool 
arcpy.Buffer_analysis("Vally Margin",'buffers','10 Meters')


#open text file
logfile = open(r'D:\T-Temp\Outs.txt','w')

#for loop 
for i in range(0,arcpy.GetMessageCount()):
    logfile.write(arcpy.GetMessage(i)+'\n\n')

#close txt file
logfile.close()

