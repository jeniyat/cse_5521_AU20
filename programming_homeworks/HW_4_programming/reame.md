In this assignment you will train linear models using stochastic gradient descent to predict whether a human subject is viewing a picture or reading a sentence from their fMRI brain image data.


NOTE: It may take some time to run the experiments for this assign- ment, so we recommend that you start early. 

# Data

The data comes from the [starplus dataset](http://www.cs.cmu.edu/afs/cs.cmu.edu/project/theo-81/www/) (only the first subject). 

We provide starter code to read the provided matlab file into Python/Numpy arrays. 

The data for each trial consists of a sequence of brain images that we have flattened into a feature vector X. Your task is to train a linear classifier that outputs, y \(\epsilon\) {+1,-1}

