import nltk
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
from lxml.html import fromstring
from lxml.html import tostring

# def answer_generation(question):
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

# to search
question = "What Are OOP Concepts in Java?"

for j in search(question, tld="co.in", num=10, stop=1, pause=100):
    print(j)
    url = j
    html = urlopen(url)
    soup = BeautifulSoup(html, 'lxml')

    text = soup.text
    cleantext = BeautifulSoup(text, 'html5lib').prettify()
    newtext = soup.get_text(strip=True)
    print(newtext)

    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences = tokenizer.tokenize(newtext)
    print(sentences)
    if question in sentences:
        print("Success")
    else:
        print("Fail")

