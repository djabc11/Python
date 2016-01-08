
from __future__ import division

import sys
#print(sys.path)


import numpy as np
from statsmodels import api as sm

from math import radians, cos, sin, asin, sqrt

import csv



"""
y = [1,2,3,4,3,4,5,4,5,5,4,5,4,5,4,5,6,5,4,5,4,3,4]

x = [
     [4,2,3,4,5,4,5,6,7,4,8,9,8,8,6,6,5,5,5,5,5,5,5],
     [4,1,2,3,4,5,6,7,5,8,7,8,7,8,7,8,7,7,7,7,7,6,5],
     [4,1,2,5,6,7,8,9,7,8,7,8,7,7,7,7,7,7,6,6,4,4,4]
     ]
"""

y = []
x = [ [] ]



"""
for line in open('Liberty Mutual/TrainingFeatures.csv'):
    line = line.split(',')
    itemCount = 0
    CTotal = 0
    for item in line:
        if itemCount == 0:
            y.append(float(item))
        else:
            if itemCount == 4:
                CTotal = CTotal + float(item)*2.4242
            if itemCount == 5:
                CTotal = CTotal + float(item)*3.86
            if itemCount == 6:
                CTotal = CTotal + float(item)*2.9056
            if itemCount < 4:
                x[itemCount-1].append(float(item.replace("\n",'')))
            if itemCount == 7:
                x[3].append(float(item.replace("\n",'')))
        itemCount = itemCount + 1
    #x[4].append(CTotal)
    """

"""
for line in open('Liberty Mutual/TrainingFeaturesPt2.csv'):
    line = line.split(',')
    itemCount = 0
    for item in line:
        if itemCount == 0:
            y.append(float(item))
        else:
            if itemCount == 6:
                x[0].append(float(item.replace("\n",'')))
        itemCount = itemCount + 1
    #x[4].append(CTotal)



#print(x)




def regm(y, x):
    ones = np.ones(len(x[0]))
    X = sm.add_constant(np.column_stack((x[0], ones)))
    for ele in x[1:]:
        X = sm.add_constant(np.column_stack((ele, X)))
    results = sm.OLS(y, X).fit()
    return results

blah = regm(y, x).summary()

print(blah)

"""

def calculateWRW(origin,destination,weight):
    return haversine(origin[0],origin[1],destination[0],destination[1])*weight

def calculateWRWTrip(destinations):
    tripWRW = 0;
    destinationsCopy = destinations.copy();
    for i in range(0,len(destinationsCopy) - 1):
        origin = destinationsCopy[0]
        destination = destinationsCopy[1]
        #print(origin)
        #print(destination)
        
        giftWRW = calculateWRW([origin[1],origin[2]],[destination[1],destination[2]],currentSleightWeight(destinationsCopy))
        print(giftWRW)
        #print(giftWRW)
        tripWRW = tripWRW + giftWRW
        del destinationsCopy[0]
    return tripWRW

def currentSleightWeight(destinations):
    
    totalWeight = 10;
    """destinationsToListPre = np.array(destinations)
    print("blah")
    destinationsToList = destinationsToListPre.ravel()
    print("blah 2")
    destinationsToList = destinationsToList[3:]
    print("blah 3")
    destinationsToCount = [float(i) for i in destinationsToList[::5]]
    print("blah 4")
    return sum(destinationsToCount)
    """
    for i in destinations:
        totalWeight = totalWeight + i[3]
    return totalWeight

def haversine(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r

def findNextDestination(destinations,withWeight):
    origin = destinations[0]
    if (withWeight == 0):
        totalWeight = 100
    else:
        totalWeight = currentSleightWeight(destinations)
    minValue = 1000000000000
    minID = 0
    maxRange = len(destinations) - 1

    if (len(destinations) > 400):
        maxRange = 300 #list is sorted by latitude. chances are next closest one will be among the next 10000
    for i in range(1,maxRange):
        destination= destinations[i]
        destinationWeight = destination[3]
        thisValue = haversine(origin[1],origin[2],destination[1],destination[2])*(totalWeight-destinationWeight)

        #print(destination[0])
        #print("is")
        #print(haversine(origin[1],origin[2],destination[1],destination[2]))
        #print(totalWeight-destinationWeight)

        if (thisValue < minValue):
            minValue = thisValue
            minID = destination[0]
    if (len(destinations) % 100 == 0):
        print(len(destinations))
    return minID    


def sortDestinations(destinations,withWeight):
    remainingDestinations = destinations.copy()
    sortedDestinations = [[]]
    sortedDestinations.append(remainingDestinations[0]) 
    del sortedDestinations[0]
    for j in range(0,len(remainingDestinations)-1):
        nextOne = findNextDestination(remainingDestinations,withWeight)
        #print(remainingDestinations)
        #print(nextOne)
        indexOfNextOne = -1
        maxRange = len(remainingDestinations) 
        if (len(remainingDestinations) > 400):
            maxRange = 300
        for i in range(0,maxRange):
            
            if (remainingDestinations[i][0] == nextOne):
                sortedDestinations.append(remainingDestinations[i])
                indexOfNextOne = i
        del remainingDestinations[0]
        remainingDestinations.insert(0,remainingDestinations[indexOfNextOne-1])
        del remainingDestinations[indexOfNextOne]
        #del index 0
        #move value to index 0

        

    #print(sortedDestinations)    
    #print(calculateWRWTrip(sortedDestinations))
    destinations = sortedDestinations
    #return calculateWRWTrip(sortedDestinations)
    return sortedDestinations
    """
    take origin
    iterate through options (ignoring last one which is final destination). for each one, take haversine*(totalWeight-weight)
    """

"""
print(haversine(90,0,100,10))
print(calculateWRW([90,0],[100,10],1))
"""

def clusterIntoHalf(destinations):
    #create box from all points
    xMin = 1000
    xMax = -1000
    yMin = 1000
    yMax = -1000

    destinationsX = [[]]
    destinationsY = [[]]

    del destinationsX[0]
    del destinationsY[0]

    for (i in destinations):
        currentLat = i[1]
        currentLon = i[2]

        

        #put into array ordered by X:
        #look at current array. find middle value. if this one has X greater, examine top. else bottom. rinse and repeat

        a = len(destinationsX)
        minRange = 0
        maxRange = a-1
        success = 0

        #a few conditions to watch out for:

        if (a == 0): #empty array, insert first record
            destinationsX.insert(maxRange,i)
            success = 1

        #if less than min, insert in place 0
        minArrayValue = destinationsX[0]
        minLonValue = middleArrayValue[2]
        if (currentLon < minLonValue):
            destinationsX.insert(0,i)
            success = 1

        #if greater than max, append
        maxArrayValue = destinationsX[maxRange]
        maxLonValue = maxArrayValue[2]
        if (currentLon > maxLonValue):
            destinationsX.append(i)
            success = 1


        while (success == 0):
            if (maxRange - minRange == 1):
                destinationsX.insert(maxRange,i) #insert destination at index of maxRange
                success = 1 #whoo!
            else:
                middleIndex = (maxRange+minrange)/2
                middleArrayValue = destinationsX[middleIndex]
                middleLonValue = middleArrayValue[2]
                if (currentLon >= middleLonValue):
                    minRange = middleIndex
                else:
                    maxRange = middleIndex
            


        #put into array ordered by Y
        if (currentLat < yMin):
            yMin = currentLat
        if (currentLat > yMax):
            yMax = currentLat
        if (currentLon < xMin):
            xMin = currentLon
        if (currentLon > xMax):
            xMax = currentLon
    if ((yMax - yMin) > (xMax - xMin)):
        #cut on Y axis

    else:
        #cut on X axis

giftArray = [[0,90,0,0]]
"""giftArray.append([77,24.2,76.12,50])
giftArray.append([118,39.67,51.77,50])"""
giftArray.append([30289,22.83434666, 10.56579953, 27.85789274])
giftArray.append([43215,-0.911304709,    -73.38876968,    40.58210748])
giftArray.append([156,-15.85388938,    144.6591108, 19.27233967])
giftArray.append([5262,-38.13857064,    144.6125446, 50])
giftArray.append([43405,   59.1551338,  92.94181219, 1])
giftArray.append([83942,  -36.12365791,    -71.62390397,    22.19687077])
giftArray.append([55569, 40.15935797, 49.96537485, 50])
giftArray.append([51598,   -10.88303387,    -54.64391561,    20.51669253])
giftArray.append([51026,   -77.18600036,    71.40373991, 9.321197229])
giftArray.append([55912, 26.04471517, 3.130887811, 22.78740482])

giftArray.append([0,90,0,0])

"""
print(calculateWRWTrip(giftArray))
print(currentSleightWeight(giftArray))
"""



giftArray2 = [[0,90,0,0,-1]]



for line in open('gifts.csv'):
    lineSplit = line.split(',')
    lineSplit[0] = float(lineSplit[0])
    lineSplit[1] = float(lineSplit[1])
    lineSplit[2] = float(lineSplit[2])
    lineSplit[3] = float(lineSplit[3])
    giftArray2.append(lineSplit)


del giftArray2[0] #remove dummy     
#print(len(giftArray2))

masterGiftArray = giftArray2.copy()
masterGiftArraySorted = [[0,0]]




#masterGiftArray10000 = masterGiftArray[0:10000];
#masterGiftArray10000.append([0,90,0,0,-1])

#masterGiftArray10000 = sortDestinations(masterGiftArray10000)

masterGiftArray.append([0,90,0,0,-1])
masterGiftArray = sortDestinations(masterGiftArray,0) #if all of them were in one trip- this is a close to optimal path


finalWRW = 0
initialTripSize = 50
for i in range(0,len(masterGiftArray)//initialTripSize):
    
    tempArray = masterGiftArray[i*initialTripSize:(i+1)*initialTripSize]
    tempArray.insert(0,[0,90,0,0,-1])
    tempArray.append([0,90,0,0,-1])
    #print(sortDestinations(tempArray))
    tempArray = sortDestinations(tempArray,1)
    finalWRW = finalWRW + calculateWRWTrip(tempArray)
    print(calculateWRWTrip(tempArray))
    print(currentSleightWeight(tempArray))
    print(tempArray)
    for j in tempArray:
        if(j[0] != 0):
            
            masterGiftArraySorted.append([int(j[0]),i+1])

del masterGiftArraySorted[0]

print(finalWRW)



#print(masterGiftArraySorted)
#loop for every 20
#sort
#put into master array



with open("output2.csv", "w") as f:
    writer = csv.writer(f)
    for i in masterGiftArraySorted:
        writer.writerow(i)

"""
with open("output.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(masterGiftArraySorted)
"""




