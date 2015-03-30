'''
read data
'''
__author__ = 'Li'



from numpy import *
import csv
import viewTestData

def readTrainData(filename, numberOfLines):
    '''
    read data from .csv file
    :param filename: the name of the .csv file
    :param numberOfLines:  how many lines to read from the .csv file
    :return: labelArray :  the label data in 1*n matrix
    :return: arr :    the data in 1*n matrix
    '''
    label = []
    fcsv = open(filename,'rb')
    lineNumber = 0
    for row in csv.reader(fcsv):
        if lineNumber-lineNumber/1000*1000 == 1:
            print 'readTrainData.py linenumber'
            print lineNumber
        if lineNumber == 0:
            lineNumber = lineNumber + 1
            continue
        row = map(int, row)
        #create train data array
        if lineNumber == 1:
            arr = array(row[1:])
            label.append(row[0])
            if lineNumber == numberOfLines:
                break
            lineNumber = lineNumber + 1
            continue
        arr = vstack((arr, array(row[1:])))
        #create train label array
        label.append(row[0])
        # if lineNumber == 2:
        #     print 'break'
        #     break
        lineNumber = lineNumber + 1
        if lineNumber == numberOfLines + 1:  #consider the first name line
            break
    labelArray = array(label)
    return labelArray, arr

def readTestData(filename, numberOfLines):
    '''
    read test Data
    :param filename:
    :param numbersOfLines:
    :return:
    '''
    fcsv = open(filename,'rb')
    lineNumber = 0
    for row in csv.reader(fcsv):
        if lineNumber-lineNumber/1000*1000 == 1:
            print 'readTestData.py linenumber'
            print lineNumber
        if lineNumber == 0:
            lineNumber = lineNumber + 1
            continue
        row = map(int, row)
        #create train data array
        if lineNumber == 1:
            arr = array(row[:])
            if lineNumber == numberOfLines:
                print 'break'
                break
            lineNumber = lineNumber + 1
            continue
        arr = vstack((arr, array(row[:])))
        lineNumber = lineNumber + 1
        if lineNumber == numberOfLines + 1:  #consider the first name line
            break
    return arr

if __name__ == '__main__':
    a = readTestData('test.csv',10)
    print a
