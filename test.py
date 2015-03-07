#coding:utf-8
__author__ = 'Li'

import scipy
import types
import string

# print 'hello world!'
# hello =  'te{0}ts{1}t'.format('000','111')
# str = 'hello中文'
# print ('hello'+str)
# print hello

#read file
f =  open('0_0.txt','r')
flag  = 0
for line in f:
    #remove the \n
    line = line.strip()
    #convert str into list
    linelist = list(line)
    print linelist
    print linelist
    # linelist = [int(item) for item in line ]
    if flag == 0:
        print len(linelist)
        flag = flag + 1
    flag = flag +1
print flag

