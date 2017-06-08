# In this exercise, we'll use the Titanic dataset as before, train two classifiers and
# look at their confusion matrices. Your job is to create a train/test split in the data
# and report the results in the dictionary at the bottom.

import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
# Load the dataset
from sklearn import datasets

X = pd.read_csv('titanic_data.csv')

X = X._get_numeric_data()
y = X['Survived']
del X['Age'], X['Survived']


from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB

# TODO: split the data into training and testing sets,
# using the default settings for train_test_split (or test_size = 0.25 if specified).
# Then, train and test the classifiers with your newly split data instead of X and y.
X_train, X_test, y_train, y_test= train_test_split(X, y, test_size=0.25, random_state=0)
clf1 = DecisionTreeClassifier()
clf1.fit(X_train,y_train)
dt = confusion_matrix(y_test,clf1.predict(X_test))
print "Confusion matrix for this Decision Tree:\n",dt
print "Decision Tree recall: {:.2f} and precision: {:.2f}".format(recall(y_test,clf1.predict(X_test)),precision(y_test,clf1.predict(X_test)))

clf2 = GaussianNB()
clf2.fit(X_train,y_train)
gc = confusion_matrix(y_test,clf2.predict(X_test))
print "GaussianNB confusion matrix:\n",gc
print "GaussianNB recall: {:.2f} and precision: {:.2f}".format(recall(y_test,clf2.predict(X_test)),precision(y_test,clf2.predict(X_test)))

#TODO: store the confusion matrices on the test sets below

confusions = {
 "Naive Bayes": gc,
 "Decision Tree": dt
}