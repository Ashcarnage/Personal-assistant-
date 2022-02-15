from lemmatize1 import data
from activation_fun import Activation_ReLU, Activation_Sigmoid, Activation_SoftMax
import numpy as np
import pickle
np.random.seed(43)

# X = [[1,0,0,1],
#      [0,0,1,1],
#      [1,1,0,1]] 
X = data.inputs
Y = data.expected

class Layer_Dense:
    def __init__(self,n_inputs,n_neurons):
        self.weights = np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1,n_neurons))
    def forward(self,inputs):
        self.output = np.dot(inputs, self.weights) + self.biases


class Forward_Propagation():
    def __init__(self,layers,inputs,Y):
        self.layers=layers
        self.inputs=inputs
        self.expected = Y
    def propagate(self):
        self.weight_bag = {}
        self.X = self.inputs
        for i in range(self.layers):
            if i ==0: 
                layer1 = Layer_Dense(len(self.inputs[0]),164)
            else:
                layer1 = Layer_Dense(164,len(self.expected[0]))
           # print(f"\nweights = {layer1.weights}\n")
            if i==0:
                self.weight_bag["weights1"] = layer1.weights
            else:
                self.weight_bag["weights2"] = layer1.weights
            layer1.forward(self.X)
           # print(f"output = {layer1.output}")
            Act_sigmoid= Activation_Sigmoid()
            Act_sigmoid.forward(layer1.output)
            self.X = Act_sigmoid.output.T
            if i==0:
                hidout = self.X 
              #  print(f"HIDDEN LAYER : {hidout}")

        return {'output': np.array(self.X),'hidden_output': np.array(hidout) ,'weights':self.weight_bag, "inputs": self.inputs}

def sigmoid_dev(output):
    return output*(1-output)
 
class Back_proagation():
    def __init__(self,network1,expected):
        n1 = network1["weights"]
        self.weights1 = n1["weights1"]
        self.weights2 = n1["weights2"]
        self.expected = expected
        self.hidden = network1["hidden_output"]
        self.output = network1["output"]
        self.learning_rate = 0.01
        self.inputs1 = np.array(network1["inputs"])
    def backwardpropagation(self): 
        #print(self.output)
        error = self.expected - self.output
        # print(f"self.output : {self.output}")
        # print(error)
        dev_output = error*sigmoid_dev(self.output)
        # print(f"sigmoid : {sigmoid_dev(self.output)}")
        # print(f"dev_output  : {dev_output}")
        adj_weights2 = np.dot(self.hidden.T,dev_output) * self.learning_rate 
    

        dev_input = np.dot(dev_output,self.weights2.T)*sigmoid_dev(self.hidden)
        #print(f"dev_input : {dev_input}\n")
        adj_weights1 = np.dot(self.inputs1.T,dev_input) * self.learning_rate
        # print(f"self.inputs  :  {self.inputs1}")
        # print(f"weights1 before : {self.weights1}")
        # print(f"adj_weight1 : {adj_weights1}")
        # print(f"weight2 before : {self.weights2}")
        # print(f"adj_weights2 : {adj_weights2}")

        self.weights1 += adj_weights1
        self.weights2 += adj_weights2
        #print(f"new weights1  : {self.weights1}\nnew weights2 : {self.weights2}")

        #print(f"hidden layer  : {self.hidden}")#\n{self.output}\n{np.dot(self.hidden,self.output)}")
        # print(f"\n adjweights2 : {adj_weights2}")

        # print(f"adj_weights-1  : {adj_weights1.T} ")
        # print(f"weights1  : {self.weights1}")
        # print(f'adj_weights-2  : {adj_weights2}')
        # print(f"weights2  : {self.weights2}")
        # print(f"Output :  {self.output}")

        # print(f"dev_input : {dev_output}\nweights2 : {self.weights2.T}\n dot product : imp value :  {np.dot(dev_output,self.weights2.T)}\n hidden : {self.hidden}")
        # print(f"Adjustement of weights :  {dev_input}")
network = Forward_Propagation(2,X,Y)
network1=network.propagate()
bp = Back_proagation(network1,Y)
bp.backwardpropagation()
#print(f"OUTPUTTTTT-1  : {bp.output}\n")
class network_training():
    def __init__(self,inputs,epochs,bp):
        self.inputs = inputs
        self.epochs = epochs
        self.weights1 = bp.weights1
        self.weights2 = bp.weights2
    def TrainModel(self):
        for epoch in range(self.epochs):   
            # LAYER 1
            layer1 = np.dot(self.inputs,self.weights1)
            Act_sigmoid = Activation_Sigmoid()
            Act_sigmoid.forward(layer1)
            hidout = Act_sigmoid.output
            # LAYER 2
            layer2 = np.dot(hidout.T,self.weights2)
            Act_sigmoid = Activation_Sigmoid()
            Act_sigmoid.forward(layer2)
            output = Act_sigmoid.output

            weights = {'weights1' : self.weights1, "weights2" : self.weights2}
            network1 = {'output': np.array(output).T,'hidden_output': np.array(hidout).T ,'weights':weights, "inputs": self.inputs}
            bp = Back_proagation(network1,Y)
            bp.backwardpropagation()

            if epoch % 19000 == 0:
                print(f"FINAL OUTPUT  : {output.T}\n")

        with open ("model.dat", 'wb') as f:
            pickle.dump(network1,f)

        return weights

training = network_training(X,1800000,bp)
model = training.TrainModel()
# def test_forward(pred_input,model):
#     weights1 = model["weights1"]
#     weights2 = model["weights2"]
#     layer1 = np.dot(pred_input,weights1)
#     Act_sigmoid = Activation_Sigmoid()
#     Act_sigmoid.forward(layer1)
#     hidout = Act_sigmoid.output

#     layer2 = np.dot(hidout.T,weights2)
#     Act_sigmoid = Activation_Sigmoid()
#     Act_sigmoid.forward(layer2)
#     prediction = Act_sigmoid.output
#     print(prediction)
# # Y = [[1,0,0,0],
# #      [0,1,1,1],
# #      [1,1,1,1]] 

# test_forward(Y, model)