# -*- coding: utf-8 -*-
"""
Created on Sat May 07 19:17:12 2016

@author: ETHICAL DRUIDS
"""
#This section classifies on the basis of state
import json
from sklearn.linear_model import LogisticRegression
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn import svm
import numpy as np
from matplotlib import pyplot as plt
from sklearn import cross_validation
from sklearn.cluster import KMeans
from scipy.spatial.distance import cdist

sid=SentimentIntensityAnalyzer()
tweets = []
for line in open('cluster-4.txt').readlines():
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
State = {'Washington' : 0, 'Alaska': 1, 'Mexico': 2}
policy = ['policy', 'law']
#class-label->state, feature vector->ss
X = []
y = []
for tweet in tweets:
    text = tweet[0]
    city = tweet[1]
    text = text.lower()
    x = [0,0,0]
    ss = sid.polarity_scores(text)
    x[0] = ss['neg']
    x[1] = ss['pos']
    x[2] = ss['neu']
    if any(term in text for term in policy) and ("environmental" or "health" or "foreign" or "non cooperation") not in text:
        terms = [term for term in text.split() if len(term) > 2]
        for term in terms:
            if (term == policy[0] or term == policy[1]) and ss['neg'] >= 0.12:
                y.append(State[city])
                X.append(x)
                break
print X
X_train, X_test, Y_train, Y_test = cross_validation.train_test_split(X,y,test_size=0.5, random_state=0)
#for items in X:
 #   print items

clf = LogisticRegression()#svm.SVC(kernel='linear',C=1.0)
#Cs = range(1, 10)
#clf = GridSearchCV(estimator=clf, param_grid=dict(C=Cs), cv = 10)
clf.fit(X_train,Y_train)
print clf.score(X_test,Y_test)
print clf.predict(X_test)

K_val=np.arange(2,51,1)
S_list=[]
for k in K_val:
    kmeans = KMeans(n_clusters = k)
    y=kmeans.fit_predict(X)
    S_list.append(sum(np.min(cdist(X, kmeans.cluster_centers_,'euclidean'),axis=1))/np.asarray(X).shape[0])
plt.plot(K_val.tolist(),S_list)
plt.show()
print np.median(np.asarray(S_list))
index=np.where(np.asarray(S_list)==np.median(np.asarray(S_list)))#K_val.max()
print index
k=10
km = KMeans(n_clusters = k, n_init = 100) # try 100 different initial centroids
class_labels=km.fit_predict(np.asarray(X))
centroids=km.cluster_centers_
idx=class_labels
for items,tweets in zip(class_labels,X):
    print tweets, ":", items

X=np.asarray(X)
print X
colors=np.random.rand(k)
fig=plt.figure()
plt.scatter(X[:,0],class_labels,c=colors, alpha=0.5)
plt.xlabel('negative_sentiments', fontsize=18)
plt.ylabel('clusters', fontsize=16)
plt.show()
fig=plt.figure()
plt.scatter(X[:,1],class_labels,c=colors, alpha=0.5)
plt.xlabel('postive_sentiments', fontsize=18)
plt.ylabel('clusters', fontsize=16)
plt.show()
fig=plt.figure()
plt.scatter(X[:,2],class_labels,c=colors, alpha=0.5)
plt.xlabel('neutral_sentiment', fontsize=18)
plt.ylabel('clusters', fontsize=16)
plt.show()
