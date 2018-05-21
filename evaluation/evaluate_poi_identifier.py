#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here 
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.cross_validation import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, 
																			random_state=42)

clf = DecisionTreeClassifier(min_samples_split=2)  # default (for practice)
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
poi_count = 0
for i in pred:
	if i == 1:
		poi_count += 1
print "poi's in test set: ", poi_count
print "total points in test set: ", len(labels_test)
print "accuracy score for train data: ", accuracy_score(pred, labels_test)
print pred
print labels_test

print "precision score: ", precision_score(labels_test, pred)
print "recall score: ", recall_score(labels_test, pred)

