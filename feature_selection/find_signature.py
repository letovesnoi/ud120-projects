#!/usr/bin/python

import pickle
import numpy
numpy.random.seed(42)


### The words (features) and authors (labels), already largely processed.
### These files should have been created from the previous (Lesson 10)
### mini-project.
words_file = "../text_learning/your_word_data.pkl" 
authors_file = "../text_learning/your_email_authors.pkl"
word_data = pickle.load( open(words_file, "r"))
authors = pickle.load( open(authors_file, "r") )



### test_size is the percentage of events assigned to the test set (the
### remainder go into training)
### feature matrices changed to dense representations for compatibility with
### classifier functions in versions 0.15.2 and earlier
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(word_data, authors, test_size=0.1, random_state=42)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
features_train = vectorizer.fit_transform(features_train)
features_test = vectorizer.transform(features_test).toarray()


### a classic way to overfit is to use a small number
### of data points and a large number of features;
### train on only 150 events to put ourselves in this regime
features_train = features_train[:150].toarray()
labels_train = labels_train[:150]



### your code goes here
from sklearn import tree
from sklearn.metrics import accuracy_score

clf = tree.DecisionTreeClassifier()
clf.fit(features_train, labels_train)
pred = clf.predict(features_test)
print "Accuracy:", accuracy_score(pred, labels_test)
print 'Number of training points: ', len(features_train)

# check overfitting (accuracy on training data >> accuracy on test)
pred_train = clf.predict(features_train)
print "Accuracy on training data:", accuracy_score(pred_train, labels_train)


# What's the importance of the most important feature?
# What is the number of this feature?
import numpy as np

importances = [importance for importance in clf.feature_importances_ if importance > 0.2]
max_importance = max(clf.feature_importances_)
max_ind = np.argmax(clf.feature_importances_)
print 'Importances: ', importances
print 'Max importance: ', max_importance, 'Index: ', max_ind

# Get the most important word with TfIdf
print 'The most important word: ', vectorizer.get_feature_names()[max_ind]
