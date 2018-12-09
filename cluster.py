
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn as skl
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score



# Reading in the data
df = pd.read_excel('ClusteringDataset.xlsx', 'Sheet1') # Reading in the data file
datamattotal = df.values # Creating a matrix from the data 
datamat = datamattotal[1:,-2:]


# Perform kmeans clustering algorithm on the data and printing out the
# silhouette coefficient
kmeans = KMeans(n_clusters=3).fit(datamat)
centroids = kmeans.cluster_centers_
kmeanspredict = kmeans.predict(datamat)
score = silhouette_score(datamat, kmeanspredict, metric='euclidean')
print("Silhouette coefficient = " + str(score))


# Plotting the data
f = plt.figure()
plt.scatter(datamat[:, 0], datamat[:, 1], c=kmeanspredict, s=50)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=200, alpha=0.5);
plt.xlabel('x1')
plt.ylabel('x2')
plt.show()
f.savefig("ClusterPlot.pdf", bbox_inches='tight')

