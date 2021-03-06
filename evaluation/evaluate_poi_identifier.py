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
from sklearn import tree

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score

from sklearn.model_selection import train_test_split

features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size=0.3, random_state=42)

clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

print "Accuracy:", accuracy_score(pred, labels_test)

# How many POIs are predicted for the TEST set?
print 'Number of predicted POIs: ', sum(labels_test)
# How many people total are in the test set?
print 'Total people in the test set: ', len(labels_test)
# If your identifier predicted 0. (not POI) for everyone in the test set, what would its accuracy be?
print accuracy_score([0] * 29, labels_test)

i_labels_test = [i for i in range(len(labels_test)) if labels_test[i]]
i_pred = [i for i in range(len(pred)) if pred[i]]
print i_labels_test, i_pred

TP = 0
TN = 0
FP = 0
FN = 0
for ii, jj in zip(labels_test, pred):
    if ii == 1 and jj == 1:
        TP += 1
    if ii == 0 and jj == 0:
        TN += 1
    if ii == 0 and jj == 1:
        FP += 1
    if ii == 1 and jj == 0:
        FN += 1
print 'True positive: ', TP, '\nTrue negative: ', TN, '\nFalse positive: ', FP, '\nFalse negative: ', FN

print 'Precision: ', precision_score(labels_test, pred)
print 'Recall: ', recall_score(labels_test, pred)
