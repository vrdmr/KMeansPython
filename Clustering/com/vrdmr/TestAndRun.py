__author__ = 'varad'

import numpy as np
import sklearn.cluster as cluster

data = [[5.1, 3.5, 1.4, 0.1], [5.4, 3.7, 1.5, 0.2], [5.4, 3.4, 1.7, 0.2], [4.8, 3.1, 1.6, 0.2], [5.0, 3.5, 1.3, 0.3],
        [7.0, 3.2, 4.7, 1.4], [5.0, 2.0, 3.5, 1.0], [5.9, 3.2, 4.8, 1.8], [5.5, 2.4, 3.8, 1.1], [5.5, 2.6, 4.4, 1.2],
        [6.3, 3.3, 6.0, 2.5], [6.5, 3.2, 5.1, 2.0], [6.9, 3.2, 5.7, 2.3], [7.4, 2.8, 6.1, 1.9], [6.7, 3.1, 5.6, 2.4]]

initial_centroids_indices = [0,5,10]

nddata = np.ndarray(np.array(data).shape, buffer=np.array(data))

meanscaled = nddata - nddata.mean(axis=0)
range = meanscaled.max(axis=0) - meanscaled.min(axis=0)
normalised = meanscaled / range

initial_centroids = normalised[initial_centroids_indices,]

kmeans = cluster.KMeans(n_clusters=3, max_iter=400, precompute_distances=True, tol=0.0001, n_jobs=1, verbose=0,
                    random_state=None, copy_x=True, init=initial_centroids)

kmeans.Fit(normalised)

kmeans.labels_
kmeans.cluster_centers_