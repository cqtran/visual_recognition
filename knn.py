import math
import tensorflow as tf
import numpy as np
from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets
import timeit
from random import randint
import operator

def most_common(lst):
    return max(set(lst), key=lst.count)

def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
	    distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)

def get_distances(list_distances, k):
    distances = []
    for i in range(k):
        print(list_distances[i][1])
        distances.append(int(list_distances[i][1]))
    return distances

def run(x_test):


    # TODO: Write your algorithm here
#    raise NotImplementedError

    mnist = read_data_sets("/tmp/data", one_hot=True)
    ntrain = mnist.train.num_examples
    Xtrain = mnist.train.images
    ytrain = mnist.train.labels

    all_distances = []
    huge_final_list = []

    # k value
    k = 3
    i = 0
    z = 0


    # getting 1000 images to test (training set)
    x = [randint(0, ntrain - 1) for p in range(0, 1000)]

    # work within for loop to test samples
    for j in range(len(x_test)):
        i = 0
        for i in range(len(x)):
            sample = x[i]  # get one sample
            # euclidean distance function
            distance = euclideanDistance(x_test[j], Xtrain[sample], 784)
            # store all distances coupled with their array
            all_distances.append((Xtrain[sample], distance))
            if i == 999:
                print(j, i)
                all_distances.sort(key=operator.itemgetter(1))
                distances = get_distances(all_distances, k)
                bigint = most_common(distances)
                huge_final_list.append(bigint)
                print(huge_final_list)
                all_distances = []
                #print("Distance:" + repr(distance))

    print("THIS IS huge_final_list")
    print(huge_final_list)

    predicted_y_test = []
    predicted_y_test = huge_final_list
    return predicted_y_test






def hyperparameters_search():
    raise NotImplementedError


if __name__ == '__main__':
    hyperparameters_search()
