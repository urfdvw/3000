# plot the frequecy level bar chart
import csv
import numpy as np
import matplotlib.pyplot as plt

def readCSV(nameFile):
    with open (nameFile, "r") as myfile:
        data = myfile.readlines()
    data = [line.replace('*','') for line in data]
    data = [line.replace('?','') for line in data]
    data = [line.strip() for line in data]
    return data
words = readCSV('worddata.csv')
level = readCSV('frequencyLevel.csv')

freq = []
count = []
for i in range(-1,6):
    freq.append(i)
    count.append(sum([1*(int(f) == i) for f in level]))
plt.figure()
plt.bar(freq,count)
plt.show()

frequency = readCSV('frequency.csv')
frequency = [int(f) for f in frequency]
for i in range(len(frequency)):
    if (frequency[i] <= 0):
        frequency[i] = 1

plt.figure()
plt.hist(np.log10(frequency),bins=100)
plt.show()