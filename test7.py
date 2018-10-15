import csv
def readCSV(nameFile):
    with open (nameFile, "r") as myfile:
        data = myfile.readlines()
    data = [line.replace('*','') for line in data]
    data = [line.replace('?','') for line in data]
    data = [line.strip() for line in data]
    return data
words = readCSV('worddata.csv')
form = [[f] for f in words]
with open("words.csv", "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(form)