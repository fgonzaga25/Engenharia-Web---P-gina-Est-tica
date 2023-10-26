import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

x = np.array([[1, 2], [5, 8], [5, 1], [8, 8], [1, 6], [9, 11],
              [2, 3], [3, 2], [6, 7], [7, 6], [4, 5],
              [5, 4], [9, 10], [10, 9], [8, 7], [7, 8],
              [1, 2], [2, 2], [3, 2], [3, 3], [3, 4], [3, 5],
              [1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6],
              [1, 1], [2, 3], [3, 1], [4, 3], [5, 1], [6, 3],
              [1, 1], [1, 2], [2, 2], [2, 3], [3, 3], [3, 4]
            ])

kmeans = KMeans(n_clusters=3)
kmeans.fit(x)

centroids = kmeans.cluster_centers_
labels = kmeans.labels_

colors = ["g.", "r.", "y."]
for i in range(len(x)):
    plt.plot(x[i][0], x[i][1], colors[labels[i]], markersize=10)

plt.scatter(centroids[:, 0], centroids[:, 1], marker="x", s=150, linewidths=5, zorder=10)
plt.show()