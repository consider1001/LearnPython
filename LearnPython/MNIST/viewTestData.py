__author__ = 'Li'

import csv
import numpy

def writeIntoFile(arr,csvfilename):
    arr = numpy.array(arr).reshape(28,28)
    f = open(csvfilename,'wb')
    for i in range(28):
        list1 =  arr[i]
        text = ''.join(map(str,list1))  # list to str
        csvWriter = csv.writer(f)
        csvWriter.writerow(list1)
    f.close()
