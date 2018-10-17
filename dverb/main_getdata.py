# get data
import urllib
import random
import time
import csv

def word2html(word):
    timeDelay = random.randrange(0, 1)
    time.sleep(timeDelay)
    url="https://www.collinsdictionary.com/dictionary/english/" + word
    req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"}) 
    con = urllib.request.urlopen( req )
    source = con.read().decode('utf-8')
    return source
 
def wordFrequency(source):
    ind = source.find("|0:")
    source = source[ind+3:-1]
    ind = source.find("\'")
    source = source[0:ind]
    return int(source)
import csv

def wordLevel(source):
    ind = source.find("data-band=")
    if ind < 0:
        return -1
    else:
        return int(source[ind+11])

def readCSV(nameFile):
    with open (nameFile, "r") as myfile:
        data = myfile.readlines()
    data = [line.replace('*','') for line in data]
    data = [line.replace('?','') for line in data]
    data = [line.strip() for line in data]
    return data

def writeCSV(nameFile,form):
    with open(nameFile +".csv", "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(form)

words = readCSV('worddata.csv')
# words = words[0:30]# for debug
frequency = []
level = []
form = []
i = 1
for w in words:
    print(w,i)
    i += 1
    try:
        html = word2html(w)
        try:
            f = wordFrequency(html)
        except:
            f = -1
        l = wordLevel(html)
    except:
        w = 'NA-' + w
        f = -1
        w = -1
    form.append([l,f,w])
    frequency.append([f])
    level.append([l])
writeCSV('report',form)
writeCSV('frequency',frequency)
writeCSV('frequencyLevel',level)
writeCSV('words',[[w] for w in words])


