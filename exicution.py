import time
from text_speech import *
from actions1 import *
import random 
import json
import pickle as pickle
import numpy as np
from model_run import prediction
import nltk 
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
nlu =  json.loads(open("data.json").read())
words  =  pickle.load(open("words.dat","rb"))
classes  =  pickle.load(open("classes.dat",'rb'))
model = pickle.load(open("model.dat","rb"))
print(classes)

def set_of_actions(actions):
    if actions == "show_zoom":
        act = show_zoom()
        act.run()
    elif actions == "google_it":
        act = google_it()
        act.run()

def clean_up_sentence(sentence):
    sentence = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence]
    return sentence_words

def bag_of_words(sentence):
    sentence_words =  clean_up_sentence(sentence)
    bag = [0]* len(words)
    for w in sentence_words:
       if w in words: bag[words.index(w)] = 1 
    return np.array(bag)

def predict_class(sentence):
    bow = bag_of_words(sentence)
    model = prediction(bow)
    res,probs = model.test_forward()
    Error_threshold = 0.75
    print(f"result : {res}")
    results={}
    # for i,r in enumerate(res):
    #     if r > Error_threshold:
    #         d[r]=i
    # print(results)

    # results=results[::-1]
    return_list = []
    res = list(res)
    n = res.index(max(res))
    if max(res)*100 <=40:
        print("Please try again !")
    
    else:
        return_list.append({'tags': classes[n], 'probability': probs})
        return return_list

def get_response(return_list, nlu_json):
    tag = return_list[0]['tags']
    nlu = nlu_json['nlu']
    actions = []
    for i in nlu:
        if i['tag'] == tag:
            response = random.choice(i['responses'])
            if i["actions"]!= []:
                actions.append(random.choice(i["actions"]))
            break
    return response,actions
print("GO! Bot is running!")

while True:
    print("The bot's started")
    speech = Stealth_listening()
    prompt =  speech.run()
    print(prompt)
    if "mike" in prompt.lower():
        command = SpeechToText()
        message = command.run()
        return_list = predict_class(message)
        if return_list == None: continue
        response,actions = get_response(return_list,nlu)
        print(f"bot : {response}")
        resp = TextToSpeech(response)
        resp.run()
        # print(actions)
        if actions != []:
            set_of_actions(actions[0])
        time.sleep(3)