import urllib.request

import nltk

response =  urllib.request.urlopen('https://www.w3schools.com/java/java_encapsulation.asp')
html = response.read()

from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'html5lib')
text = soup.get_text(strip = True)

tokens = [t for t in text.split()]
print(tokens)

from nltk.corpus import stopwords

sr = stopwords.words('english')
clean_tokens = tokens[:]
for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)
freq = nltk.FreqDist(clean_tokens)
for key, val in freq.items():
    print(str(key) + ':' + str(val))
freq.plot(20, cumulative=False)