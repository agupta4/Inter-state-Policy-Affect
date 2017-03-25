# -*- coding: utf-8 -*-
"""
Created on Sat May 07 16:18:46 2016

@author: ETHICAL DRUIDS
"""
#This section classifies on the basis of crime
import json
from sklearn.linear_model import LogisticRegression
from nltk.sentiment import SentimentIntensityAnalyzer
sid=SentimentIntensityAnalyzer()
tweets = []
for line in open("cluster-4.txt").readlines():
    tweets.append(json.loads(line))
    
vocab = {"crime":0, 
        "kill":1, 
        "murder":2, 
        "drugs":3, 
        "homicide":4, 
        "harass":5, 
        "illegal":6, 
        "rape":7, 
        "assault":8, 
        "kidnap":9,
        "corruption:":10}
y = []
X = []
for tweet in tweets:    
    x = [0,0,0]
    text = tweet[0]
    text = text.lower()    
    ss = sid.polarity_scores(text)
    x[0] = ss['neg']
    x[1] = ss['pos']
    x[2] = ss['neu']
    terms = [term for term in text.split() if len(term) > 2]
    for term in terms:
        if vocab.has_key(term):
            y.append(vocab[term])   #Defining labels on the basis of vocab
            X.append(x)
            break
print "X: {0}, y:{1}".format(len(X), len(y))

#Train the data according to feature vector X
clf = LogisticRegression()
clf.fit(X,y)
score = clf.score(X, y)
