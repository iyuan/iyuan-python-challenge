import urllib
import string
url = 'http://www.pythonchallenge.com/pc/def/ocr.html'
content = urllib.urlopen(url).read()
index = content.index('%%')
print filter(lambda i:i in string.letters,content[index:])

