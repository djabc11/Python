
import sys
print(sys.path)


import numpy as np
from statsmodels import api as sm

from math import radians, cos, sin, asin, sqrt

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
        
        #print(giftWRW)
        tripWRW = tripWRW + giftWRW
        del destinationsCopy[0]
    return tripWRW

def currentSleightWeight(destinations):
    totalWeight = 10;
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

def findNextDestination(destinations):
    origin = destinations[0]
    totalWeight = currentSleightWeight(destinations)
    minValue = 1000000000
    minID = 0
    for i in range(1,len(destinations) - 1):
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

 
    return minID    


def sortDestinations(destinations):
    remainingDestinations = destinations.copy()
    sortedDestinations = [[]]
    sortedDestinations.append(remainingDestinations[0]) 
    del sortedDestinations[0]
    for j in range(0,len(remainingDestinations)-1):
        nextOne = findNextDestination(remainingDestinations)
        #print(remainingDestinations)
        #print(nextOne)
        indexOfNextOne = -1
        for i in range(0,len(remainingDestinations)):
            
            if (remainingDestinations[i][0] == nextOne):
                sortedDestinations.append(remainingDestinations[i])
                indexOfNextOne = i
        del remainingDestinations[0]
        remainingDestinations.insert(0,remainingDestinations[indexOfNextOne-1])
        del remainingDestinations[indexOfNextOne]
        #del index 0
        #move value to index 0

        

    #print(sortedDestinations)    
    print(calculateWRWTrip(sortedDestinations))
    """
    take origin
    iterate through options (ignoring last one which is final destination). for each one, take haversine*(totalWeight-weight)
    """

"""
print(haversine(90,0,100,10))
print(calculateWRW([90,0],[100,10],1))
"""

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
print(calculateWRWTrip(giftArray))
print("how about now")
print(sortDestinations(giftArray))


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

giftArray3 = giftArray2.copy()
del giftArray3[20:len(giftArray3)]
giftArray3.append([0,90,0,0])
#print(len(giftArray3))

print(giftArray3)
print(calculateWRWTrip(giftArray3))
print("how about now")
print(sortDestinations(giftArray3))



