#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()



#########################################################
### your code goes here ###
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

""" slicing the train dataset to 1% of the original"""
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]

svc_clf = SVC(C=10000.0, kernel="rbf")  # c is optimum here
t0 = time()
svc_clf.fit(features_train, labels_train)
print "time taken to train {}".format(round(time()-t0, 3))
t1 = time()
pred = svc_clf.predict(features_test)
print "time taken to predict {}".format(round(time()-t1, 3))
accuracy = accuracy_score(pred, labels_test)
print "accuracy score for rbf kernel svm is {}".format(accuracy)
#print "output class for 10th, 26th and 50th elements are {}, {} and {}".format(pred[10], pred[26], pred[50])
print len(features_test)
print sum(pred)

#########################################################


