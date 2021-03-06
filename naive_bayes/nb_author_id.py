#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project. 

    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
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
from sklearn.naive_bayes import GaussianNB
g_clf = GaussianNB()
start_time = time()
g_clf.fit(features_train, labels_train)
# print "training time {} seconds".format(round(time()-start_time, 3))
start_time_pred = time()
pred = g_clf.predict(features_test)
# print "prediction time {} seconds".format(round(time()-start_time_pred, 3))
#print pred
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(labels_test, pred)
print accuracy
print sum(pred)

#########################################################


