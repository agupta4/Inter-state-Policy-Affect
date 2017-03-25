from twython import TwythonStreamer
import json
import datetime
import os

word ='crime OR government OR policy'


class TweetStreamer(TwythonStreamer):
    def on_success(self, data):
        output_folder_date = 'data/{0}'.format(datetime.datetime.now().strftime('%Y_%m_%d'))
        if not os.path.exists(output_folder_date):
            os.makedirs(output_folder_date)

        output_file = output_folder_date+'/NewMexico_1.txt'
        try:
             #print data['text'].encode('utf-8')
             #jdata = json.load(str(data))
             if word in data['text']:
                 f = open(output_file, 'a+')
                 f.write(json.dumps(data['text'].encode('utf-8')) + '\n')
                 f.close()
        except:
             print 'Data writting exception.'
    #def on_error(self, status_code, data):
    #  print status_code

def main():
    stream= TweetStreamer('HJSJE0dT8GYMOtgaKPm4tGNFW', 'Nd2NEziiW44TfaGUVANLLsXd9rJjMzax0ErZmDRgS7BRorDkuY', '713236429795528705-h4Fyou7iTB7l3eptFyLDt4Xt44B7CUT', '0aTBOL9ebkdtADwUYdaUHwgEgCKsmvStg3SiPuiSm83fC')#'PeH7lROp4ihy4QyK87FZg', '1BdUkBd9cQK6JcJPll7CkDPbfWEiOyBqqL2KKwT3Og','1683902912-j3558MXwXJ3uHIuZw8eRfolbEGrzN1zQO6UThc7', 'e286LQQTtkPhzmsEMnq679m7seqH4ofTDqeArDEgtXw' )
    stream.statuses.filter(locations=['-105.8701','34.5199','-105.8710','34.60'])
#locations=['-77.0364','38.8951','-75.9500','37.9500'] city of washingtonDC
#locations=['-94.9027','29.3838','-93.9037','29.5000'] city of texas
#locations='-102.0000', '23.0000', '-101.5000','23.5000' city of mexico
if __name__=='__main__':
    main()
