__author__ = 'Li'

import csv
from numpy import *

print 'hello world'

fcsv = open('train.csv','rb')
lineNumber = 0
for row in csv.reader(fcsv):
    if lineNumber == 0:
        lineNumber = lineNumber + 1
        continue

    print 'row = '
    row = map(int, row)
    print row[1:]
    print ''.join(map(str,row[1:]))
    print row[1:]
    array = array(row[1:])
    array = array.reshape(28,28)
    f = open('array.csv','wb')
    for i in range(28):
        list1 =  array[i]
        text = ''.join(map(str,list1))  # list to str
        print text
        csvWriter = csv.writer(f)
        csvWriter.writerow(list1)
    f.close()
    if lineNumber == 1:
        print '\nbreak'
        break
    lineNumber = lineNumber +  1