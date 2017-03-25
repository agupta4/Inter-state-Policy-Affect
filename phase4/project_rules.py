##################################  PROJECT CODE (ABHISHEK GUPTA MANAS GAUR) ######################################
####### Main part of this code is :
####### ABHISHEK GUPTA - ASSOCIATION RULE MINING and MANAS GAUR - FREQUENT PATTERN TREE

import json
import Orange
from nltk.sentiment import SentimentIntensityAnalyzer
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

sid=SentimentIntensityAnalyzer()
raw_tweets = []
new_tweets = []
keywords = ["crime", "kill", "murder", "drugs", "homicide", "harass", "illegal", "rape", "assault", "kidnap"]

for tweet in open("cluster-4.txt").readlines():
    new_tweets.append(json.loads(tweet))

lst = []
c = 0

for tweet in new_tweets:
    line = tweet[0]
    line = line.lower()
    count = 0
    ss = sid.polarity_scores(line)
    new_lst = line.split()
    for l in keywords:
        for x in new_lst:
            if x == l:
                if count == 0:
                    lst.append(ss["neg"])
                    count += 1
                else:
                    pass
                c = c + 1

#print c
#Applying mean-twice standard deviation rule
nmp_array = np.asarray(lst, dtype = list)
mean = np.mean(nmp_array)
std_dev = np.std(nmp_array)
print "mean = {0}, std_dev = {1}".format(mean, std_dev)
threshold = mean - 2*std_dev
print "threshold: {0}".format(threshold)

for tweet in new_tweets:
    line = tweet[0]
    line = line.lower()
    str = ""
    prev_Str = ""
    count = 0
    new_list = []
    ss = sid.polarity_scores(line)
    if ss["neg"] > threshold:   #Value should be greater than threshold as this lie b/w q1 and q3
        lst = line.split()
        for l in keywords:
            for x in lst:
                if x == l:
                    if prev_Str != x:
                        str = str + x
                        new_list.append(x)
                        count = count + 1
                        prev_Str = x
    if(len(str) > 1):
        new_list.append(ss["neg"])
        raw_tweets.append([new_list, tweet[1]])
print "Out of {0} tweets which satisfy threshold {1} are {2} for crime related tweets".format(c, threshold, len(raw_tweets))
print raw_tweets
#### all the labels have been identified by converting the list to Set and then back to list
state_label={"Washington": 0, "Alaska": 1, "Mexico": 2}
crime_label={"murder": 0, "drugs": 1, "illegal": 2, "crime": 3, "assault": 4, "kill": 5, "rape": 6}
print state_label["Washington"]
data_w=np.zeros(7)
data_a=np.zeros(7)
for i1,i2 in raw_tweets:
    if len(i1)>2:
        if state_label[i2]==0:
            data_w[crime_label[i1[0]]]+=i1[2]/2
            data_w[crime_label[i1[0]]]+=i1[2]/2
        else:
            data_a[crime_label[i1[0]]]+=i1[2]/2
            data_w[crime_label[i1[0]]]+=i1[2]/2
    else:
        if state_label[i2]==0:
            data_w[crime_label[i1[0]]]+=i1[1]
        else:
            data_a[crime_label[i1[0]]]+=i1[1]

print data_a[:]
'''
ind=np.arange(7)
width=0.5
p1=plt.bar(ind, data_a[:], 0.5, color='r')
p2=plt.bar(ind, data_w[:], 0.5, color='g')
plt.ylabel('Crimes')
plt.title('Crime based labeling')
plt.xticks(ind + width/2., ("murder", "drugs", "illegal", "crime", "assault", "kill", "rape"))
plt.yticks(np.arange(0, 50, 5))
plt.legend((p1[0], p2[0]), ('Washington', 'Alaska'))

plt.show()
#df=pd.DataFrame(raw_data, columns=['States', 'Category_Crime', 'Values'])
'''

#Crime=set(Crime)
#Crime=list(Crime)
#print Crime
keywords2 = ["policy", "law"]
#keywords3 = ["environmental", "foreign", "health"]
lst = []
c = 0
for tweet in new_tweets:
    line = tweet[0]
    line = line.lower()
    count = 0
    ss = sid.polarity_scores(line)
    new_lst = line.split()
    for l in keywords2:
        for x in new_lst:
            if x == l:
                if count == 0:
                    lst.append(ss["pos"])
                    count += 1
                else:
                    pass
                c = c + 1
#print c
#Applying mean-twice standard deviation rule
nmp_array = np.asarray(lst, dtype = list)
mean = np.mean(nmp_array)
std_dev = np.std(nmp_array)
print "mean = {0}, std_dev = {1}".format(mean, std_dev)
threshold = mean + 2*std_dev
print "threshold: {0}".format(threshold)
raw_tweets1 = []

for tweet in new_tweets:
    line = tweet[0]
    line = line.lower()
    str = ""
    prev_Str = ""
    count = 0
    new_list = []
    ss = sid.polarity_scores(line)
    if "environmental" in line or "health" in line or "foreign" in line:
        ss["pos"]=1
    if ss["pos"] < threshold:   #Value should be less than the threshold as we are considering tweets between Q1 and Q3
        lst = line.split()
        for l in keywords2:
            for x in lst:
                if x == l:
                    if prev_Str != x:
                        str = str + x
                        new_list.append(x)
                        count = count + 1
                        prev_Str = x
    if(len(str) > 1):
        new_list.append(ss["pos"])
        raw_tweets1.append([new_list, tweet[1]])
print "Out of {0} tweets which satisfy threshold {1} are {2} for policy related tweets".format(c, threshold, len(raw_tweets1))
print raw_tweets1
#policy = {"kill":0, "Crime": 1}
'''
data_w=np.zeros(7)
data_a=np.zeros(7)
data_w[0:2]=0.5
data_a[0:2]=1.0
data_w[2]=data_a[2]=0.107
c=0
for i1,i2 in raw_tweets1:
    if len(i1)==2:
        if state_label[i2]==0 and (c%2==0) :
            data_w[crime_label["kill"]]+=i1[1]
            data_w[crime_label["crime"]]+=0.05
        else:
            data_a[crime_label["crime"]]+=i1[1]
            data_a[crime_label["kill"]]+=0.05
    #else:
     #   data_crime[crime_label["crime"]]+=i1[2]/2
      #  data_kill[crime_label["kill"]]+=i1[2]/2
    c+=1
x=np.arange(7)
data_policy=np.zeros(7)
#data_kill[3]= data_crime[3]/2
#data_crime[5]=data_kill[5]/2
print data_w
print data_a
width=0.5
p1=plt.bar(x, data_w[:], 0.5, color='b')
p2=plt.bar(x, data_a[:], 0.5, color='r')
plt.ylabel('policy')
plt.title('Policy based crime labeling')
plt.xticks(x + width/2., ("Texas", "Arkansas", "Mexico", "Washington", "New Mexico", "Alaska", "Albany"))
plt.yticks(np.arange(0, 20, 2))
plt.legend((p1[0], p2[0]), ('Kill', 'Crime'))
plt.show()
'''
#print data_crime
#print data_kill
raw_tweets3 = []
for tweet1 in raw_tweets:
    #x is list
    x = tweet1[0]
    s1 = ""
    c1 = 0
    for item in x:
        if type(item) != type(0.1):
            item = item.encode('ascii','ignore')
        if type(item) == type(""):
            if c1 == 0:
                s1 = s1 + item
                c1 = c1+1
            else:
                s1 = s1 + "," +item
                c1 = c1+1
        else:
            neg_val = -1 * item
    for tweet2 in raw_tweets1:
        final_str = ""
        #y is list
        y = tweet2[0]
        s2 = ""
        c2 = 0
        for item1 in y:
            if type(item1) != type(0.1):
                item1 = item1.encode('ascii','ignore')
            if type(item1) == type(""):
                if c2 == 0:
                    s2 = s2 + item1
                    c2 = c2+1
                else:
                    s2 = s2 + "," +item1
                    c2 = c2+1
            else:
                pos_val = item1
        final_val = pos_val + neg_val
        if final_val > -0.1 and final_val < 0.1:
            final_str = s1 + "," + s2 + "," + tweet1[1] + "," + tweet2[1]
            raw_tweets3.append(final_str)
#Final Relation is as follows

raw_data = raw_tweets3
f = open('data1.basket', 'w')
for item in raw_data:
    f.write(item + '\n')
f.close()

# Load data from the text file: data.basket
data = Orange.data.Table("data1.basket")


# Identify association rules with supports at least 0.3
rules = Orange.associate.AssociationRulesSparseInducer(data, support = 0.2, confidence = 0.2)
rule=rules[0]

ind = Orange.associate.AssociationRulesSparseInducer(support = 0.2, storeExamples=True)
f = open('rules.txt', 'w')
# print out rules
print "%4s %4s  %s" % ("Supp", "Conf", "Rule")
for r in rules[:]:
    print "%4.1f,%s,%4.1f" % (r.support,r, r.confidence)
    #f.write(([r.support, r.confidence, r])+'\r\n')
itemsets = ind.get_itemsets(data)
#print itemsets
for itemset, tids in itemsets:
    print "(%4.2f) %s" % (len(tids)/float(len(data)),
                          " ".join(data.domain[item].name for item in itemset))