from bs4 import BeautifulSoup
from urllib.request import urlopen

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

# to search
query = "java interview questions"

for j in search(query, tld="co.in", num=10, stop=1, pause=100):
    print(j)
    url = j
    html = urlopen(url)
    soup = BeautifulSoup(html, 'lxml')

    text = soup.text
    cleantext = BeautifulSoup(text, 'html5lib').text
    newtext = soup.get_text(strip=True)
    # print(newtext)

    tokens = [t for t in newtext.split()]
    print(tokens)

    level1Words = ['What is', 'What are', 'Is it', 'Define', 'State', 'List', 'Recall', 'what is', 'what are',
                   'is it', 'define', 'state', 'list', 'recall']
    level2Words = ['Why', 'Explain', 'Classify', 'Describe', 'Discuss', 'Identify', 'why', 'explain',
                   'classify', 'describe', 'discuss', 'identify']
    level3Words = ['How', 'Demonstrate', 'Illustrate', 'Sketch', 'how', 'demonstrate', 'illustrate', 'sketch']

    for x in level1Words:
        if x in tokens:
            print('This is a memory-recall question')

            # text_to_speech_conversion(sentence)
            # answer = text_to_speech_conversion(sentence)
            # result = evaluation(answer)

    for x in level2Words:
        if x in tokens:
            print('This is a comprehensive level question')
            # text_to_speech_conversion(sentence)
            # answer = text_to_speech_conversion(sentence)
            # result = evaluation(answer)

    for x in level3Words:
        if x in tokens:
            print('This is an application level question')
            # text_to_speech_conversion(sentence)
            # answer = text_to_speech_conversion(sentence)
            # result = evaluation(answer)

    else:
        print("Can not categorize the given question into defined levels")
