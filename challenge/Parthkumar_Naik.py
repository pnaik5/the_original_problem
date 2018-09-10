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
#It's kk to import whatever you want from the local util module if you would like:
#from util.X import ... 

def classify(labels):
    #method to classify labels
    random_number = np.randon.randint (low=0, high =len(labels)-1)
    #finding random integer
    return labels [random_number]
    
    #returning a value
    print "Enter some names:"
    labels = raw_input().split()
    #splitting labels
    print "classify:", classify(labels)
    #print generated label
