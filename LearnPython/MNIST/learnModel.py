__author__ = 'Li'

'''

'''

import numpy
import readData
from sklearn import svm
import pickle
from sklearn import neighbors
import time
import csv
# my module
import viewTestData

# write into csv
def write_intoCSV(data, filename):
    f = open(filename, 'wb')
    csvWriter = csv.writer(f)
    for line in data:
        csvWriter.writerow(line)
    f.close()

# neural networks
def nn(trainData, trainLabel):

    return 0

def SVM_train(trainData, trainLabel):
    clf = svm.SVC(kernel='rbf', gamma=0.7, C=1.0)
    clf.fit(trainData,trainLabel)

    f = file('svmParameter.pkl','wb')
    pickle.dump(clf,f,False)               # False : whether write binary
    f.close()
    #print clf.predict(trainData[3])
    return 0

def SVM_predict(predictData):
    f = file('svmParameter.pkl','rb')
    clf = pickle.load(f)
    f.close()
    return clf.predict(predictData)

def KNN_train(trainData, trainLabel):
    n_neighbors = 5
    weights = 'distance'
    clf = neighbors.KNeighborsClassifier(n_neighbors,weights)
    clf.fit(trainData,trainLabel)
    #write into file
    f = file('KNNParameter.pkl','wb')
    pickle.dump(clf,f,False)               # False : whether write binary
    f.close()

def KNN_prediction(predictData):
    start_time = time.time()
    f = file('KNNParameter.pkl','rb')
    clf = pickle.load(f)
    f.close()
    end_time  = time.time()
    print 'time used load file is %d' % (end_time - start_time)
    return clf.predict(predictData)

def precision(prediction, label):
    length = prediction.shape[0]
    count = 0.0
    for i in range(length):
        if knn_prediction[i] == predictLabel[i]:
            count =count + 1
        else :
            print str(i)+' '+str(knn_prediction[i])+'   '+str(predictLabel[i])
    print 'Predict %d hit %d' %(length, count)
    print 'Precision is %f %% ' % (count/length*100)

if __name__ == '__main__':
    # labelArray, dataArray = readData.readTrainData('trainTrain.csv', -1)
    #predictLabel, predictData= readData.readTrainData('trainTest.csv',-1)
    predictData  =  readData.readTestData('test.csv',-1)
    # SVM_train(dataArray,labelArray)
    start_time = time.time()
    knn_prediction = KNN_prediction(predictData)
    end_time  = time.time()
    data = []
    for i in range(knn_prediction.shape[0]):
        data.append([i+1,knn_prediction[i]])
    data.insert(0,['ImageId','Label'])
    write_intoCSV(data, 'result.csv')
    #precision(knn_prediction, predictLabel)
    print 'time used is %f' % (end_time - start_time)
    # print 'predictData'
    # #print predictData[0]
    # print predictData
    # #print SVM_predict(predictData)
    # print predictLabel
    # for i in range(10):
    #     print 'predict' + str(i)
    #     print SVM_predict(dataArray[i])
    #     print 'label'
    #     print labelAarray[i]
    # for i in range(1000):
    #     print 'predict' + str(i)
    #     print SVM_predict(predictData[i])
    #     print 'label'
    #     print predictLabel[i]


