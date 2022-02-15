from  activation_fun import Activation_Sigmoid
import numpy as np
import pickle 

class prediction():
    def __init__(self,inputs):
        with open ("model.dat","rb") as f :
            file = pickle.load(f)
            weights= file['weights']
            self.weights1 = weights['weights1']
            self.weights2 = weights["weights2"]
        self.inputs = inputs

    def test_forward(self):
        layer1 = np.dot(self.inputs,self.weights1)
        Act_sigmoid = Activation_Sigmoid()
        Act_sigmoid.forward(layer1)
        hidout = Act_sigmoid.output

        layer2 = np.dot(hidout.T,self.weights2)
        Act_sigmoid = Activation_Sigmoid()
        Act_sigmoid.forward(layer2)
        prediction = Act_sigmoid.output
        probs =[np.sum(i*100) for i in prediction]
        probs.sort()
        probs = probs[::-1]


        #expected = pickle.load(open("classes.dat","rb"))
        #error = np.abs(prediction - expected)
        return prediction,probs
# model = prediction(X)
# preds = model.test_forward()

# [[1,0,1],[0,1,1],[0,0,0]]