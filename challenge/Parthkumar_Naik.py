## ---------------------------- ##
## 
## sample_student.py
##
## Example student submission for programming challenge. A few things: 
## 1. Before submitting, change the name of this file to your firstname_lastname.py.
## 2. Be sure not to change the name of the method below, classify.py
## 3. In this challenge, you are only permitted to import numpy and methods from 
##    the util module in this repository. Note that if you make any changes to your local 
##    util module, these won't be reflected in the util module that is imported by the 
##    auto grading algorithm. 
## 4. Anti-plagarism checks will be run on your submission
##
##
## ---------------------------- ##

import numpy as np

labels = ['brick', 'ball', 'cylinder']
"""
brick = 0;
ball = 1;
cylinder = 2;
"""

class KNN(object):""""a kNN classifier with L2 distance"""

def __init__(self):
    pass

def train(self, X, y):
    self.X_train = X
    self.y_train = y
   

def classify(self, X, k=1):
   """
       predict the label
   """
   distances = L2Distance(X)

   return self.predictLabels(distances)


def L2Distance(self, X):
   #test between the images
    num_test = X.shape[0]
    num_train = self.X_train.shape[0]
    dists = np.zeros((num_test, num_train))

    dists = np.sqrt(np.sum(X**2, axis=1).reshape(num_test, 1)
     + np.sum(self.X_train**2, axis=1) - 2 * X.dot(self.X_train.T))
    return dists


def predictLabels(self, dists, k=1):
    """
    find nearest test image
    """
    num_test = dists.shape[0]
    y_pred = np.zeros(num_test)
    for i in range(num_test):

      closest_y = []

      top_k_indx = np.argsort(dists[i])[:k]
    
      closest_y = self.y_train[top_k_indx]
    
      vote = Counter(closest_y)
    
      count = vote.most_common()

      y_pred[i] = count[0][0]
    return y_pred


"""
#initialize a knn classifer

classifier = KNearestNeighbor()

classifier.train(X_train, y_train)

label = classifier.classify(im)

if im ==0:
   out = "brick"
elif(im==1):
   out = "ball"
else:
   out = "cylinder"
"""
