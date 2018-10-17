import re
import csv
def readCSV(nameFile):
    with open (nameFile, "r") as myfile:
        data = myfile.readlines()
    data = [line.replace('*','') for line in data]
    data = [line.replace('?','') for line in data]
    data = [line.strip() for line in data]
    return data
raw = readCSV('data.txt')
# raw = raw[0:10]
raw = [re.sub('[^a-zA-Z]', ' ', stri) for stri in raw]#https://stackoverflow.com/a/22521156
words = [line.split(" ") for line in raw]
def flatten(l):
    return [item for sublist in l for item in sublist]
    #https://stackoverflow.com/a/952952
words = flatten(words)
words = list(filter(None, words))#https://stackoverflow.com/a/3845453
wordset = list(set(words))
wordcount = [words.count(w) for w in wordset]
def writeCSV(nameFile,form):
    with open(nameFile +".csv", "w") as output:
        writer = csv.writer(output, lineterminator='\n')
        writer.writerows(form)
writeCSV('worddata',[[w] for w in wordset])
writeCSV('wordcount',[[c] for c in wordcount])
pass