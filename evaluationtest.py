# This class is responsible for comparing the two text vectors and providing the percentage for the technical capability

import nltk.stem.wordnet
import nltk.tokenize
from TextToSpeech import SpeechToText
from nltk.stem import PorterStemmer
try:
    answer1 = 'This is the programme for evaluating the answer given by the candidate and the answer generated from the Stack Overflow'
    answer2 = 'This programme is used for measuring the similarity between the candidates answer and the generated answer'

    lemmatizer = nltk.WordNetLemmatizer()
    newWordsString1: str = " "
    newWordsString2: str = " "
    Answer1 = nltk.sent_tokenize(answer1, 'english')
    for sentences1 in Answer1:
        words1 = nltk.word_tokenize(sentences1)
        # print(words1)
        for w in words1:
            # newWords1 = porter.stem(w)
            newWords1 = lemmatizer.lemmatize(w)
            # print(newWords1)
            newWordsString1 = newWordsString1 + " " + newWords1
            # print(newWordsString1)

    Answer2 = nltk.sent_tokenize(answer2, 'english')
    for sentences2 in Answer2:
        words2 = nltk.word_tokenize(sentences2)
        # print(words2)
        for w in words2:
            # newWords2 = porter.stem(w)
            newWords2 = lemmatizer.lemmatize(w)
            # print(newWords2)
            newWordsString2 = newWordsString2 + " " + newWords2
            # print(newWordsString2)

        # Similarity is calculated using Jaccard similarity

        print('..................',newWordsString1)
        print('..................',newWordsString2)
        a = set(newWordsString1.split())
        print(a)
        b = set(newWordsString2.split())
        print(b)
        c = a.intersection(b)
        print(c)
        x = float(len(c)) / (len(a) + len(b) - len(c))
        print(x)
except:
    string = "Candidate has not given an answer. The score is 0"

