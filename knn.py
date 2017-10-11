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

    mnist = read_data_sets("/tmp/data", one_hot=True)
    Xtrain = mnist.train.images
    ytrain = mnist.train.labels

    all_distances = []
    huge_final_list = []

    # k value
    k = 3
    i = 0
    z = 0

    xtrain_ph = tf.placeholder("float", [None, 784])
    xtest_ph = tf.placeholder("float", [784])

#   distance = tf.reduce_sum(tf.abs(tf.add(xtrain_ph, tf.negative(xtest_ph))), axis=1) # a + -b
    # euclidean distance function
    distance = tf.reduce_sum(tf.abs(tf.subtract(xtrain_ph, xtest_ph)), axis=1)  # a - b

    # Prediction: Get min distance index (Nearest neighbor)
    prediction = tf.argmin(distance, 0)

    # Initialize the variables (i.e. assign their default value)
    init = tf.global_variables_initializer()

    # get the x_test labels and store into list
    with tf.Session() as sess:
        sess.run(init)
        for i in range(len(x_test)):
            bigint = sess.run(prediction, feed_dict={xtrain_ph: Xtrain, xtest_ph: x_test[i, :]})
            huge_final_list.append(np.argmax(ytrain[bigint]))
            print("THIS IS huge_final_list")
            print(huge_final_list)

    print("THIS IS huge_final_list")
    print(huge_final_list)

    # return x_test labels in predicted_y_test
    predicted_y_test = huge_final_list
    return predicted_y_test

    '''
     getting 1000 images to test (training set)
    x = [randint(0, ntrain - 1) for p in range(0, 1000)]


    print(range(len(Xtrain)))
    # work within for loop to test samples
    for j in range(len(x_test)):
        i = 0
        for i in range(len(Xtrain)):
            sample = x[i]  # get one sample
             euclidean distance function
             distance = euclideanDistance(x_test[j], Xtrain[i], 784)
             store all distances coupled with their array
            all_distances.append((Xtrain[i], distance))
            if i == 999:
                print(j, i)
                all_distances.sort(key=operator.itemgetter(1))
                distances = get_distances(all_distances, k)
                bigint = most_common(distances)
                huge_final_list.append(bigint)
                print(huge_final_list)
                all_distances = []
                print("Distance:" + repr(distance)) '''


def hyperparameters_search():
    raise NotImplementedError


if __name__ == '__main__':
    hyperparameters_search()
