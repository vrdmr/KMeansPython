from random import randrange
import numpy
import sys
from com.vrdmr.clustering.distance import DistanceMetrics

__author__ = 'Varad Meru'
__version__ = '0.1'
__since__ = '0.1'

'''
Takes 3 parameters - The Normalised Records, The number of Iterations
and the Number of Clusters required.
Returns the Cluster{} and Centroids{}, with the key being the key.
'''
def cluster_algorithm(mat_records, num_iterations, num_clusters, initial_centroids, initial_clusters):
    # Get the initial clusters and centroids
    if initial_centroids is None and initial_clusters is None:
        print "Check the initial clusters and centroids passed", initial_clusters ,initial_centroids
        sys.exit(1)
        # exit(0) check the python version

    # Run the number of iterations
    for i in range(num_iterations):
        print "Iteration num: ", i
        # Create a new set of clusters and calculate new centroids from the clusters
        new_temp_clusters = {}
        new_temp_centroids = {}

        # Initialize the new_temp_* objects
        for i in range(num_clusters):
            new_temp_clusters[i] = list()
            new_temp_centroids[i] = list()

        # For all the records in the matrix
        for record in mat_records:

            # No use of distance_to_centroid
            closest_centroid, distance_to_centroid = find_nearest_centroid(record, centroids)

            # Adding the data point to the cluster whose centroid is the closest to it.
            new_temp_clusters.get(closest_centroid).append(record)

        # After all the data points have been distributed, the new centroids would be calculated
        for i in clusters:
            new_temp_centroids.get(i).append(numpy.average(new_temp_clusters.get(i), axis=0))

        # As we are using the "centroids" variable to be sent to find_nearest_centroid,
        # we will re-initiate it and assign it the new centroids calculated above
        centroids = new_temp_centroids

    # And we return the Clusters and the Centroids.
    return new_temp_clusters, centroids


'''
Returns the initial set of clusters as a Dictionary.
Randomly distributing the points to the lists.
Dictionary helps in keeping things manageable
'''
def get_initial_clusters(mat_records, num_clusters):

    # Initial Clusters
    clusters = {}
    centroids = {}

    for i in range(num_clusters):
        clusters[i] = list()
        centroids[i] = list()

    # For all the records, randomly distribute the data-points to the random clusters
    for i in mat_records:
        random_num = randrange(0, num_clusters)
        clusters.get(random_num).append(i)

    for i in clusters:
        centroids.get(i).append(numpy.average(clusters.get(i), axis=0))

    return clusters, centroids


'''
Finds the nearest centroid to the datapoint being passed.
Returns the index of the centroid
'''
def find_nearest_centroid(data_point, centroids):
    closest_distance = sys.float_info.max
    closest_index = 0
    # print "Check"
    # print closest_distance
    # print closest_index

    for centroidKey in centroids.iterkeys():
        current_distance = DistanceMetrics.euclidean_distance_1d_arrays(numpy.asarray(data_point),
                                                                        numpy.asarray(centroids.get(centroidKey)[0]))
        if current_distance < closest_distance:
            closest_distance = current_distance
            closest_index = centroidKey
        else:
            continue
    return closest_index, closest_distance

def get_initial_clusters_from_data(mat_records, num_clusters):

    # Initial Clusters
    clusters = {}
    centroids = {}

    for i in range(num_clusters):
        clusters[i] = list()
        centroids[i] = list()

'''
    # For all the records, randomly distribute the data-points to the random clusters
    for i in mat_records:
        random_num = randrange(0, num_clusters)
        clusters.get(random_num).append(i)

    for i in clusters:
        centroids.get(i).append(numpy.average(clusters.get(i), axis=0))
'''
    return clusters, centroids