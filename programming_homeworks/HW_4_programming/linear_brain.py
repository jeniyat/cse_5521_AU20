import scipy.io as sio
import numpy as np
import math
import argparse

starplus = sio.loadmat("data-starplus-04847-v7.mat")


###########################################
metadata = starplus['meta'][0,0]
#meta.study gives the name of the fMRI study
#meta.subject gives the identifier for the human subject
#meta.ntrials gives the number of trials in this dataset
#meta.nsnapshots gives the total number of images in the dataset
#meta.nvoxels gives the number of voxels (3D pixels) in each image
#meta.dimx gives the maximum x coordinate in the brain image. The minimum x coordinate is x=1. meta.dimy and meta.dimz give the same information for the y and z coordinates.
#meta.colToCoord(v,:) gives the geometric coordinate (x,y,z) of the voxel corresponding to column v in the data
#meta.coordToCol(x,y,z) gives the column index (within the data) of the voxel whose coordinate is (x,y,z)
#meta.rois is a struct array defining a few dozen anatomically defined Regions Of Interest (ROIs) in the brain. Each element of the struct array defines on of the ROIs, and has three fields: "name" which gives the ROI name (e.g., 'LIFG'), "coords" which gives the xyz coordinates of each voxel in that ROI, and "columns" which gives the column index of each voxel in that ROI.
#meta.colToROI{v} gives the ROI of the voxel corresponding to column v in the data.
study      = metadata['study']
subject    = metadata['subject']
ntrials    = metadata['ntrials'][0][0]
nsnapshots = metadata['nsnapshots'][0][0]
dimx       = metadata['dimx'][0][0]
colToCoord = metadata['colToCoord']
coordToCol = metadata['coordToCol']
rois       = metadata['rois']
colToROI   = metadata['colToROI']
###########################################

###########################################
info = starplus['info'][0]
#info: This variable defines the experiment in terms of a sequence of 'trials'. 'info' is a 1x54 struct array, describing the 54 time intervals, or trials. Most of these time intervals correspond to trials during which the subject views a single picture and a single sentence, and presses a button to indicate whether the sentence correctly describes the picture. Other time intervals correspond to rest periods. The relevant fields of info are illustrated in the following example:
#info(18) mint: 894 maxt: 948 cond: 2 firstStimulus: 'P' sentence: ''It is true that the star is below the plus.'' sentenceRel: 'below' sentenceSym1: 'star' sentenceSym2: 'plus' img: sap actionAnswer: 0 actionRT: 3613
#info.mint gives the time of the first image in the interval (the minimum time)
#info.maxt gives the time of the last image in the interval (the maximum time)
#info.cond has possible values 0,1,2,3. Cond=0 indicates the data in this segment should be ignored. Cond=1 indicates the segment is a rest, or fixation interval. Cond=2 indicates the interval is a sentence/picture trial in which the sentence is not negated. Cond=3 indicates the interval is a sentence/picture trial in which the sentence is negated.
#info.firstStimulus: is either 'P' or 'S' indicating whether this trail was obtained during the session is which Pictures were presented before sentences, or during the session in which Sentences were presented before pictures. The first 27 trials have firstStimulus='P', the remained have firstStimulus='S'. Note this value is present even for trials that are rest trials. You can pick out the trials for which sentences and pictures were presented by selecting just the trials trials with info.cond=2 or info.cond=3.
#info.sentence gives the sentence presented during this trial. If none, the value is '' (the empty string). The fields info.sentenceSym1, info.sentenceSym2, and info.sentenceRel describe the two symbols mentioned in the sentence, and the relation between them.
#info.img describes the image presented during this trial. For example, 'sap' means the image contained a 'star above plus'. Each image has two tokens, where one is above the other. The possible tokens are star (s), plus (p), and dollar (d).
#info.actionAnswer: has values -1 or 0. A value of 0 indicates the subject is expected to press the answer button during this trial (either the 'yes' or 'no' button to indicate whether the sentence correctly describes the picture). A value of -1 indicates it is inappropriate for the subject to press the answer button during this trial (i.e., it is a rest, or fixation trial).
#info.actionRT: gives the reaction time of the subject, measured as the time at which they pressed the answer button, minus the time at which the second stimulus was presented. Time is in milliseconds. If the subject did not press the button at all, the value is 0.
###########################################

###########################################
data = starplus['data']
#data: This variable contains the raw observed data. The fMRI data is a sequence of images collected over time, one image each 500 msec. The data structure 'data' is a [54x1] cell array, with one cell per 'trial' in the experiment. Each element in this cell array is an NxV array of observed fMRI activations. The element data{x}(t,v) gives the fMRI observation at voxel v, at time t within trial x. Here t is the within-trial time, ranging from 1 to info(x).len. The full image at time t within trial x is given by data{x}(t,:).
#Note the absolute time for the first image within trial x is given by info(x).mint.
###########################################

MIN_LOSS_CHANGE=0.0001

def Prediction(X,W):
	return np.dot(W,np.transpose(X))

def LogisticLoss(X, Y, W, lmda):
    try:
        loss = lmda * np.sum(np.square(W))
    
        Y_pred = Prediction(X,W)
        loss += sum(map(lambda t: math.log(1. + math.exp(-t)), np.multiply(Y, Y_pred)))
    except:
        loss=709.78271
    
    return loss

def LogisticGradient(X, Y, W, lmda):
	Y_pred = Prediction(X,W)
    grad_vector = np.dot(np.multiply(Y, list(map( lambda t: -1. / (1. + math.exp(t)),    np.multiply(Y, Y_pred) )) ), X) + 2 * lmda * W

    return grad_vector
	

def SgdLogistic(X, Y, maxIter, learningRate, lmda):
    W = np.zeros(X.shape[1])
    
    
    
    loss_prev= LogisticLoss(X, Y, W, lmda)
    diff_loss = 1

    #TODO: implement stochastic gradient descent using the LogisticLoss  and LogisticGradient Fucntion

    	


    return W



def TrainLogisitcRegression(X, Y,  lmda, learningRate, maxIter=100, sample=range(20)):
    #Leave one out cross validation accuracy
    nCorrect   = 0.
    nIncorrect = 0.
    
    for i in sample:
        
        training_indices = [j for j in range(X.shape[0]) if j != i]
        W = SgdLogistic(X[training_indices,], Y[training_indices,], maxIter=maxIter, lmda=lmda, learningRate=learningRate)
        
        
        y_hat = np.sign(X[i,].dot(W))

        if y_hat == Y[i]:
            nCorrect += 1
        else:
            nIncorrect += 1

    
    return (nCorrect / (nCorrect + nIncorrect), W)

    

def Accuracy(X, Y, W):
    Y_hat = np.sign(X.dot(W))
    correct = (Y_hat == Y)
    return float(sum(correct)) / len(correct)

def main():
    maxFeatures =  max([data[i][0].flatten().shape[0] for i in range(data.shape[0])])

    #Inputs
    X = np.zeros((ntrials, maxFeatures+1))
    for i in range(data.shape[0]):
        f = data[i][0].flatten()
        X[i,:f.shape[0]] = f
        X[i,f.shape[0]]  = 1     #Bias

    #Outputs (+1 = Picture, -1 = Sentence)
    Y = np.ones(ntrials)
    Y[np.array([info[i]['firstStimulus'][0] != 'P' for i in range(ntrials)])] = -1

    #Randomly permute the data
    np.random.seed(1)      #Seed the random number generator to preserve the dev/test split
    permutation = np.random.permutation(ntrials)
    permutation = np.random.permutation(X.shape[0])
    X = X[permutation,]
    Y = Y[permutation,]

    X_train = X[:40]
    X_test = X[40:]

    Y_train = Y[:40]
    Y_test = Y[40:]

    # print("number of data instances: ", X.shape)
    # print("number of data instances: ", Y.shape)


    #Cross validation
    
    #----------------Logistic Loss-----------------------------------
    
    #Development
    dev_accuracy , W_logistic = TrainLogisitcRegression(X_train, Y_train,  maxIter=100, lmda=0.1, learningRate=0.0001, sample=range(20))
    test_accuracy = Accuracy(X_test, Y_test, W_logistic)
    print("Accuracy Logistic Regression dev set: ", dev_accuracy )
    print("Accuracy Logistic Regression test set: ", test_accuracy )
    
    
    
    







if __name__ == "__main__":
    main()
