import pandas as pd
from gtts import gTTS
import nltk.tokenize



# Loading the Questions.csv and Tags.csv data sets into Python

# def answer_generation():
from TextToSpeech.TextToSpeechConversion import text_to_speech_conversion
from TextToSpeech.NewTest import question_selection

url1 = r"C:\Users\HP\Documents\Academic Folder\L4S1\Comprehensive Group Project\Stack Overflow Data Set\Questions.csv"
questionsDataFrame = pd.read_csv(url1, encoding='latin-1')

url2 = r"C:\Users\HP\Documents\Academic Folder\L4S1\Comprehensive Group Project\Stack Overflow Data Set\Answers.csv"
answersDataFrame = pd.read_csv(url2, encoding='latin-1')

mergedDataFrame = (pd.merge(questionsDataFrame, answersDataFrame, left_on='Id', right_on='ParentId', how='left'))
print("Merged successfully")

# retrieving questions from the data set
technical_Skill: str = "java"
selectedQuestionsList = question_selection(technical_Skill)
length = len(selectedQuestionsList)

for i in range(length):
    selectedQuestion = selectedQuestionsList[i]
    # print('Selected Question:' + selectedQuestion)

    # categorizing the questions into levels
    sentences = nltk.sent_tokenize(selectedQuestion, 'english')
    for sentence in sentences:
        print(sentence)

        for sentence in sentences:
            words = nltk.word_tokenize(sentence)
            # print(words)

            level1Words = ['What is', 'What are', 'Is it', 'Define', 'State', 'List', 'Recall', 'what is', 'what are',
                           'is it', 'define', 'state', 'list', 'recall']
            level2Words = ['Why', 'Explain', 'Classify', 'Describe', 'Discuss', 'Identify', 'why', 'explain',
                           'classify', 'describe', 'discuss', 'identify']
            level3Words = ['How', 'Demonstrate', 'Illustrate', 'Sketch', 'how', 'demonstrate', 'illustrate', 'sketch']

            for x in level1Words:
                if x in sentence:
                    print('This is a memory-recall question')
                    text_to_speech_conversion(sentence)
                    newdataframe1 = mergedDataFrame.loc[mergedDataFrame['Title'] == sentence]
                    selectedQuestions2 = newdataframe1.to_csv(columns=['ParentId'], sep='\t', index=False)
                    question = newdataframe1.to_csv(columns=['Body_y'], sep='\t', index=False)
                    print(newdataframe1)
                    print(selectedQuestions2)
                    print(question)
                    # answer = Speech_To_Text(sentence)
                    # result = evaluation(answer)

            for x in level2Words:
                if x in sentence:
                    print('This is a comprehensive level question')
                    text_to_speech_conversion(sentence)
                    newdataframe1 = mergedDataFrame.loc[mergedDataFrame['Title'] == sentence]
                    selectedQuestions2 = newdataframe1.to_csv(columns=['ParentId'], sep='\t', index=False)
                    question = newdataframe1.to_csv(columns=['Body_y'], sep='\t', index=False)
                    print(newdataframe1)
                    print(selectedQuestions2)
                    print(question)
                    # answer = Speech_To_Text(sentence)
                    # result = evaluation(answer)

            for x in level3Words:
                if x in sentence:
                    print('This is an application level question')
                    text_to_speech_conversion(sentence)
                    newdataframe1 = mergedDataFrame.loc[mergedDataFrame['Title'] == sentence]
                    selectedQuestions2 = newdataframe1.to_csv(columns=['ParentId'], sep='\t', index=False)
                    question = newdataframe1.to_csv(columns=['Body_y'], sep='\t', index=False)
                    print(newdataframe1)
                    print(selectedQuestions2)
                    print(question)
                    # answer = Speech_To_Text(sentence)
                    # result = evaluation(answer)

            else:
                print("Can not categorize the given question into defined levels")

# newdataframe = mergedDataFrame.loc[mergedDataFrame['ParentId'] == 90]
# selectedQuestions = newdataframe.to_csv(columns=['Title'], sep='\t', index=False)
# answer = newdataframe.to_csv(columns=['Body_y'], sep='\t', index=False)
# parentid = newdataframe.to_csv(columns=['ParentId'], sep='\t', index=False)
# print(newdataframe)
# print(selectedQuestions)
# print(answer)

# newdataframe1 = mergedDataFrame.loc[mergedDataFrame['Title'] == 'How to search a char array for a specific char?']
# selectedQuestions2 = newdataframe1.to_csv(columns=['ParentId'], sep='\t', index=False)
# question = newdataframe1.to_csv(columns=['Body_y'], sep='\t', index=False)
# print(newdataframe1)
# print(selectedQuestions2)
# print(question)