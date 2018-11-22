# import libs
import csv
import random
import math
random.seed(123)

# load data and set to train
with open('./data/iris.csv') as csvfile:
    load_data = csv.reader(csvfile)
    next(load_data, None) # skip header
    dataset = list(load_data)

# change string value to numeric
for row in dataset:
    row[4] = ["Iris-setosa", "Iris-versicolor", "Iris-virginica"].index(row[4])
    row[:4] = [float(row[j]) for j in range(len(row))]

# split x and y
random.shuffle(dataset)
datatrain = dataset[:int(len(dataset) * 0.8)]
datatest = dataset[int(len(dataset) * 0.8):]
train_X = [data[:4] for data in datatrain]
train_y = [data[4] for data in datatrain]
test_X = [data[:4] for data in datatest]
test_y = [data[4] for data in datatest]

"""
    - one hidden layer
    - 4 neurons input that represult_1ents the featuresult_1 of iris
    - 3 neurons hidden layer that active using sigmoid
    - 3 nuron output layer that represult_1ents the class of iris 
"""
# build mlp model and train

"""
    - optimizer = gradient descent
    - loss function = square root error
    - learning rate = 0.005
    - epoch = 400
    - best result_1ult = 96.67%
"""

# matrix multiplication
def matrix_mul_bias(A, B, bias): 
    C = [[0 for i in range(len(B[0]))] for i in range(len(A))]    
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
            C[i][j] += bias[j]
    return C

 # vector (A) x matrix (B) multiplication
def vectorA_mul_matrixBias(A, B, bias):
    C = [0 for i in range(len(B[0]))]
    for j in range(len(B[0])):
        for k in range(len(B)):
            C[j] += A[k] * B[k][j]
            C[j] += bias[j]
    return C

# matrix (A) x vector (B) multipilicatoin
def matrix_mul_vector(A, B): 
    C = [0 for i in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B)):
            C[i] += A[i][j] * B[j]
    return C

def sigmoid(A, deriv=False):
    if deriv: # derivation of sigmoid
        for i in range(len(A)):
            A[i] = A[i] * (1 - A[i])
    else:
        for i in range(len(A)):
            A[i] = 1 / (1 + math.exp(-A[i]))
    return A

# set parameter
alfa = 0.005
epoch = 400
neuron = [4, 4, 3] # number of neuron each layer

# set weight and bias with 0 value
weight = [[0 for j in range(neuron[1])] for i in range(neuron[0])]
weight_2 = [[0 for j in range(neuron[2])] for i in range(neuron[1])]
bias = [0 for i in range(neuron[1])]
bias_2 = [0 for i in range(neuron[2])]

# set weight with random between -1.0 ... 1.0
for i in range(neuron[0]):
    for j in range(neuron[1]):
        weight[i][j] = 2 * random.random() - 1

for i in range(neuron[1]):
    for j in range(neuron[2]):
        weight_2[i][j] = 2 * random.random() - 1

for e in range(epoch):
    cost_total = 0
    for idx, x in enumerate(train_X):
        # forward propagation
        h_1 = vectorA_mul_matrixBias(x, weight, bias)
        X_1 = sigmoid(h_1)
        h_2 = vectorA_mul_matrixBias(X_1, weight_2, bias_2)
        X_2 = sigmoid(h_2)
        
        # convert to one-hot target
        target = [0, 0, 0]
        target[int(train_y[idx])] = 1

        error = 0
        for i in range(3):
            error +=  0.5 * (target[i] - X_2[i]) ** 2 
        cost_total += error

        # backward propagation
        # update weight_2 and bias_2 (layer 2)
        delta_2 = []
        for j in range(neuron[2]):
            delta_2.append(-1 * (target[j]-X_2[j]) * X_2[j] * (1-X_2[j]))

        for i in range(neuron[1]):
            for j in range(neuron[2]):
                weight_2[i][j] -= alfa * (delta_2[j] * X_1[i])
                bias_2[j] -= alfa * delta_2[j]
        
        # update weight and bias (layer 1)
        delta_1 = matrix_mul_vector(weight_2, delta_2)
        for j in range(neuron[1]):
            delta_1[j] = delta_1[j] * (X_1[j] * (1-X_1[j]))
        
        for i in range(neuron[0]):
            for j in range(neuron[1]):
                weight[i][j] -=  alfa * (delta_1[j] * x[i])
                bias[j] -= alfa * delta_1[j]

    cost_total /= len(train_X)
    if(e % 100 == 0):
        print('one-hot target: ', cost_total)

# test....
result_1 = matrix_mul_bias(test_X, weight, bias)
result_2 = matrix_mul_bias(result_1, weight_2, bias)

# get prediction
prediction = []
for r in result_2:
    prediction.append(max(enumerate(r), key=lambda x:x[1])[0])
print('prediction:', prediction)

# calculate acuration
accuracy = 0.0
for i in range(len(prediction)):
    if prediction[i] == int(test_y[i]):
        accuracy += 1
print('accuracy: ', accuracy / len(prediction) * 100, "%")