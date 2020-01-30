from bs4 import BeautifulSoup
from urllib.request import urlopen

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

# to search
query = "java"

for j in search(query, tld="co.in", num=10, stop=1, pause=100):
    print(j)
    url = j
    html = urlopen(url)
    soup = BeautifulSoup(html, 'lxml')

    text = soup.text
    cleantext = BeautifulSoup(text, 'html5lib').text
    newtext = soup.get_text(strip=True)
    print(newtext)

    tokens = [t for t in newtext.split()]
    print(tokens)

    # if 'encapsulation' in cleantext:
    # print('Success!')
    # else: print('Fail!')