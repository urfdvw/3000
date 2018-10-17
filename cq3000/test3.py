# plot the frequecy level bar chart
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

import matplotlib.pyplot as plt
freq = []
count = []
for i in range(-1,6):
    freq.append(i)
    count.append(sum([1*(int(f) == i) for f in frequency]))
plt.bar(freq,count)
plt.show()