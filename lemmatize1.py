
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import json
import pickle
import csv
import random
import numpy as np
data = json.loads(open("data.json").read())

words = []
classes = []
documents = []
ignore_letters = ["?",".","!",","]

for intent in data['nlu']:
    for pattern in intent['intents']:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list,intent['tag']))
        if  intent['tag'] not in classes:
            classes.append(intent['tag'])

words = [lemmatizer.lemmatize(word) for word in words if word not in ignore_letters]  
words = sorted(set(words))

pickle.dump(words,open("words.dat",'wb'))
pickle.dump(classes,open("classes.dat",'wb'))

training = []

for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns ]
    for word in words: 
        bag.append(1) if word in word_patterns else bag.append(0)

    output_row = [0]* len(classes)
    output_row[classes.index(document[1])]=1

    training.append([bag, output_row])

random.shuffle(training)
#print(training)
train_x = np.array([i[0] for i in training ])
train_y = np.array([i[1] for i in training])

print(f"train_x = {train_x}")
print(f"train_y = {train_y}")

class AI_learning():
    def __init__(self,train_x,train_y):
        self.inputs = train_x
        self.expected = train_y
data = AI_learning(train_x, train_y)
# print(np.array(training))
#training = np.array(training)
#print(training)
# train_x = list(training[:,0])
# train_y = list(training[:,1])
























# nlu_data = open("data.json").read()
# data = json.loads(nlu_data)
# for val in data['nlu']:
#     l1=[]
#     for intent in val["intents"]:
#         w = nltk.word_tokenize(intent)
#         intents.extend(w)
#         l1.extend(w)
#         #domain.append((val['tag'],intents))
#         if val['tag'] not in tags:
#             tags.append(val['tag'])
#     domain.append((val['tag'],l1))
#     # print(domain)

# # print(f"h = {h}\n\n\n\
# #     domain = {domain}")
# print(f"domain = {domain}")




# # lemmatizatiion
# intents = [lemmatizer.lemmatize(w.lower()) for w in intents if w not in ignore_words]
# intents =  sorted(list(set(intents)))
# tags = sorted(list(set(tags)))
# # with open('intent.csv','w') as f:
# #     writer = csv.writer(f)
# #     writer.writerow(intents)
# # with open("intent.csv",'r') as f:
# #     reader = csv.reader(f)
# #     r=[]
# #     for i in reader:
# #         r.append(i)
# # a=[]
# # for i in r:
# #     # print(i)
# #     # print(i)
# #     a.append(i)
# # for i in a:
# #     print(i)

# # # Bag of words
# # domain_bag = []
# # output_bag = []
# # patterns = [0]* len(tags)
# # print(patterns)
# # for i in tags :
# #     print(tags.index(i))
# #     patterns[tags.index(i)] = 1 if i in tags else print ("none")
# #     val = [0]* len(intents)
# #     for j in domain:
# #         for k in j[1]:
# #             if k in intents:
# #                 val[intents.index(k)]=1
# #         domain_bag.append((j[0],val))
# #         val = [0]* len(intents)

# #     print(patterns)
# #     output_bag.append(patterns)


# # print("pattern" + " =", patterns)
# # print(domain)
# # print(output_bag)
# # print(f"domian_bag = {domain_bag}")