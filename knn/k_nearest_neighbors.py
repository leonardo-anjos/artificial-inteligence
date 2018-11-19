
# coding: utf-8

# ## K-Nearest Neighbors
# 
# Solving problem classification on knn algorithm from iris dataset

# In[1]:


# @autor leonardo-anjos
# @see https://towardsdatascience.com/k-nearest-neighbours-introduction-to-machine-learning-algorithms-18e7ce3d802a


# In[7]:


# import libs
import csv
import random
import math
import operator
# import matplotlib.pyplot as plt
# get_ipython().magic(u'matplotlib inline')

def unsupervised_learn():
    print('this is some more test')

# handler data
def load_data(filename, split, set_training = [] , set_test = []):
    with open(filename, 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        for x in range(len(dataset)-1):
            for y in range(4):
                dataset[x][y] = float(dataset[x][y])
            if random.random() < split:
                set_training.append(dataset[x])
            else:
                set_test.append(dataset[x])

# training_set=[]
# test_set=[]
# load_data('./data/iris.data', 0.66, training_set, test_set)

# print('Train: ' + repr(len(training_set)))
# print('Test: ' + repr(len(test_set)))

#some visualization of data
# def plot(data):
#     for i in range(len(data)):
#         if data[i][4] =='setosa':
#             plt.plot(data[i, :1], data[i,1:2],'go')
#         if data[i][4] =='versicolor':
#             plt.plot(data[i, :1], data[i,1:2],'bo')
#         if data[i][4] =='virginica':
#             plt.plot(data[i, :1], data[i,1:2],'ro') 
#         plt.xlabel('Sepal-length')
#         plt.ylabel('Sepal-width')
# plot(data)

# similarity
def euclidean_distance(data1, data2, length):
    distance = 0
    for x in range(length):
        distance += pow((data1[x] - data2[x]), 2)
    return math.sqrt(distance)

# data1 = [2, 2, 2, 'a']
# data2 = [4, 4, 4, 'b']
# distance = euclidian_distance(data1, data2, 3)
# print('Distance: ' + repr(distance))

# neighbors
def get_neighbors(set_training, test_instance, k):
    distances = []
    length = len(test_instance) - 1
    
    for x in range(len(set_training)):
        dist = euclidean_distance(test_instance, set_training[x], length)
        distances.append((set_training[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    
    for x in range(k):
        neighbors.append(distances[x][0])
    return neighbors

# train_set = [[2, 2, 2, 'a'], [4, 4, 4, 'b']]
# test_instance = [5, 5, 5]
# k = 1
# neighbors = get_neighbors(train_set, test_instance, 1)
# print(neighbors)

# response
def get_response(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.items(), key = operator.itemgetter(1), reverse = True)
    return sortedVotes[0][0]

# neighbors = [[1,1,1,'a'], [2,2,2,'a'], [3,3,3,'b']]
# response = get_response(neighbors)
# print('Response: ' + response)

# accuracy of predictions
def get_accuracy(set_test, predictions):
    correct = 0
    for x in range(len(set_test)):
        if set_test[x][-1] == predictions[x]:
            correct += 1
    return (correct/float(len(set_test))) * 100.0

# test_set = [[1,1,1,'a'], [2,2,2,'a'], [3,3,3,'b']]
# predictions = ['a', 'a', 'a']
# accuracy = get_accuracy(test_set, predictions)
# print(accuracy)

# main
def main():
    # prepare data
    set_training = []
    set_test = []
    split = 0.67
    load_data('./data/iris.data', split, set_training, set_test)
    print('train set: ' + repr(len(set_training)))
    print('test set: ' + repr(len(set_test)))
    
    # generate predictions
    predictions=[]
    k = 3
    for x in range(len(set_test)):
        neighbors = get_neighbors(set_training, set_test[x], k)
        result = get_response(neighbors)
        predictions.append(result)
        print('> predicted=' + repr(result) + ', actual=' + repr(set_test[x][-1]))
    accuracy = get_accuracy(set_test, predictions)
    print('Accuracy: ' + repr(accuracy) + '%')

main()

