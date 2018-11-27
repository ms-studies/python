from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np

def runKnnClustering(data_without_class, class_column):
    # findNumberOfClusters(data_without_class)
    kmeans = KMeans(n_clusters = 2, max_iter = 300, random_state = 0)
    y_kmeans = kmeans.fit_predict(data_without_class)

    zeroMeansB = True
    counter = 0
    for i in range(len(class_column)):
        if (y_kmeans[i] == 0 and class_column[i] == 'b') or (y_kmeans[i] == 1 and class_column[i] == 'g'):
            counter += 1

    coverage = counter / len(class_column)
    if coverage < 0.5:
        coverage = 1 - coverage
        zeroMeansB = False
    print("Clustering coverage: "+str(int(100*coverage))+"%")
    
    #Visualising the clusters
    plt.subplot(2, 1, 2)
    plt.scatter(data_without_class[y_kmeans == 0, 0], data_without_class[y_kmeans == 0, 1], s = 100, c = 'blue' if zeroMeansB else 'green', label = 'b' if zeroMeansB else 'g')
    plt.scatter(data_without_class[y_kmeans == 1, 0], data_without_class[y_kmeans == 1, 1], s = 100, c = 'green' if zeroMeansB else 'blue', label = 'g' if zeroMeansB else 'b')
    plt.legend()

    #Plotting the centroids of the clusters
    plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:,1], s = 100, c = 'yellow', label = 'Centroids')
