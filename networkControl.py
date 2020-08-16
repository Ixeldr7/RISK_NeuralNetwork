import math
import numpy as np


class neuralNetwork(object):

    def feedForward(self, trainingSet):
        #multiplies input data by the random weights
        self.a = np.dot(trainingSet, self.randomWeights1)
        #uses an activation function
        self.a2 = 1.0 / (1.0 + np.exp( - self.a))
        #multiplies the hidden layer values by a second set of random weights
        self.a3 = np.dot(self.a2, self.randomWeights2)
        #assigns output values
        output = 1.0 / (1.0 + np.exp( - self.a3))
        return output

    #calculates error based on desired outputs
    def backPropagate(self, trainingSet, desiredOutput, output):
        #calculates base error output
        self.outputError = desiredOutput - output
        #calcualtes the derivate to show the rate of change of the activation function
        self.outputError2 = self.outputError * (output * ( 1 - output))

        #calculates error for hidden layer weights
        self.a2error = self.outputError2.dot(self.randomWeights1.T)
        #calcualtes the derivate to show the rate of change of the activation function
        self.a2error2 = self.a2error * (self.a2 * ( 1 - self.a2))

        #adjusts weights according to error calculations
        #adjusts first set of weights
        self.randomWeights1 += trainingSet.T.dot(self.a2error2)
        #adjusts second set of weights
        self.randomWeights2 += self.a2.T.dot(self.outputError2)
        
    
    def trainNetwork(self, trainingSet, desiredOutput):
        output = self.feedForward(trainingSet)
        self.backPropagate(trainingSet, desiredOutput, output)
                                   

    def useNetwork(self, data):
        print("Using Network")
        output = self.feedForward(data)
        return output
                           

    def __init__(self):
        #initialise variables

        #set the number of nodes for each layer
        self.inputNodes = 4
        self.hiddenNodes = 4
        self.outputNodes = 4

        #assign random weights
        #np.random.randn creates an array within the shape of provided int like args
        self.randomWeights1 = np.random.randn(self.inputNodes, self.hiddenNodes)
        self.randomWeights2 = np.random.randn(self.hiddenNodes, self.outputNodes)


    
                           
