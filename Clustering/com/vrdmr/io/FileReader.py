import numpy as np

__author__ = 'Varad Meru'
__version__ = '0.1'
__since__ = '0.1'

# Assumes the ',' to be the default delim
def readFileIntoMatrix1(filename):
    __DELIM__ = ','

    # Opening the file
    fr = open(filename)

    # Number of lines in the file a.k.a. number of records in the file
    numOfLines = len(fr.readlines())

    # For Finding out the number of dimensions in the file
    # First reading a single record, splitting it by delim
    # and knowing the size of the list generated
    fr = open(filename)
    singleLine = fr.next()

    # Stripping off the return line character
    singleLine = singleLine.strip()

    # Splitting the line and getting a List back
    listFromString = singleLine.split(__DELIM__)

    # Making a zero matrix
    inputRecordsMatrix = np.zeros((numOfLines, len(listFromString)))

    # Now Reading record by record and adding it to the Matrix
    fr = open(filename)
    index = 0
    for record in fr.readlines():
        record = record.strip();
        recordList = record.split(__DELIM__)
        inputRecordsMatrix[index, :] = recordList[:]
        index += 1

    return inputRecordsMatrix

# Takes the delim as a param
def readFileIntoMatrix2(filename, delim):
    # Opening the file
    fr = open(filename)

    # Number of lines in the file a.k.a. number of records in the file
    numOfLines = len(fr.readlines())

    # For Finding out the number of dimensions in the file
    # First reading a single record, splitting it by delim
    # and knowing the size of the list generated
    fr = open(filename)
    singleLine = fr.next()

    # Stripping off the return line character
    singleLine = singleLine.strip()

    # Splitting the line and getting a List back
    listFromString = singleLine.split(delim)

    # Making a zero matrix
    inputRecordsMatrix = np.zeros((numOfLines, len(listFromString)))


    # Now Reading record by record and adding it to the Matrix
    fr = open(filename)
    index = 0
    for record in fr.readlines():
        record = record.strip();
        recordList = record.split(delim)
        inputRecordsMatrix[index, :] = recordList[:]
        index += 1

    return inputRecordsMatrix


def readfile_df1(filename):
    __DELIM__ = ','

    # Opening the file
    fr = open(filename)

    # Number of lines in the file a.k.a. number of records in the file
    numOfLines = len(fr.readlines())

    # For Finding out the number of dimensions in the file
    # First reading a single record, splitting it by delim
    # and knowing the size of the list generated
    fr = open(filename)
    singleLine = fr.next()

    # Stripping off the return line character
    singleLine = singleLine.strip()

    # Splitting the line and getting a List back
    listFromString = singleLine.split(__DELIM__)


def readfile_df2(filename, delim):
    print "Hello World"


def readfile_df3(filename, delim, bool_colHeader, bool_rowHeader):
    print "Hello World"


def readfile_lol(filename, delimeter):
    # Making a zero matrix
    list_of_records = []

    # Now Reading record by record and adding it to a ListOfList
    fr = open(filename)
    index = 0
    for record in fr.readlines():
        record = record.strip();
        record_list = record.split(delimeter)
        list_of_records.append(record_list)
        index += 1

    # Now converting the List of Lists (String format) into a Float LoL
    list_of_records_float = []
    for record in list_of_records:
        list_of_records_float.append(map(float, record))

    return list_of_records_float


def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = np.zeros(np.shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - np.tile(minVals, (m, 1))
    normDataSet = normDataSet / np.tile(ranges, (m, 1))
    return normDataSet, ranges, minVals, maxVals


#Safety -  Prints the output of the program after reading from the file
if __name__ == '__main__':
    print readfile_lol("milk-modified.dat", ',')
