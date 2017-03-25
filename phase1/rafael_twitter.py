from twython import Twython, TwythonAuthError
import sys
import json
import sys; sys.path.append('/Library/Python/2.7/site-packages/pattern')
from pattern.en import sentiment, positive
reload(sys)
from dateutil.tz import *
sys.setdefaultencoding("utf-8")
myApi=Twython('Ic8lLpnaJKhrBuVmzT2hoQdG7', \
              '3vk8ItYR8wnTrnKMyNXrgoM9KQllHxYDCFNyS66L13fwHRgvPu', \
              '16538561-Hkh2L2wrnYHRpLS6V5TbGrLTuOLRZAM0mLDlFyy6l', \
              'bmjomV1KynrrOympM6kTAgnOOukOcdhmIl7Kl0pv5A88l')

#Calculating API Recall, Quality precision, Quality recall
def getting_tweets():
    #Calculating Random Sample for a domain
    query = '(crime OR misconduct OR felony OR offense OR misdeed\
            OR misdeed OR murder OR kill OR assassinate OR kidnap OR homicide OR rape OR assault OR\
            theft OR robbery OR burglary OR drugs OR decrease OR less OR decline OR reduce OR drop OR descend) OR (policy OR approach OR rule OR law)'
    geo = ('64.2008','149.4937','1000mi') #Alaska
    #texas '-94.9027','29.3838'
    # washington '38.889931', '-77.009003'
    # arkansas '34.44', '-92.1700'
    Max_id = None
    final_tweets = []
    for i in range(1000):
        #tweets = [json.loads(str(raw_tweet)) for raw_tweet  in\
        raw_tweets=myApi.search(q=query, geo=geo, count = 100)# max_id = Max_id)
        for i,v in enumerate(raw_tweets['statuses']):
            data2=v
            tweets=data2
       # print tweets
        #Max_id = min([t['id'] for t in raw_tweets['statuses']]) - 1
        final_tweets.append(tweets)
    return final_tweets

def rest_query():
    #finding random sample for crime
    final_values = {}

    senti_file=open("sentiments.txt","w")
    R = 1
    M = 1
    N = 1
    A = 1
    B = 1
    C = 1
    keywords = ['crime','Crime', 'misconduct' ,'Misconduct' , 'felony' ,'Felony' , 'offense', 'Offense', 'misdeed' 'Misdeed']
    keywords1 = ['murder','Murder','homicide','Homicide', 'assault', 'Assault', 'killing', 'Killing', 'assassinate', 'Assassinate']
    keywords2 = ['policy','law','approach','rule']
    f = open('AlaskaText.txt','w')
    senti_list=[]
    for it in range(1): # Retrieve up to 1000 tweets
        final_tweets = getting_tweets()
        #f.writelines(str(final_tweets))
        for t in final_tweets:
            print t['text']
            #'''for t in tweets:
            print sentiment(t['text'])
            senti_list.append(sentiment(t['text']))
            dic = {'Tweet_text': t['text'], 'Day': t['created_at']}
            f.write(json.dumps(dic))
            f.write('\n')
            R=R+1
            """
             I am trying to find out any decrease in murder or killing related crimes due to any policy.
            """
            if any(x in t['text'] for x in keywords2):
                C = C+1
            if any(x in t['text'] for x in keywords1):
                N = N+1
                if any(x in t['text'] for x in keywords2):
                     B = B+1
                if ('less' or 'decrease' or 'descend' or 'decline' or 'reduce' or 'drop') in t['text']:
                        M = M+1
                        if any(x in t['text'] for x in keywords2):
                            A = A+1
                            d = {'ID':t['id'],
                                 'user': t['user']['screen_name'],
                                 'Tweet_text': t['text'],
                                 'created_at': t['created_at']
                                }
                            with open('Abhi_random1.txt','a') as file:
                                file.write(json.dumps(d['ID']))
                                file.write('\n')
                                file.write(json.dumps(d['user']))
                                file.write('\n')
                                file.write(json.dumps(d['Tweet_text']))
                                file.write('\n')
                                file.write(json.dumps(d['created_at']))
                                file.write('\n')
                                file.write('***************************')
                                file.write('\n')


    print 'R = %s' %R
    print 'C = %s' %C
    print 'N = %s' %N
    print 'B = %s' %B
    print 'M = %s' %M
    print 'A = %s' %A
    final_values = {'R': R, 'C': C, 'N': N, 'B':B, 'M':M, 'A': A}
    print len(senti_list)
    json.dumps(str(senti_list),senti_file)

    return final_values
    f.close()
    file.close()
def main():
    for i in range(1):
        values = rest_query()
        API_RECALL = values['M']/float(values['N'])
        QUALITY_PRECISION = values['A']/float(values['M'])
        QUALITY_RECALL = values['A']/float((values['A']+values['B']+values['C']))
        print 'API_RECALL = %s' %API_RECALL
        print 'QUALITY_PRECISION = %s' %QUALITY_PRECISION
        print 'QUALITY_RECALL = %s' %QUALITY_RECALL
if __name__ == '__main__':
    main()