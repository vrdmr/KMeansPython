import numpy as np
import scipy.spatial.distance as scid

__author__ = 'Varad Meru'
__version__ = '0.1'
__since__ = '0.1'

# Computers tthe distance between two 1d numpy matrices
def euclidean_distance_1d_matrix(list_dataPoint1, list_dataPoint2):
    return np.linalg.norm(list_dataPoint1-list_dataPoint2)

# Computes the Euclidean distance between two 1-D arrays.
def euclidean_distance_1d_arrays(list_dataPoint1, list_dataPoint2):
    return scid.euclidean(list_dataPoint1,list_dataPoint2)