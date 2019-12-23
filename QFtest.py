# This class is responsible for filtering questions according to the technical skills
import os
import pandas as pd
from gtts import gTTS
import nltk.tokenize


# Loading the Questions.csv and Tags.csv data sets into Python
url1 = r"C:\Users\HP\Documents\Academic Folder\L4S1\Comprehensive Group Project\Stack Overflow Data Set\Questions.csv"
questionsDataFrame = pd.read_csv(url1, encoding='latin-1')

url2 = r"C:\Users\HP\Documents\Academic Folder\L4S1\Comprehensive Group Project\Stack Overflow Data Set\Tags.csv"
tagsDataFrame = pd.read_csv(url2, encoding='latin-1')

mergedDataFrame = (pd.merge(questionsDataFrame, tagsDataFrame, left_on='Id', right_on='Id', how='left'))


sampleDataFrame = mergedDataFrame.sample(n=100, replace=True, weights=None, random_state=None, axis=None)
grouped_dataframe = sampleDataFrame.groupby('Tag')
selectedDataFrame = grouped_dataframe.get_group('java')
selectedQuestions = selectedDataFrame.to_csv(columns=['Title'], sep='\t', index=False)
print(selectedQuestions)
selectedQuestionsList = []
selectedQuestionsList = selectedQuestions.split("\n")
print(selectedQuestionsList)
length = len(selectedQuestionsList)

for i in range(length):
    selectedQuestion = selectedQuestionsList[i]
    print('Selected Question:' + selectedQuestion)

    # Categorizing questions
    sentences = nltk.sent_tokenize(selectedQuestion, 'english')
    for sentence in sentences:
        print(sentence)

        for sentence in sentences:
            words = nltk.word_tokenize(sentence)
            print(words)

            level1Words = ['What is', 'What are', 'Is it', 'Define', 'State', 'List', 'Recall', 'what is', 'what are',
                           'is it', 'define', 'state', 'list', 'recall']
            level2Words = ['Why', 'Explain', 'Classify', 'Describe', 'Discuss', 'Identify', 'why', 'explain',
                           'classify', 'describe', 'discuss', 'identify']
            level3Words = ['How', 'Demonstrate', 'Illustrate', 'Sketch', 'how', 'demonstrate', 'illustrate', 'sketch']

            for x in level1Words:
                if x in sentence:
                    print('This is a memory-recall question')

            for x in level2Words:
                if x in sentence:
                    print('This is a comprehensive level question')

            for x in level3Words:
                if x in sentence:
                    print('This is an application level question')

            else:
                print("Can not categorize the given question into defined levels")


    language = 'en'
    myobj = gTTS(text=selectedQuestion, lang=language, slow=False)
    myobj.save("Question.mp3")
    os.system("Question.mp3")



