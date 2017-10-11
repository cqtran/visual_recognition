import math
import tensorflow as tf
import numpy as np
from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets
import timeit
from random import randint
import operator


def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
	    distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)

# add closest neighbours to list
def find_neighbours(list_distances, k):
    closest_neighbours = []
    for i in range(k):
        print(list_distances[i][1])
        closest_neighbours.append(list_distances[i][0])
    return closest_neighbours

def classification(list_of_neighbours):
    return list_of_neighbours[0] # because it is already sorted lowest distance to highest

mnist = read_data_sets("/tmp/data", one_hot=True)
ntrain = mnist.train.num_examples
Xtrain = mnist.train.images
ytrain = mnist.train.labels
print(Xtrain)
print(ntrain, Xtrain.shape, ytrain.shape)

all_distances = []
# k value
k = 5

# getting 1000 images to test (training set)
x = [randint(0,ntrain-1) for p in range(0,999)]

# work within for loop to test samples
for i in range(len(x)):
    sample = x[i]   # get one sample
    fakextest = x[0]    # test array eg first array in training set
    #print(Xtrain[sample])

    # euclidean distance function
    distance = euclideanDistance(Xtrain[fakextest], Xtrain[sample], 784)
    # store all distances coupled with their array
    all_distances.append((Xtrain[sample], distance))
    print("Distance:" + repr(distance))
    # each individual value
    for j in range(784 - 1):
        row = (Xtrain[sample][j])
        #print(row)

i = 0
all_distances.sort(key=operator.itemgetter(1))
closest_neighbours = find_neighbours(all_distances, k)
print(type(closest_neighbours))

final_array = classification(closest_neighbours)





