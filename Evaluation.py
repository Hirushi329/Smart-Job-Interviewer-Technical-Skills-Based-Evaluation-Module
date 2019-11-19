# This class is responsible for comparing the two text vectors and providing the percentage for the technical capability

import nltk.stem.wordnet
import nltk.tokenize
from nltk.stem import PorterStemmer

answer1: str = "AI is our friends and it has been friendly. This is the answers given in the stack overflow."
answer2: str = "AI and humans have always been friendly. This is the answers given by the interviewee."

# Words in the answers should be tokenized and lemmatized before calculating the similarity
# porter = PorterStemmer()

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

print(newWordsString1)
print(newWordsString2)
a = set(newWordsString1.split())
b = set(newWordsString2.split())
c = a.intersection(b)
x = float(len(c)) / (len(a) + len(b) - len(c))
print(x)

