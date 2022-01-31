""" Caleb Klenda
    CSE 590
    HW #1
    Football Simluator
"""
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

#simulates a single drive, with 4 downs to gain at least 10 yards or
#score, turning over otherwise.
#returns the points scored and field position of other team as tuple 
def drive(yardsToTD, successPrct, yardRange):
    pointsScored = 0
    fieldPosition = 0
    downCount = 1
    yardsToFirst = 10

    while (True):
        #run the down, calculate yards
        yardsGained = down(successPrct, yardRange)
        yardsToTD -= yardsGained
        yardsToFirst -= yardsGained

        #first down gained
        if yardsToFirst <= 0:
            downCount = 1
            yardsToFirst = 10
        else:
            downCount += 1

        #team score
        if yardsToTD <= 0:
            #PAT 
            if np.random.randint(0, 100 + 1) < 90:
                pointsScored = 7
            else:
                pointsScored = 6
            fieldPosition = 80
            break

        #turnover
        if downCount >= 4:
            fieldPosition = 100 - yardsToTD
            break

    return(pointsScored, fieldPosition)

#helper function for printing the results of a single down
#takes yards to gain, currentDown, and optionally points
#prints out ascii art field to console showing progress
def printDown(yardsToTD, currentDown, pointsScored=0):
    fieldString = list("O----|----|----|----|----|----|----|----|----|----X")
    downSuffixList = ["1st Down, ", "2nd Down, ", "3rd Down, ", "4th Down, ", "Turnover, "]

    #TD was scored
    if yardsToTD <= 0:
        nearestYardMarker = 50
        fieldString[nearestYardMarker] = "T"
        if pointsScored == 7:
            endingPhrase = "Touchdown! PAT good\n"
        else:
            endingPhrase = "Touchdown! PAT missed\n"

    #No score
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
    yardsToFirst = 10

    while (True):
        printDown(yardsToTD, downCount)
        yardsGained = down(successPrct, yardRange)
        yardsToTD -= yardsGained
        yardsToFirst -= yardsGained

        if yardsToFirst <= 0:
            downCount = 1
            yardsToFirst = 10
        else:
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

#Simulates game by alternating calls to the drive function for two teams, and summing
#the scores based on the resutl. Optional parameter to include visuals or no visuals
def simulategame(numDrives, prctT1, yrangeT1, prctT2, yrangeT2, driveFunction=drive):
    t1Score = 0
    t2Score = 0
    PointsScored = 0
    FieldPosition = 1
    yardsToTD = 80

    #each team gets a drive, so run twice that many dives total 
    for i in range(0, numDrives*2):
        if i % 2 == 0:
            driveResult = driveFunction(yardsToTD, prctT1, yrangeT1)
            t1Score += driveResult[PointsScored]
        else:
            driveResult = driveFunction(yardsToTD, prctT2, yrangeT2)
            t2Score += driveResult[PointsScored]
        yardsToTD = driveResult[FieldPosition]

    return(t1Score , t2Score)
