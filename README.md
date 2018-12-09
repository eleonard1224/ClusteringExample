# ClusteringExample
Exercise which uses kmeans clustering from scikit-learn on a sample dataset

This repository contains Python code which uses scikit-learn's KMeans clustering algorithm to separate a dataset into three clusters.
The dataset is located in this repository as ClusteringDataset.xlsx.  It was created so as to contain a dataset which was
fairly well-separated into three different clusters.  The Python code in this repository is located in cluster.py.  In addition to 
utilizing the KMeans clustering algorithm, cluster.py calculates the Silhouette Coefficient for the dataset contained 
in ClusteringDataset.xlsx and then plots the cluster centers as well as the data itself using a color-coding scheme based on the 
KMeans algorithm. The resulting plot is stored in this repository as ClusterPlot.pdf.
