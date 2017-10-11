import math
import tensorflow as tf
import numpy as np
from tensorflow.contrib.learn.python.learn.datasets.mnist import read_data_sets
import timeit
from random import randint
import operator


a = []
b = list(range(1000))
for j in range(1000):
    for i in range(1000):
        if i == 999:
            a.append(1)
        continue


print(len(a))
print(len(b))