# testing urllib function
import urllib
url="https://www.collinsdictionary.com/dictionary/english/girl"
req = urllib.request.Request(url, headers={'User-Agent' : "Magic Browser"}) 
con = urllib.request.urlopen( req )
source = con.read().decode('utf-8')
ind = source.find("data-band=")
print(int(source[ind+11]))
