import numpy as np 
import math
#from neural_net import Layer_Dense
# inputs = [[0,21,-1,3.3,-2.7],
#           [2,-3,4, -2.2, 3]]
# a= Activation_ReLU()
class Activation_ReLU():
  def forward(self,inputs):
      self.output = []
      for i in inputs:
          L = []
          for j in i:
            L.append(max(0,j))
          self.output.append(L)
      
class Activation_SoftMax():
  def forward(self,inputs):    
    # for j in inputs:
    #   L = []
    #   for i in j:
    #     L.append(math.e**i)
    #   exp_values.append(L)
    exp_values =np.exp(inputs - np.max(inputs,axis=1,keepdims=True))
    # Normalization (finding prbability)
    probabilities= exp_values/np.sum(np.array(exp_values).T,axis=1)
    self.output = probabilities


#inputs = [[4.8,1.21,2.385],[5,-6.2,2]]

class Activation_Sigmoid():
  def forward(self,inputs):
    self.output = 1/(1+ math.e**(-np.array(inputs).T))

