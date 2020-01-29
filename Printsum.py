##    3D Print Time Aggregator
##    Purpose: Get and sum the estimated print times for printed parts
##    in a directory so that we know the total print time
##
##    Shane Frost
##    27 Jan 2020
##    
##    Todo
##    Add support for other slicers
##    Output to SQL table
##    Output to MQTT
##    Octoprint add-in?

# Import Modules
import os
import re

# Variables
locationName = []
totalFiles = []
totalPrintTime = []
filamentLength = []
plasticVolume = []
plasticWeight = []
materialCost = []
location = 0

def getPrintTimeSimplify(tString):
    hours = int(tString[:tString.find(' ')].strip()) * 60
    minutes = int(re.sub('[^0-9 ]+', '', tString[tString.find('hours ') + 6:]).strip())
    return hours + minutes

def getFilamentLengthSimplify(tString):
    filamentLen = float(tString[:tString.find(' ')].strip())
##    print(str(filamentLen))
    return filamentLen

def getFilamentLengthSimplify(tString):
    filamentLen = float(tString[:tString.find(' ')].strip())
##    print(str(filamentLen))
    return filamentLen

       
# Read the config file
config = 'config.txt'
with open(config) as fp:
    line = fp.readline()
    while line:
        totalPrintTime.append(location)
        locationName.append(location)
        totalFiles.append(location)
        filamentLength.append(location)
        plasticVolume.append(location)
        plasticWeight.append(location)
        materialCost.append(location)

        locationName[location] = line
        totalFiles[location] = 0
        filamentLength[location] = 0
        plasticVolume[location] = 0
        plasticWeight[location] = 0
        materialCost[location] = 0

        dirPath = line.replace('\n','')

        for filename in os.listdir(dirPath):
            if dirPath != "":
                print(filename)

                if filename.endswith(".gcode"): 
                    f=open(os.path.join(dirPath, filename), "r")
                    contents =f.read()
                    temp = contents[contents.find('Build time:') + 12:contents.find('Build time:') + 50]
                    print(getPrintTimeSimplify(temp[:temp.find(';')].strip()))
                    f.close()
                    totalPrintTime[location] = totalPrintTime[location] + getPrintTimeSimplify(temp[:temp.find(';')].strip())
                    totalFiles[location] = totalFiles[location] + 1
                    filamentLength[location] = filamentLength[location] + getFilamentLengthSimplify(contents[contents.find('Filament length: ') + 17:contents.find('Filament length: ') + 50])
                    plasticVolume[location] = 0
                    plasticWeight[location] = 0
                    materialCost[location] = 0                    
                    continue
                else:
                    continue



        line = fp.readline()
        print(totalPrintTime[location])
        location = location + 1


for x in range(len(locationName)):
    print(x)
    print(locationName[x].strip())
    print(totalPrintTime[x])
    print(totalFiles[x])
    print(filamentLength[x])








