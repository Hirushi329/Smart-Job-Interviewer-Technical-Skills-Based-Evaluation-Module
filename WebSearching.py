import inline as inline
import pandas
import numpy
import matplotlib.pyplot
import seaborn
#matplotlib inline
import pymongo

from urllib.request import urlopen

import soup as soup
from bs4 import BeautifulSoup

#myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#mydb = myclient["mydatabase"]
#mycollection = mydb["keywords"]
#myquery = {"keyword": "Java"}
#mydocument = mycollection.find(myquery)
#value = mydocument.distinct("url")
#print(value)
#url = value.split("'")
#print(url)

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