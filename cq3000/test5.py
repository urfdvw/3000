# Get word frequency count
import urllib
import random
import time
 
def wordFrequency(word):
    timeDelay = random.randrange(0, 1)
    time.sleep(timeDelay)
    url="https://www.collinsdictionary.com/dictionary/english/" + word
    req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"}) 
    con = urllib.request.urlopen( req )
    source = con.read().decode('utf-8')
    ind = source.find("|0:")
    source = source[ind+3:-1]
    ind = source.find("\'")
    source = source[0:ind]
    return int(source)
import csv
def readCSV(nameFile):
    with open (nameFile, "r") as myfile:
        data = myfile.readlines()
    data = [line.replace('*','') for line in data]
    data = [line.replace('?','') for line in data]
    data = [line.strip() for line in data]
    return data
words = readCSV('worddata.csv')
# words = words[0:10]
frequency = []
for w in words:
    try:
        f = wordFrequency(w)
    except:
        f = -1
    frequency.append(f)
    print(w,f)
pass
form = [[f] for f in frequency]
with open("frequency.csv", "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(form)