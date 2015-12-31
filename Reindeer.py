
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
    for i in range(0,len(destinations) - 1):
        origin = destinations[0]
        destination = destinations[1]
        giftWRW = calculateWRW([origin[1],origin[2]],[destination[1],destination[2]],currentSleightWeight(destinations))
        tripWRW = tripWRW + giftWRW
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


print(haversine(90,0,100,10))
print(calculateWRW([90,0],[100,10],1))

giftArray = [[77,24.2,76.12,50]]
giftArray.append([118,39.67,51.77,50])


print(calculateWRWTrip(giftArray))
print(currentSleightWeight(giftArray))


