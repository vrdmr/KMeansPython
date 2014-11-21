__author__ = 'user1'
from com.vrdmr.clustering.algorithms import kmeans
import com.vrdmr.io.FileReader as FR
import numpy as np
import re
import pandas as pd

def ind_match(filename):
    fr = open(filename)
    singleLine = fr.next()
    singleLine = re.sub(r'[ ]+', ',', singleLine)
    listFromString = singleLine.split(',')
    try:
        if type(float(listFromString[0])) == type(1.0):
            pass
    except ValueError:
        ref_index = []
        fr = open(filename)
        for record in fr.readlines():
            record = record.strip()
            record = re.sub(r'[ ]+', ',', record)
            recordList = record.split(',')
            ref_index.append(recordList[0])
        return ref_index

def readFileIntoMatrix1(filename):
    """
    Return the x intercept of the line M{y=m*x+b}.  The X{x intercept}
    of a line is the point at which it crosses the x axis (M{y=0}).

    This function can be used in conjuction with L{z_transform} to
    find an arbitrary function's zeros.

    @type  m: number
    @param m: The slope of the line.
    @type  b: number
    @param b: The y intercept of the line.  The X{y intercept} of a
              line is the point at which it crosses the y axis (M{x=0}).
    @rtype:   number
    @return:  the x intercept of the line M{y=m*x+b}.
    """

    fr = open(filename)
    numOfLines = len(fr.readlines())
    fr = open(filename)
    singleLine = fr.next()
    singleLine = re.sub(r'[ ]+', ',', singleLine)
    listFromString = singleLine.split(',')
    try:
        if type(float(listFromString[0])) == type(1.0):
            inputRecordsMatrix = np.zeros((numOfLines, len(listFromString)))
            fr = open(filename)
            index = 0
            for record in fr.readlines():
                record = record.strip()
                recordList = record.split(',')
                inputRecordsMatrix[index, :] = recordList[:]
                index += 1
            return inputRecordsMatrix
    except ValueError:
        inputRecordsMatrix = np.zeros((numOfLines, len(listFromString)-1))
        fr = open(filename)
        index = 0
        li = []
        for record in fr.readlines():
            record = record.strip()
            record = re.sub(r'[ ]+', ',', record)
            recordList = record.split(',')
            li.append(recordList[0])
            inputRecordsMatrix[index] = map(float,(recordList[1:]))
            index += 1
        return inputRecordsMatrix

def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = np.zeros(np.shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - np.tile(minVals, (m, 1))
    normDataSet = normDataSet / np.tile(ranges, (m, 1))
    return normDataSet, ranges, minVals, maxVals

FILE_NAME = "C:/Users/user1/Google Drive/research_works/Clustering/com/vrdmr/io/milk.dat"

records_mat = readFileIntoMatrix1(FILE_NAME)
norm_records_mat, ranges, min_values, max_values = FR.autoNorm(records_mat)
New_Frame = pd.DataFrame(norm_records_mat,ind_match(FILE_NAME))
clusters, centroids = kmeans.apply_clustering(norm_records_mat, 2, 2)

print "Summary"
print "Clusters Length"
for i in clusters:
    for j in clusters[i]:
        for k in ind_match(FILE_NAME):
            if list(New_Frame.ix[k]) == list(j):
                print k
    print "Clusters Centroid", centroids[i]