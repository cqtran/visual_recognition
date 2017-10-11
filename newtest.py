import math
import tensorflow as tf
import numpy as np
from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets
import timeit
from random import randint
import operator


def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)-1
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors

def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
	    distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)


def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        print("This is the response")
        print(response)
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]


trainSet = [[2, 2, 2, 'a'], [4, 4, 4, 'b'],[5,5,5,'c'],[6,6,6,'f']]
testInstance = [5, 5, 5]
k = 3
neighbors = getNeighbors(trainSet, testInstance, k)
print(neighbors)


#neighbors = [[1,1,1,'a'], [2,2,2,'a'], [3,3,3,'b']]
response = getResponse(neighbors)
print(response)



 for j in range(100): #range(len(x_test)):
        i = 0
        print("this j")
        print(j)

        for i in range(len(x_test - 1)):
         #   sample = x[i]  # get one sample
            # euclidean distance function
            if j == z:
                if z == 9:
                    print("Fuck you mean")
                    all_distances.append((x_test[i], 1))

                else:
                    print("hi")
                    print(i)
                    print(j)

                    z = z + 1
                    distance = euclideanDistance(x_test[j], x_test[z], 784)
                    all_distances.append((x_test[z], distance))

            else:
                print("yes")
                distance = euclideanDistance(x_test[j], x_test[z], 784)
                all_distances.append((x_test[z], distance))
                z = z + 1
#            distance = euclideanDistance(x_test[j], Xtrain[sample], 784)
            # store all distances coupled with their array
 #           all_distances.append((Xtrain[sample], distance))
            if i == 99:
                print(j, i)
                all_distances.sort(key=operator.itemgetter(1))
                distances = get_distances(all_distances, k)
                bigint = most_common(distances)
                huge_final_list.append(bigint)
                print(huge_final_list)
                all_distances = []
                #print("Distance:" + repr(distance))
                z = 0