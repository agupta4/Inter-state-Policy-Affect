# -*- coding: utf-8 -*-
import re
import json

try:
    # Wide UCS-4 build
    myre = re.compile('['
        u'\U0001F300-\U0001F64F'
        u'\U0001F680-\U0001F6FF'
        u'\u2600-\u26FF\u2700-\u27BF]+', 
        re.UNICODE)
except re.error:
    # Narrow UCS-2 build
    myre = re.compile(u'('
        u'\ud83c[\udf00-\udfff]|'
        u'\ud83d[\udc00-\ude4f\ude80-\udeff]|'
        u'[\u2600-\u26FF\u2700-\u27BF])+', 
        re.UNICODE)

tweets = []
for line in open('data.txt').readlines():
    tweets.append(json.loads(line))
f = open('cluster-4.txt', 'a')
for text in tweets:
    print text
    text = ' '.join(re.sub("(@[A-Za-z0-9]+)|(\w+:\/\/\S+)"," ",text).split())
    f.write(json.dumps([myre.sub('',text), "Alaska"]))
    f.write("\r\n")
f.close()