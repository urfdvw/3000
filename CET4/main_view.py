# plot the frequecy level bar chart
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
#%% level count
freq = []
count = []
for i in range(-1,6):
    freq.append(i)
    count.append(sum([1*(int(f) == i) for f in level]))
plt.figure()
plt.bar(freq,count)
plt.show()

#%% original frequency and word count
frequency = readCSV('frequency.csv')
frequency = [float(f) for f in frequency]
nf = np.array(frequency)
nf[nf<=0] = 0.1

plt.figure()
plt.hist(np.log10(nf),bins=100)
plt.show()

#%% frequency and word count after sensored
level = [int(l) for l in level]

ind = [l in [2,3,4] for l in level]
nf = nf[ind]

plt.figure()
plt.hist(np.log10(nf),bins=100)
plt.show()