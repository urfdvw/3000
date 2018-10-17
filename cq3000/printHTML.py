chapter = 0
unit = 0

def readCSV(nameFile):
    with open (nameFile, "r",encoding='utf-8') as myfile:
        raw = myfile.readlines()
        data = [line.split(",") for line in raw]
        data = [[w.strip() for w in line] for line in data]
    return data

data = readCSV('data4print.csv')

data = [[int(d[0].encode('ascii', 'ignore')),d[2],','.join(d[3:len(d)])] for d in data]

def oneWord(en,ch):
    html_str = ''
    html_str += '<p style="font-size:70%;">\n ' + en +'<br/>\n'
    html_str += '&nbsp;&nbsp;&nbsp;&nbsp;' +ch +'<br/>\n</p>\n'
    return html_str

html_str = ''
for i in range(len(data)):
    d = data[i]
    if i%100 == 0:
        unit = 0
        chapter += 1
        html_str += '<HR>\n'
        html_str += '<h1> Chapter ' + str(chapter) + '<h1>'
    if i%10 == 0:
        unit += 1
        html_str += '<HR>\n'
        html_str += '<h2> Unit ' + str(unit) + ' '
        level = max(0,d[0])
        for i in range(level):
        # https://www.w3schools.com/charsets/ref_utf_symbols.asp
            html_str += '&#9733'
        for i in range(level,5):
            # https://www.w3schools.com/charsets/ref_utf_symbols.asp
            html_str += '&#9734'
        html_str += '<h2>'
    html_str += oneWord(d[1],d[2])
# https://stackoverflow.com/a/934173
import codecs
file = codecs.open("book2.html", "w", "utf-8")
file.write(html_str)
file.close()