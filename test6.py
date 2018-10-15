# plot the log-frequecy level bar chart
import csv
def readCSV(nameFile):
    with open (nameFile, "r") as myfile:
        data = myfile.readlines()
    data = [line.replace('*','') for line in data]
    data = [line.replace('?','') for line in data]
    data = [line.strip() for line in data]
    return data
words = readCSV('worddata.csv')
frequency = readCSV('frequency.csv')
frequency = [int(f) for f in frequency]
for i in range(len(frequency)):
    if (frequency[i] <= 0):
        frequency[i] = 1


import matplotlib.pyplot as plt
import numpy as np
plt.hist(np.log10(frequency),bins=100)
plt.show()
plt.plot(sorted(frequency))
plt.show()