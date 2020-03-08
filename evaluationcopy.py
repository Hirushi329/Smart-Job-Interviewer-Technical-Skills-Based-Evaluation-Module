# This class is responsible for comparing the two text vectors and providing the percentage for the technical capability

import nltk.stem.wordnet
import nltk.tokenize
from nltk.corpus import stopwords

from TextToSpeech import SpeechToText
from nltk.stem import PorterStemmer

def evaluation(answer1, answer2):
    try:
        print(answer2)

        # Words in the answers should be tokenized and lemmatized before calculating the similarity
        # porter = PorterStemmer()

        lemmatizer = nltk.WordNetLemmatizer()
        newWordsString1: str = " "
        newWordsString2: str = " "
        Answer1 = nltk.sent_tokenize(answer1, 'english')
        stop_words = set(stopwords.words('english'))

        # Tokenizing the answer1
        for sentences1 in Answer1:
            words1 = nltk.word_tokenize(sentences1)
            # print(words1)

            # Lemmatizing the answer1
            for w in words1:
                # newWords1 = porter.stem(w)
                newWords1 = lemmatizer.lemmatize(w)
                # print(newWords1)
                newWordsString1 = newWordsString1 + " " + newWords1
                # print(newWordsString1)

                # Removing stop words from answer1
                word_tokens1 = nltk.word_tokenize(newWordsString1)
                filtered_sentence1 = [w for w in word_tokens1 if not w in stop_words]
                filtered_sentence1 = []

                for w in word_tokens1:
                    if w not in stop_words:
                        filtered_sentence1.append(w)


        # Tokenizing the answer2
        Answer2 = nltk.sent_tokenize(answer2, 'english')
        for sentences2 in Answer2:
            words2 = nltk.word_tokenize(sentences2)
            # print(words2)
            # Lemmatizing the answer2
            for w in words2:
                # newWords2 = porter.stem(w)
                newWords2 = lemmatizer.lemmatize(w)
                # print(newWords2)
                newWordsString2 = newWordsString2 + " " + newWords2
                # print(newWordsString2)

                # Removing stop words from answer2
                word_tokens2 = nltk.word_tokenize(newWordsString2)
                filtered_sentence2 = [w for w in word_tokens2 if not w in stop_words]
                filtered_sentence2 = []

                for w in word_tokens2:
                    if w not in stop_words:
                        filtered_sentence2.append(w)

            print(filtered_sentence1)
            print(filtered_sentence2)
            print('Calculating the similarity...........')
            a = set(filtered_sentence1)
            b = set(filtered_sentence2)
            c = a.intersection(b)
            print(c)
            x = float(len(c)) / (len(filtered_sentence1) + len(filtered_sentence2) - len(c))
            print(x)
            return x
    except:
        string = "Candidate has not given an answer. The score is 0"
        return string
