__author__ = 'Li'

from numpy import *
import csv

lable = []

def read(filename):
    fcsv = open('train.csv','rb')
    lineNumber = 0
    for row in csv.reader(fcsv):
        if lineNumber-lineNumber/1000*1000 == 1:
            print 'linenumber'
            print lineNumber
        if lineNumber == 0:
            lineNumber = lineNumber + 1
            continue
        row = map(int, row)
        #create train data array
        if lineNumber == 1:
            arr = array(row[1:])
            lable.append(row[0])
            lineNumber = lineNumber + 1
            continue
        arr = vstack((arr, array(row[1:])))
        #create train lable array
        lable.append(row[0])
        # if lineNumber == 2:
        #     print 'break'
        #     break
        lineNumber = lineNumber + 1
    return lable, arr
if __name__ == '__main__':
    lable, arr = read('train.csv')
    print 'lable'
    print lable
    print 'array'
    print arr.shape