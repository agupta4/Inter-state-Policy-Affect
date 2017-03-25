# -*- coding: utf-8 -*-
"""
Created on Fri Apr 08 13:08:21 2016

@author: ETHICAL DRUIDS
"""

"""
This file is been made to sort out the twitter data in tsb format
"""
import csv,json,sys
from pattern.en import sentiment
reload(sys)
sys.setdefaultencoding("utf-8")
f2 = open('Current.txt', 'w')

def PopulateCSV2(writer, filename, count, city):
    print count
    with open(filename, 'r') as f:
        for line in f:
            count = count+1
            tweet = json.loads(line)
            lst = tweet
            f2.write(json.dumps([lst, city])+'\r\n')
    return count

def PopulateCSV3(writer, filename, count, city):
    print count
    with open(filename, 'r') as f:
        for line in f:
            count = count+1            
            tweet = json.loads(line)
            t = tweet['Tweet_text']
            lst = t
            f2.write(json.dumps([lst, city])+'\r\n')
    return count
"""
Evaluating sentiment score and appending file data in one file
"""             
def main():
    count = 0
    f1 = open("ProjectData.csv", "w")
    writer = csv.writer(f1);
    filename = "ArkansasText.txt"
    count = PopulateCSV3(writer, filename, count, "Arkansas")
    filename2 = "data/2016_03_24/WashingtonDC.txt"    
    count = PopulateCSV2(writer, filename2, count, "Washington")
    filename3 = "data/2016_03_25/WashingtonDC.txt"
    count = PopulateCSV2(writer, filename3, count, "Washington")
    filename4 = "data/2016_03_25/WashingtonDC2.txt"
    count = PopulateCSV2(writer, filename4, count, "Washington")
    filename5 = "data/2016_03_28/WashingtonDC3.txt"
    count = PopulateCSV2(writer, filename5, count, "Washington")
    filename6 = "data/2016_03_28/Texas_1.txt"
    count = PopulateCSV2(writer, filename6, count, "Texas")
    filename7 = "mexicoText.txt"
    count = PopulateCSV3(writer, filename7, count, "Mexico")
    filename8 = "TexasText.txt"
    count = PopulateCSV3(writer, filename8, count, "Texas")
    filename9 = "M_wash_new.txt"
    count = PopulateCSV3(writer, filename9, count, 'Washington')
    f2.close();
if __name__ == '__main__':
    main()