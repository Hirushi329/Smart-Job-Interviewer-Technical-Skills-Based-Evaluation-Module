import nltk
from bs4 import BeautifulSoup
from urllib.request import urlopen
from TextToSpeech.TextToSpeechConversion import text_to_speech_conversion


level1Words = ['What is', 'What are', 'Is it', 'Define', 'State', 'List', 'Recall', 'what is', 'what are',
               'is it', 'define', 'state', 'list', 'recall']
level2Words = ['Why', 'Explain', 'Classify', 'Describe', 'Discuss', 'Identify', 'why', 'explain',
               'classify', 'describe', 'discuss', 'identify']
level3Words = ['How', 'Demonstrate', 'Illustrate', 'Sketch', 'how', 'demonstrate', 'illustrate', 'sketch']
try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

# to search
query = "sql interview questions"

for j in search(query, tld="co.in", num=10, stop=1, pause=100):
    print(j)
    url = j
    html = urlopen(url)
    soup = BeautifulSoup(html, 'lxml')

    text = soup.text
    cleantext = BeautifulSoup(text, 'html5lib').prettify()
    newtext = soup.get_text(strip=True)
    # print(newtext)

    # ntext = tokenize.sent_tokenize(newtext)
    # print(ntext)

    tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences = tokenizer.tokenize(newtext)
    # print('\n'.join(sentences))

    for sentence in sentences:
        words = nltk.word_tokenize(sentence)
        # print(words)
        for x in level1Words:
            if x in sentence:
                print("This is a memory recall question:", sentence)
                # print(sentence)
                newSentencelist = sentence.split(x)
                # print("new sentence is", newSentencelist)
                phrase = newSentencelist[1]
                # print(newSentencelist[1])
                # print(phrase)
                # print(x)
                question = x+newSentencelist[1]
                answerlist = question.split('?')
                print(answerlist)
                length = len(answerlist)
                print(length)
                answer = answerlist[length-1]
                print("The question is:", question)
                text_to_speech_conversion(question)
                print("The answer is:", answer)
                # text_to_speech_conversion(question)
        for x in level2Words:
            if x in sentence:
                print("This is a comprehension level question:", sentence)
                # print(sentence)
                newSentencelist = sentence.split(x)
                # print("new sentence is", newSentencelist)
                phrase = newSentencelist[1]
                # print(newSentencelist[1])
                # print(phrase)
                # print(x)
                question = x + newSentencelist[1]
                answerlist = question.split('?')
                print(answerlist)
                length = len(answerlist)
                print(length)
                answer = answerlist[length-1]
                print("The question is:", question)
                text_to_speech_conversion(question)
                print("The answer is:", answer)
        for x in level3Words:
            if x in sentence:
                print("This is an application level question:", sentence)
                # print(sentence)
                newSentencelist = sentence.split(x)
                # print("new sentence is", newSentencelist)
                phrase = newSentencelist[1]
                # print(newSentencelist[1])
                # print(phrase)
                # print(x)
                question = x + newSentencelist[1]
                answerlist = question.split('?')
                print(answerlist)
                length = len(answerlist)
                answer = answerlist[length-1]
                print(length)
                print("The question is:", question)
                text_to_speech_conversion(question)
                print("The answer is:", answer)



    # for x in level1Words:
    #     if x in tokens:
    #         print('This is a memory-recall question')
    #
    #         # text_to_speech_conversion(sentence)
    #         # answer = text_to_speech_conversion(sentence)
    #         # result = evaluation(answer)
    #
    # for x in level2Words:
    #     if x in tokens:
    #         print('This is a comprehensive level question')
    #         # text_to_speech_conversion(sentence)
    #         # answer = text_to_speech_conversion(sentence)
    #         # result = evaluation(answer)
    #
    # for x in level3Words:
    #     if x in tokens:
    #         print('This is an application level question')
    #         # text_to_speech_conversion(sentence)
    #         # answer = text_to_speech_conversion(sentence)
    #         # result = evaluation(answer)
    #
    # else:
    #     print("Can not categorize the given question into defined levels")
