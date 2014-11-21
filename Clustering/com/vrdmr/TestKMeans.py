from com.vrdmr.clustering.algorithms import kmeans
import numpy as np

__author__ = 'Varad Meru'

#records_mat = fr.readFileIntoMatrix2("milk-modified.dat",',')
#norm_records_mat,ranges, min_values, max_values = fr.autoNorm(records_mat)
data = [[5.1, 3.5, 1.4, 0.1], [5.4, 3.7, 1.5, 0.2], [5.4, 3.4, 1.7, 0.2], [4.8, 3.1, 1.6, 0.2], [5.0, 3.5, 1.3, 0.3],
        [7.0, 3.2, 4.7, 1.4], [5.0, 2.0, 3.5, 1.0], [5.9, 3.2, 4.8, 1.8], [5.5, 2.4, 3.8, 1.1], [5.5, 2.6, 4.4, 1.2],
        [6.3, 3.3, 6.0, 2.5], [6.5, 3.2, 5.1, 2.0], [6.9, 3.2, 5.7, 2.3], [7.4, 2.8, 6.1, 1.9], [6.7, 3.1, 5.6, 2.4]]

#clusters, centroids = kmeans.apply_clustering(norm_records_mat, 10, 2)
# init_clusters, init_centroids = kmeans.get_initial_clusters(data, 3)

init_clusters, init_centroids = kmeans.get_initial_clusters_from_data(np.matrix(data), [1,6,11])
final_clusters, final_centroids = kmeans.cluster_algorithm(data, 100, 3, init_clusters, init_centroids)

print "Summary"
print "Clusters Length"
for i in clusters:
    print "Number of Members", len(clusters[i])
    print "Clusters Centroid", centroids[i]