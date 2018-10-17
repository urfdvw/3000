# Getting example for each level
import csv
def readCSV(nameFile):
    with open (nameFile, "r") as myfile:
        data = myfile.readlines()
    data = [line.replace('*','') for line in data]
    data = [line.replace('?','') for line in data]
    data = [line.strip() for line in data]
    return data
words = readCSV('worddata.csv')
frequency = readCSV('frequencyLevel.csv')

for level in range(1,6):
    for i in range(len(words)):
        if(frequency[i]==str(level)):
            print(words[i])
            break