# Responsible for carrying out the execution flow
import nltk
import pandas as pd

from TextToSpeech.NewTest import question_selection
from TextToSpeech.TextToSpeechConversion import text_to_speech_conversion
from TextToSpeech.SpeechToText import speech_to_text
from TextToSpeech.Evaluation import evaluation

# retrieving the technical skills from the database

# retrieving questions from the data set
def run():
    print('Request received. Starting the Interview......')
    result_list = []
    url1 = r"C:\Users\HP\Desktop\Comprehensive Group Project\Stack Overflow Data Set\Questions.csv"
    questionsDataFrame = pd.read_csv(url1, encoding='latin-1')

    url2 = r"C:\Users\HP\Desktop\Comprehensive Group Project\Stack Overflow Data Set\Answers.csv"
    answersDataFrame = pd.read_csv(url2, encoding='latin-1')

    mergedDataFrame = (pd.merge(questionsDataFrame, answersDataFrame, left_on='Id', right_on='ParentId', how='left'))
    print("Merged successfully")

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

                level1Words = ['What is', 'What are', 'Is it', 'Define', 'Recall', 'what is', 'what are',
                           'is it', 'define', 'recall', 'Is there', 'Are there', 'is there', 'are there', 'What', 'what']
                level2Words = ['Why', 'Explain', 'Classify', 'Describe', 'Discuss', 'Identify', 'why', 'explain',
                           'classify', 'describe', 'discuss', 'identify']
                level3Words = ['How', 'Demonstrate', 'Illustrate', 'Sketch', 'how', 'demonstrate', 'illustrate', 'sketch']

                for x in level1Words:
                    if x in sentence:
                        print('This is a memory-recall question')
                        newdataframe1 = mergedDataFrame.loc[mergedDataFrame['Title'] == sentence]
                        selectedQuestions2 = newdataframe1.to_csv(columns=['ParentId'], sep='\t', index=False)
                        question = newdataframe1.to_csv(columns=['Body_y'], sep='\t', index=False)
                        print(newdataframe1)
                        print(selectedQuestions2)
                        print(question)
                        text_to_speech_conversion(sentence)
                        answer = speech_to_text()
                        result = evaluation(question, answer)
                        final_result = 'The result for the memory-recall question is ', result
                        print(final_result)
                        result_list.append(final_result)

                for x in level2Words:
                    if x in sentence:
                        print('This is a comprehensive level question')
                        newdataframe1 = mergedDataFrame.loc[mergedDataFrame['Title'] == sentence]
                        selectedQuestions2 = newdataframe1.to_csv(columns=['ParentId'], sep='\t', index=False)
                        question = newdataframe1.to_csv(columns=['Body_y'], sep='\t', index=False)
                        print(newdataframe1)
                        print(selectedQuestions2)
                        print(question)
                        text_to_speech_conversion(sentence)
                        answer = speech_to_text()
                        result = evaluation(question, answer)
                        final_result = "The result of the comprehension level question is ", result
                        print(final_result)
                        result_list.append(final_result)

                for x in level3Words:
                    if x in sentence:
                        print('This is an application level question')
                        newdataframe1 = mergedDataFrame.loc[mergedDataFrame['Title'] == sentence]
                        selectedQuestions2 = newdataframe1.to_csv(columns=['ParentId'], sep='\t', index=False)
                        question = newdataframe1.to_csv(columns=['Body_y'], sep='\t', index=False)
                        print(newdataframe1)
                        print(selectedQuestions2)
                        print(question)
                        text_to_speech_conversion(sentence)
                        answer = speech_to_text()
                        result = evaluation(question, answer)
                        final_result = "The result of the application level question is ", result
                        print(final_result)
                        result_list.append(final_result)

                else:
                    print("Can not categorize the given question into defined levels")

    # return('\n'.join('{}: {}'.format(*k) for k in enumerate(result_list)))
    string = str(result_list)
    newlist1 = string.split(')')
    string1 = str(newlist1)
    newlist2 = string1.split('(')
    string2 = str(newlist2)
    newstring1 = ('\n'.join(newlist2))
    print(newstring1)
    return newstring1