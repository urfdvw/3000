# get the frequency level of words in the data file
import urllib
def wordFrequency(word):
    url="https://www.collinsdictionary.com/dictionary/english/" + word
    req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"}) 
    con = urllib.request.urlopen( req )
    source = con.read().decode('utf-8')
    ind = source.find("data-band=")
    if ind < 0:
        return -1
    else:
        return int(source[ind+11])
import csv
def readCSV(nameFile):
    with open (nameFile, "r") as myfile:
        data = myfile.readlines()
    data = [line.replace('*','') for line in data]
    data = [line.replace('?','') for line in data]
    data = [line.strip() for line in data]
    return data
words = readCSV('worddata.csv')
frequency = []
for w in words:
    print(w)
    frequency.append(wordFrequency(w))
pass
form = [[f] for f in frequency]
with open("frequencyLevel.csv", "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(form)