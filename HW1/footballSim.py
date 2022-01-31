""" Caleb Klenda
    CSE 590
    HW #1
    Football Simluator
"""
from dataclasses import field
import numpy as np

#Returns a number in yardrange(inclusive) or a 0 
#with a random chance equal to the successPrct
def down(successPrct, yardRange):
    #range 0-100 random, the high is exclusive
    if np.random.randint(0, 100 + 1) > successPrct:
        return 0
    else:
        #yardrange is inclusive on both ends
        return np.random.randint(yardRange[0], yardRange[1] + 1)

def drive(yardsToTD, successPrct, yardRange):
    pointsScored = 0
    fieldPosition = 0
    downCount = 1
    while (True):
        yardsToTD -= down(successPrct, yardRange)
        downCount += 1
        if yardsToTD <= 0:
            #team scores
            if np.random.randint(0, 100 + 1) < 90:
                pointsScored = 7
            else:
                pointsScored = 6
            fieldPosition = 80
            break
        if downCount >= 4:
            fieldPosition = 100 - yardsToTD
            break

    return(pointsScored, fieldPosition)

def printDown(yardsToTD, currentDown, pointsScored=0):
    fieldString = list("O----|----|----|----|----|----|----|----|----|----X")
    downSuffixList = ["1st Down, ", "2nd Down, ", "3rd Down, ", "4th Down, ", "Turnover, "]

    if yardsToTD <= 0:
        nearestYardMarker = 50
        fieldString[nearestYardMarker] = "T"
        if pointsScored == 7:
            endingPhrase = "Touchdown! PAT good\n"
        else:
            endingPhrase = "Touchdown! PAT missed\n"
    else:
        fieldPosition = 100 - yardsToTD
        nearestYardMarker = int(np.round(fieldPosition/2))
        fieldString[nearestYardMarker] = ">"
        if currentDown > 4:
            endingPhrase = downSuffixList[currentDown-1] + str(yardsToTD) + " Yds short\n"
        else:
            endingPhrase = downSuffixList[currentDown-1] + str(yardsToTD) + " Yds to Go"
        
    print("".join(fieldString), ";", endingPhrase)

#this function is identical to drive, except that it calls the printDown
#to print out the results of each down
def drive_depicted(yardsToTD, successPrct, yardRange):
    pointsScored = 0
    fieldPosition = 0
    downCount = 1
    while (True):
        printDown(yardsToTD, downCount)
        yardsToTD -= down(successPrct, yardRange)
        downCount += 1
        if yardsToTD <= 0:
            #team scores
            if np.random.randint(0, 100 + 1) < 90:
                pointsScored = 7
            else:
                pointsScored = 6
            fieldPosition = 80
            printDown(yardsToTD, downCount, pointsScored)
            break
        if downCount > 4:
            fieldPosition = 100 - yardsToTD
            printDown(yardsToTD, downCount)
            break

    return(pointsScored, fieldPosition)

def simulategame(numDrives, prctT1, yrangeT1, prctT2, yrangeT2, driveFunction=drive):
    t1Score = 0
    t2Score = 0
    PointsScored = 0
    FieldPosition = 1
    yardsToTD = 80

    for i in range(0, numDrives):
        if i % 2 == 0:
            driveResult = driveFunction(yardsToTD, prctT1, yrangeT1)
            t1Score += driveResult[PointsScored]
        else:
            driveResult = driveFunction(yardsToTD, prctT2, yrangeT2)
            t2Score += driveResult[PointsScored]
        yardsToTD = driveResult[FieldPosition]

    return(t1Score , t2Score)
