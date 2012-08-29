import urllib
import string
import re
url = 'http://www.pythonchallenge.com/pc/def/equality.html'
content = urllib.urlopen(url).read()
index = content.index('--')
p = re.compile(r'(?:^|[^A-Z])[A-Z]{3}([a-z])[A-Z]{3,3}(?:[^A-Z]|$)')
l=p.findall(content[index:])
print ''.join(l)
'''
import re
"".join(re.findall('[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]', text))

r = ""
   for i in range(4, len(s) - 4):
       if (s[i]+s[i-4]+s[i+4]).islower() and (s[i-3:i]+s[i+1:i+4]).isupper():
           r += s[i]

c=reduce(lambda x,y:x+y, map(lambda x:str(int(x.islower())), s))
res=''
x=0
while x>=0:
   res+=s[x+4]
   x=c.find('100010001', x+1)
res=res[1:]
print res

znaki = [""] * 9
znalezione = ""
for znak in dane:
    del znaki[0]
    znaki.append(znak)
    if \
        not znaki[0].isupper() and\
            znaki[1].isupper() and\
            znaki[2].isupper() and\
            znaki[3].isupper() and\
            znaki[4].islower() and\
            znaki[5].isupper() and\
            znaki[6].isupper() and\
            znaki[7].isupper() and\
        not znaki[8].isupper()    \
    :
        znalezione += znaki[4]
print(znalezione) # -->> "linkedlist"

markers = ''.join( [ '0' if c in string.lowercase else '1' for c in t2 ] )
def f( res, t2, markers ):
    n = len(markers.partition('011101110')[0])
    return f( res+t2[n+4], t2[n+9:], markers[n+9:] ) if n != len(markers) else res
print f( '', t2, markers )

'''
