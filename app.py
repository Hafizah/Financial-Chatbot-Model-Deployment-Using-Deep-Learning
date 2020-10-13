#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask,request, url_for, redirect, render_template,jsonify,make_response
import json
import numpy as np
from tensorflow.keras.models import load_model
import random
import nltk
nltk.download('punkt')

app = Flask(__name__)
def bag_of_words(s, words):
    bag = [0 for _ in range(len(words))]

    s_words = nltk.word_tokenize(s)
    s_words = [stemmer.stem(word.lower()) for word in s_words]

    for se in s_words:
        # adds a counter to an iterable and returns it in a form of numbered object
        for i, w in enumerate(words):
            if w == se:
                bag[i] = 1
            
    return np.array(bag)


import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import json
with open('Chatbot_Intents.json') as file:
  data=json.load(file)
# In[4]:




# consist of unique stemmed words/tokens from patterns extended in this list. No duplicates
words = []
# consist of tag words from intent
labels = []
# consist of tokenized sentences from patterns appended in this list
doc_x = []
# consists of tag words from intent matching tokens in doc_x
doc_y = []

# loop through each sentences in the data/intent
for intent in data['intents']:
    # loop through each sentences in patterns in intent
    for pattern in intent['patterns']:
        # tokenize each words in the pattern in intent
        wrds = nltk.word_tokenize(pattern)
        # method iterates over its argument adding each element to the list by extending the list
        words.extend(wrds)
        # method adds its argument as a single element to the end of a list. Length of the list increase by one
        doc_x.append(wrds)
        doc_y.append(intent['tag'])
        
    if intent['tag'] not in labels:
        labels.append(intent['tag'])

# stems and lower case the words 
words = [stemmer.stem(w.lower()) for w in words if w != '?']
 
# set() removes duplicates, list() change into a list and sorted() sort in ascending order
words = sorted(list(set(words)))

labels = sorted(labels)

model=load_model('final_model.h5')
@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
def predict():
      while True:
        # prompt user to respond
        userInput = request.form['name']
            
              
        # predict the correct label given user input and comparing it to the words in pattern of intent 
        results = model.predict(bag_of_words(userInput, words).reshape(-1,468))
        # returns the indices of the maximum values along an axis
        results_index = np.argmax(results)
        # return the label(tag) that best match the user input   
        user_tag = labels[results_index]
        #print(results.max()) # -- shows the highest probability for each chosen tag

        
        # condition set - only result with probability more than 0.85 will be considered correct respond
        if results.max() > 0.85 :
        # prints out the responses form matching tag randomly
            for tag_selection in data['intents']:
                if tag_selection['tag'] == user_tag:
                    responses = tag_selection['responses']
            data1=random.choices(responses)
            resp = make_response(json.dumps(data1))
            resp.status_code = 200
            resp.headers['Access-Control-Allow-Origin'] = '*' 
            return resp
        
        # user input with probability < 0.85, will get this message
        else:
            data1="Sorry I didn't get that. Please try again or go to https://worlddatascience.tech/datapedia for more assistance"
            resp = make_response(json.dumps(data1))
            resp.status_code = 200
            resp.headers['Access-Control-Allow-Origin'] = '*' 
            return resp
         
    

if __name__ == '__main__':
    app.run(port='5000',debug=False)


