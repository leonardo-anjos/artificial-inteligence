#!/usr/bin/env python
# coding: utf-8

# ## k-means clustering on the Iris dataset
# 
# - clustering data
# - unsupervised learning

# In[10]:


# @see https://towardsdatascience.com/unsupervised-learning-with-python-173c51dc7f03<br>
# @author leonardo-anjos


# In[2]:


# import libs
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# load and handler data with pandas
dataset = pd.read_csv('./data/iris.csv')
x = dataset.iloc[:, [1, 2, 3, 4]].values


# In[6]:


# finding the optimum number of clusters for k-means classification
# this method allows us to pick the optimum amount of clusters for classification
from sklearn.cluster import KMeans
wcss = []

for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
    
# plotting the results discovery
plt.plot(range(1, 11), wcss)
plt.title('result')
plt.xlabel('numbers of clusters')
plt.ylabel('squares sum') # this is the sum of squares in cluster
plt.show()


# In[11]:


# applying k-means clustering to the dataset and creating k-means classifier
kmeans = KMeans(n_clusters = 3, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
y_kmeans = kmeans.fit_predict(x)


# In[14]:


# visualising the clusters
plt.scatter(x[y_kmeans == 0, 0], x[y_kmeans == 0, 1], s = 100, c = 'orange', label = 'iris-setosa')
plt.scatter(x[y_kmeans == 1, 0], x[y_kmeans == 1, 1], s = 100, c = 'green', label = 'iris-versicolour')
plt.scatter(x[y_kmeans == 2, 0], x[y_kmeans == 2, 1], s = 100, c = 'blue', label = 'irirs-virginica')


# In[15]:


# plotting the centroids of the clusters
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:,1], s = 100, c = 'black', label = 'centroids')
plt.legend()


# In[ ]:




