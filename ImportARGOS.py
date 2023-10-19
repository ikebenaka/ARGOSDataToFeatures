##---------------------------------------------------------------------
## ImportARGOS.py
##
## Description: Read in ARGOS formatted tracking data and create a line
##    feature class from the [filtered] tracking points
##
## Usage: ImportArgos <ARGOS folder> <Output feature class> 
##
## Created: Fall 2023
## Author: igb8@duke.edu (for ENV859)
##---------------------------------------------------------------------

#Import modules
import sys, os, arcpy

#Set input variables (Hard-wired)
inputFile = "V:/ARGOSTracking/Data/ARGOSData/1997dg.txt"
outputFC = "V:/ARGOSTracking/Scratch/ARGOStrack.shp"

#Construct a while loop to iterate through all lines in the datafile
#Open the ARGOS data file for reading
inputFileObj = open(inputFile, "r")

#Get the first line of data, so we can use a while loop
lineString = inputFileObj.readline()

#Start the while loop
while lineString:
    #Set code to only run if the line contains the string "Date:"
    if ("Date: " in lineString):

        #Parse the line into a list
        lineData = lineString.split()

        #Extract attributes from the datum header line
        tagID = lineData[0]
        obsDate = lineData[3]
        obsTime = lineData[4]
        obsLC = lineData[7] #ERROR: list index out of range

        #Extract location info from the next line
        line2String = inputFileObj.readline()

        #Parse the line into a list
        line2Data = line2String.split()

        #Extract the data we need into variables
        obsLat = line2Data[2] #ERROR: list index out of range
        obsLon = line2Data[5]

        #Print results
        print(tagID, "Lat: "+obsLat, "Long: "+obsLon)
    
    #Move to the next line so the while loop progresses
    lineString = inputFileObj.readline()

#Close the file object
inputFileObj.close()