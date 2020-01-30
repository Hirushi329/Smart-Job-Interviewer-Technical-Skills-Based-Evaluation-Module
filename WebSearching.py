from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://www.w3schools.com/java/java_encapsulation.asp"
html = urlopen(url)
soup = BeautifulSoup(html, 'lxml')

text = soup.text
cleantext = BeautifulSoup(text, 'html5lib').text
newtext = soup.get_text(strip = True)
print(newtext)

tokens = [t for t in newtext.split()]
print(tokens)

#if 'encapsulation' in cleantext:
    #print('Success!')
#else: print('Fail!')