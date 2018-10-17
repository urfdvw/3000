import urllib
import random
import time
import codecs
from bs4 import BeautifulSoup
def word2html(word):
#    timeDelay = random.randrange(0, 1)
#    time.sleep(timeDelay)
    url="https://www.collinsdictionary.com/us/dictionary/english-chinese/" + word
    req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"}) 
    con = urllib.request.urlopen( req )
    source = con.read().decode('utf-8')
    return source
def readCSV(nameFile):
    with open (nameFile, "r") as myfile:
        data = myfile.readlines()
    data = [line.replace('*','') for line in data]
    data = [line.replace('?','') for line in data]
    data = [line.strip() for line in data]
    return data

words = readCSV('worddata2.csv')
frequency = readCSV('frequency2.csv')

for i in reversed(range(1,len(words))):
    if frequency[i] == frequency[i-1]:
        if words[i][1:2] == words[i-1][1:2]:
            words.remove(words[i])
            frequency.remove(frequency[i])
            
#words = words[0:10]
#words = ['arise','take']
html_str = ''
n = 0
for w in words:
    source = word2html(w)
    print(w,n)
    # https://stackoverflow.com/a/38791471
    soup = BeautifulSoup(source, 'html.parser')
    meaning = soup.find_all('div', class_='hom')
    if len(meaning)>0:
        html_str += '<HR>'
        beginmarker = 'Chinese Translation of &ldquo;'
        ind = source.find(beginmarker) + len(beginmarker)
        source = source[ind:-1]
        endmarker = '&rdquo'
        ind = source.find(endmarker)
        realword = source[0:ind]
        html_str += '<h1>' + realword + '</h1>'
        n += 1
    for m in meaning:
        html_str += str(m) + '\n'
    if n%10 == 1:
        # https://stackoverflow.com/a/934173
        file = codecs.open("book2.html", "w", "utf-8")
        file.write(html_str)
        file.close()