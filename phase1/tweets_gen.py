from twython import Twython, TwythonAuthError
import sys
import json
import sys; sys.path.append('/Library/Python/2.7/site-packages/pattern')
from pattern.en import sentiment, positive
import goslate
import re
reload(sys)
from dateutil.tz import *
sys.setdefaultencoding("utf-8")
myApi=Twython('Ic8lLpnaJKhrBuVmzT2hoQdG7', \
              '3vk8ItYR8wnTrnKMyNXrgoM9KQllHxYDCFNyS66L13fwHRgvPu', \
              '16538561-Hkh2L2wrnYHRpLS6V5TbGrLTuOLRZAM0mLDlFyy6l', \
              'bmjomV1KynrrOympM6kTAgnOOukOcdhmIl7Kl0pv5A88l')

#Calculating API Recall, Quality precision, Quality recall
sent_list=[]
def getting_tweets():
    #Calculating Random Sample for a domain
    query = '(crime OR misconduct OR felony OR offense OR misdeed\
            OR misdeed OR murder OR kill OR assassinate OR kidnap OR homicide OR rape OR assault)'
            #theft OR robbery OR burglary OR drugs OR decrease OR less OR decline OR reduce OR drop OR descend) OR (policy OR approach OR rule OR law)'
    geo = ('64.2008','149.4937','10000mi') #Alaska
    #texas '-94.9027','29.3838'
    # washington '38.889931', '-77.009003'
    # arkansas '34.44', '-92.1700'
    Max_id = None
    final_tweets = []
    for i in range(10):
        #tweets = [json.loads(str(raw_tweet)) for raw_tweet  in\
        raw_tweets=myApi.search(q=query, geo=geo, count = 10)# max_id = Max_id)
        for i,v in enumerate(raw_tweets['statuses']):
            data2=v
            tweets=re.sub(r"http\S+","",data2['text'])
        #Max_id = min([t['id'] for t in raw_tweets['statuses']]) - 1
        final_tweets.append(tweets)

    print len(final_tweets)
    '''for items in final_tweets:
        if positive(items,threshold=0.05)=='true':
            sent_list.append(1)
        else:
            sent_list.append(0)

    print len(sent_list)'''

    fdata=open("sentiments.txt","w")
    ctr=1
    for text, item in zip(final_tweets,sent_list):
        fdata.write("[")
        fdata.write(ctr)#str(sent_list[item]))
        fdata.write(","+"\"")
        fdata.write(str(text)+"\\n"+"\"")
        fdata.write("]")
        fdata.write("\n")
        ctr+=1

def main():
    getting_tweets()
    gs=goslate.Goslate()
    for line in open("sentiments.txt").readlines():
        print (gs.translate(line,'en'))

if __name__ == '__main__':
    main()
