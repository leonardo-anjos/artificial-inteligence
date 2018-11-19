## steps to implements algorithm 

**k-nearest neighbors [knn]**
1. handler data 
2. calculate the distance between two data instances 
3. locale k most similar data instances
4. generate a response from a set of data instances
5. summarize the accuracy of predictions
6. tie it all together

**k-means [centroid]**
1. handle data: clean the file, normalize the parameters, given numeric values to non-numeric attributes. read data from the file and split the data for cross validation
2. find initial centroids: choose k centroids in random
3. distance calculation: finding the distance between each of the datapoints with each of the centroids. this distance metric is used to find the which cluster the points belong to
4. re-calculating the centroids: find the new values for centroid
5. stop the iteration: stop the algorithm when the difference between the old and the new centroids is negligible

